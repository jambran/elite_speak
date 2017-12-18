from models import define, words, speech, user, flashcard as f
import threading
import speech_recognition as sr
from pickle import dump
from pickle import load
import time

WORD_THRESHOLD = 10 # max number of definitions it'll give after any input
MAX_TIMES_WORD_DEF_DISPLAYED = 4 # will show definition this many times, then assume that you remember it
DEF_NOT_DISPLAYED_WITHIN_TIME = 60 * 60 * 24 * 3 # if the word has been defined in this time frame, assumes you remember the definition
done = False


def get_definitions(sentence, exclude, my_words):
    parts_of_speech = words.get_pos(sentence)
    uncommon_words = words.filter_words(parts_of_speech, exclude, my_words)
    return define.generate_definitions(uncommon_words)


def thread_work(voice_input, common_words, word_list, r, threads, my_words):
    voice_text = speech.recognize(voice_input, r)
    if "conversation over" in voice_text.lower():
        global done
        done = True
        return done
    # gets definitions
    definition_list = get_definitions(voice_text, common_words, my_words)
    # formats the definitions
    formatted_definitions = define.parse_speakable_definitions(definition_list)
    # grab the index of this thread in the list
    index = threads.index(threading.current_thread())
    # await the previous thread
    if index != 0:
        threads[index-1].join()

    # will reorganize the list to include new entries (theoretically this works)
    word_list[::-1]
    word_list.extend(formatted_definitions)
    if len(word_list) > WORD_THRESHOLD:
        word_list = word_list[len(list) - WORD_THRESHOLD:]
    # put words and defs in personal dictionary, my_words
    for k in definition_list:
        try:
            my_words[k] = (my_words[k][0] + 1, my_words[k][1], time.time(), my_words[k][3])
        except KeyError:
            my_words[k] = (1, definition_list[k]['def'], time.time(), definition_list[k]['pos'])
        words.pretty_print_word(k, my_words)
    word_list[::-1]


def listener(username, vocab_words):
    r = sr.Recognizer()
    my_class = open_pickle_jar(username)
    my_words = my_class.get_word_list()
    threads = []
    word_list = []
    while not done:
        voice_input = speech.listen(r)
        # start a thread here
        thread = threading.Thread(target=thread_work, args=[voice_input, vocab_words, word_list, r, threads, my_words])
        threads.append(thread)
        thread.start()
    # make sure that all threads are finished
    threads[-1].join()
    # textToSpeech.speak_many_things(word_list)
    # pickle my_words
    words.print_my_words(my_words)
    word_to_add = input("Add a word here to your vocabulary so it doesn\'t come up again by typing in its name below or hit Enter to continue:\n>")
    while(word_to_add != ""):
        if word_to_add in my_words:
            my_words.pop(word_to_add, None)
            my_class.add_to_known_words(word_to_add)
            words.print_my_words(my_words)
            word_to_add = input("Word added. Add another or hit Enter to continue:\n>")
        else:
            word_to_add = input("Unrecognized input. Add a word or hit Enter to continue:\n>")
    output = open(username + ".pkl", 'wb')
    dump(my_class, output, -1)
    output.close()
    
    
    return word_list


def main_console():
    print('Elite Speak \nby Alex T. Reese, Ellis Miranda, Jamie Brandon, Kirsten Stallings\n')
    # open the pickled users
    try:
        userfile = open('users.pkl', 'rb')
        users = load(userfile)
        userfile.close()
    except FileNotFoundError:
        # my_words[defined word] = (numTimesDefined, definition)
        users = []
    # Look for the user in users
    found = False
    while(not found):
        login = input("Press L to log in, N for new user: ")
        if (login == 'L' or login == 'l'):
            username = input("Enter your username: ")
            if(username in users):
                my_class = open_pickle_jar(username)
                my_words = my_class.get_word_list()
                vocab_words = my_class.get_known_words()
                found = True
            else:
                print("Username not found. Please try again. ")
        elif(login == 'N' or login == 'n'):
            username = input("Please enter your username: ")
            if(username not in users):
                # use this to set up a certain level of word use as our list
                vocab_level = input("Select grade level:\n1 : Elementary School\n2 : High School\n3 : College\n4 : Take quiz\n")
                while vocab_level != '1' and vocab_level != '2' and vocab_level != '3' and vocab_level != '4':
                    print("Invalid selection!\n")
                    vocab_level = input("Select grade level:\n1 : Elementary School\n2 : High School\n3 : College\n4 : Take quiz\n")
                vocab_words = words.get_common_words(vocab_level)
                users.append(username)
                output = open("users.pkl", 'wb')
                dump(users, output, -1)
                output.close()
                #my_words = open_pickle_jar(username)
                found = True
                new_user = user.User(username, {}, vocab_words)
                output = open(username + ".pkl", 'wb')
                dump(new_user, output, -1)
                output.close()
            else:
                print("Username already taken.")

    
    finished = False
    while not finished:
        start = input("\n1 : Start listening\n2 : Flashcard Practice\n3 : Quit\n")
        if start == '1':
            listener(username, vocab_words)
        elif(start == '2'):
            my_class = open_pickle_jar(username)
            my_words = my_class.get_word_list()
            f.flashcard_practice(my_words)
        else:
            finished = True



def open_pickle_jar(picklejar):
    # open the picklejar to remember what's already been defined
    try:
        input = open(picklejar + '.pkl', 'rb')
        my_class = load(input)
        #my_words = my_class.get_word_list()
        input.close()
    except FileNotFoundError:
        # my_words[defined word] = (numTimesDefined, definition)
        my_class = user.User("",{},{})
    return my_class
    
if __name__ == '__main__':
    main_console()
