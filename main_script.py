import defs
import textToSpeech
from pickle import dump
from pickle import load


def get_definitions(sentence, exclude):
    parts_of_speech = defs.get_pos(sentence)
    uncommon_words = defs.filter_words(parts_of_speech, exclude)
    return defs.get_definitions(uncommon_words)


def main():
    common_words = defs.get_common_words()
    try:
        input = open("pickle_jar.pkl", 'rb')
        my_words = load(input)
        input.close()
        print(my_words)
    except FileNotFoundError:
        my_words = {}
    lst = []
    lst_threshold = 10
    done = False
    while not done:
        voice_input = defs.speech_to_text()
        if "conversation over" not in voice_input.lower():
            definitions = get_definitions(voice_input, common_words)
            for k in definitions.keys():
                try:
                    my_words[k] = (my_words[k][0] + 1, my_words[k][1])
                    print(k + str(my_words[k]))
                except KeyError:
                    my_words[k] = (1, str(definitions[k]))
            definitions = textToSpeech.parse_definitions(definitions)
            lst[::-1]
            lst.extend(definitions)
            if len(lst) > lst_threshold:
              lst = lst[len(list) - lst_threshold:]
            lst[::-1]
            print(my_words)
            textToSpeech.speak_many_things(definitions)
        else:
            done = True
    # pickle my_words
    output = open("pickle_jar.pkl", 'wb')
    dump(my_words, output, -1)
    output.close()
    return lst


if __name__ == '__main__':
    main()
