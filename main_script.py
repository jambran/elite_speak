from models import define, words, speech
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
    if len(formatted_definitions) != 0:
        #print(formatted_definitions)
        words.pretty_print_words(formatted_definitions)
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
            my_words[k] = (my_words[k][0] + 1, my_words[k][1], time.time())
            print(k + str(my_words[k]))
        except KeyError:
            my_words[k] = (1, str(definition_list[k]), time.time())
    word_list[::-1]


def main():
    r = sr.Recognizer()
    common_words = words.get_common_words()
    # open the picklejar to remember what's already been defined
    try:
        input = open("pickle_jar.pkl", 'rb')
        my_words = load(input)
        input.close()
    except FileNotFoundError:
        # my_words[defined word] = (numTimesDefined, definition)
        my_words = {}
    threads = []
    word_list = []
    while not done:
        voice_input = speech.listen(r)
        # start a thread here
        thread = threading.Thread(target=thread_work, args=[voice_input, common_words, word_list, r, threads, my_words])
        threads.append(thread)
        thread.start()
    # make sure that all threads are finished
    threads[-1].join()
    # textToSpeech.speak_many_things(word_list)
    # pickle my_words
    output = open("pickle_jar.pkl", 'wb')
    dump(my_words, output, -1)
    output.close()
    return word_list


def main_console():
    print('Elite Speak \nby Alex T. Reese, Ellis Miranda, Jamie Brandon, Kirsten Stallings\n')
    # use this to set up a certain level of word use as our list
    vocab_level = input("Select grade level:\n1 : Elementary School\n2 : High School\n3 : College\n")
    finished = False
    while not finished:
        start = input("\n1 : Start listening\n2 : Quit\n")
        if start == '1':
            main()
            # words.print_my_words(my_words)
        else:
            finished = True


if __name__ == '__main__':
    main_console()
