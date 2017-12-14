from models import define, words, speech
import threading
import speech_recognition as sr

WORD_THRESHOLD = 10
done = False


def get_definitions(sentence, exclude):
    parts_of_speech = words.get_pos(sentence)
    uncommon_words = words.filter_words(parts_of_speech, exclude)
    return define.generate_definitions(uncommon_words)


def thread_work(voice_input, common_words, word_list, r, threads):
    voice_text = speech.recognize(voice_input, r)
    if "conversation over" in voice_text.lower():
        global done
        done = True
        return done
    # gets definitions
    definition_list = get_definitions(voice_text, common_words)
    # formats the definitions
    formatted_definitions = define.parse_speakable_definitions(definition_list)
    if len(formatted_definitions) != 0:
        print(formatted_definitions)
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
    word_list[::-1]


def main():
    r = sr.Recognizer()
    common_words = words.get_common_words()
    threads = []
    word_list = []
    while not done:
        voice_input = speech.listen(r)
        # start a thread here
        thread = threading.Thread(target=thread_work, args=[voice_input, common_words, word_list, r, threads])
        threads.append(thread)
        thread.start()
    # make sure that all threads are finished
    threads[-1].join()
    # textToSpeech.speak_many_things(word_list)
    return word_list


if __name__ == '__main__':
    main()
