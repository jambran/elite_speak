from PyDictionary import PyDictionary
import nltk
import speech_recognition as sr


def get_common_words():
    with open('docs/wiki-100k.txt', 'r') as file:
        words = file.readlines()
    return {w.lower().strip():True for w in words if not w.strip()[0] == '#'}


def get_pos(sentence):
    words_list = nltk.word_tokenize(sentence)
    new_list = []
    for i in range(len(words_list)-1):
        if '\'' not in words_list[i] and 'n\'t' not in words_list[i+1]:
            new_list.append(words_list[i])
    if len(new_list) > 0 and '\'' not in words_list[-1]:
        new_list.append(words_list[-1])
    print(new_list)
    return nltk.pos_tag(new_list)


def filter_words(words, common_words):
    # Returns list of words not in set w
    return [w for w in words if w[0] not in common_words]


def get_definitions(words):
    defs = {}  # dict of words and their definitions (specific to part of speech)
    dictionary = PyDictionary()
    for word, pos in words:
        if pos.startswith('NN'):  # Noun
            part = 'Noun'
        elif pos.startswith('VB'):  # Verb
            part = 'Verb'
        elif pos.startswith('JJ'):  # Adjective
            part = 'Adjective'
        elif pos.startswith('RB'):  # Adverb
            part = 'Adverb'
        else:
            continue
        try:
            definitions = dictionary.meaning(word)
            # given that POS_Tagger tags words, if the POS is not found for that word, grabs the first ("default") one
            if part not in definitions:
                part = list(definitions.keys())[0]
            defs[word] = {
                    'pos': part,
                    'def': definitions[part][0]
                }
                
        except TypeError:
            continue
    return defs


def speech_to_text():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source, duration=1)
        r.dynamic_energy_threshold = True
        audio = r.listen(source)
        print("Done!")
    input = ""
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        input = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return input
  
  
# MOVED TO NODE
# def format_defs_for_speech(defs):
#     # Returns a list of sentences of definitions
#     sentences = []
#     for word in defs:
#         sentences.append('{}, {}, {}.'.format(
#             word,
#             defs[word]['pos'].lower(),
#             defs[word]['def']
#         ))
#     return sentences


if __name__ == '__main__':
    exclude = get_common_words()

    example = speech_to_text()
    print(example)
    pos = get_pos(example)
    filtered = filter_words(pos, exclude)
    print(pos)
    defs = get_definitions(filtered)
    print(defs)
