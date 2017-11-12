import defs
import textToSpeech


def get_definitions(sentence, exclude):
    parts_of_speech = defs.get_pos(sentence)
    uncommon_words = defs.filter_words(parts_of_speech, exclude)
    return defs.get_definitions(uncommon_words)


def main():
    common_words = defs.get_10000()
    listDefs = []
    done = False
    while not done:
        voice_input = defs.speech_to_text()
        print(voice_input)
        if "conversation over" not in voice_input.lower():
            definitions = get_definitions(voice_input, common_words)
            definitions = textToSpeech.parse_definitions(definitions)
            listDefs.extend(definitions)
            textToSpeech.speak_many_things(definitions)
        else:
            done = True
    return listDefs


if __name__ == '__main__':
    main()
