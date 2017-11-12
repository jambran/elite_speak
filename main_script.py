import defs
import textToSpeech


def get_definitions(sentence, exclude):
    parts_of_speech = defs.get_pos(sentence)
    uncommon_words = defs.filter_words(parts_of_speech, exclude)
    return defs.get_definitions(uncommon_words)


def main():
    common_words = defs.get_10000()
    lst = []
    lst_threshold = 10
    while True:
        voice_input = defs.speech_to_text()
        definitions = get_definitions(voice_input, common_words)
        for k in definitions.keys():
            lst.append(k + ": " +  str(definitions[k]))
        if len(lst) > lst_threshold:
            lst = lst[len(lst) - lst_threshold:]
        lst.sort(reverse = True)
        print(lst)
        #print(definitions)
        textToSpeech.say_definitions(definitions)


if __name__ == '__main__':
    main()
