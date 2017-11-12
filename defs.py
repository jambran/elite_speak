from PyDictionary import PyDictionary
import nltk
import speech_recognition as sr


def get_10000():
    with open('docs/google-10000-english-usa.txt', 'r') as file:
        words = file.readlines()
    return set([w.strip() for w in words])


def get_pos(sentence):
    words_list = nltk.word_tokenize(sentence)
    return nltk.pos_tag(words_list)


def filter_words(l, w):
    # Returns list of words not in set w
    return [p for p in l if p[0] not in w]


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
            if part in definitions:
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
        audio = r.listen(source)
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
    exclude = get_10000()

    example = speech_to_text()
    print(example)
    pos = get_pos(example)
    filtered = filter_words(pos, exclude)
    defs = get_definitions(filtered)

    print(defs)
