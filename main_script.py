from elite_speak.python import defs
import sys


def get_definitions(sentence, exclude):
    parts_of_speech = defs.get_pos(sentence)
    uncommon_words = defs.filter_words(parts_of_speech, exclude)
    return defs.get_definitions(uncommon_words)


def main():
    common_words = defs.get_10000()
    while True:
        # get string from audio input
        # wait until person is done talking
        voice_input = input('>')
        definitions = get_definitions(voice_input, common_words)

        sys.stdout.write('DEF_FLAG' + str(definitions).replace('\'', '\"'))  # print definitions as an event in Node


if __name__ == '__main__':
    main()
