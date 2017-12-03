import defs
import textToSpeech
import threading

WORD_THRESHOLD = 10


def get_definitions(sentence, exclude):
    parts_of_speech = defs.get_pos(sentence)
    uncommon_words = defs.filter_words(parts_of_speech, exclude)
    return defs.get_definitions(uncommon_words)


def thread_work(voice_input, common_words, word_list, threads):
    # gets definitions
    definitions = get_definitions(voice_input, common_words)
    # formats the definitions
    formatted_definitions = textToSpeech.parse_definitions(definitions)
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
    common_words = defs.get_common_words()
    threads = []
    word_list = []
    done = False
    while not done:
        voice_input = defs.speech_to_text()
        if "conversation over" not in voice_input.lower():
            # start a thread here
            thread = threading.Thread(target=thread_work, args=[voice_input, common_words, word_list, threads])
            threads.append(thread)
            thread.start()
        else:
            done = True
    # make sure that all threads are finished
    threads[-1].join()
    textToSpeech.speak_many_things(word_list)
    return word_list


if __name__ == '__main__':
    main()
