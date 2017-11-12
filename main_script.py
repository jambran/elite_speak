from elite_speak import defs
import sys


def get_definitions(sentence, exclude):
    parts_of_speech = defs.get_pos(sentence)
    uncommon_words = defs.filter_words(parts_of_speech, exclude)
    return defs.get_definitions(uncommon_words)


def main():
    common_words = defs.get_10000()
    while True:
        voice_input = defs.speech_to_text()
        definitions = get_definitions(voice_input, common_words)
        # print definitions to create event in Node
        sys.stdout.write('DEF_FLAG' + str(definitions).replace('\'', '\"'))


if __name__ == '__main__':
    main()
