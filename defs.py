from PyDictionary import PyDictionary
import nltk


def get_10000():
    with open('google-10000-english-usa.txt', 'r') as file:
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
        definitions = dictionary.meaning(word)
        defs[word] = {
            'pos': part,
            'def': definitions[part][0]
        }
    return defs


def format_defs_for_speech(defs):
    # Returns a list of sentences of definitions
    sentences = []
    for word in defs:
        sentences.append('{}, {}, {}.'.format(
            word,
            defs[word]['pos'].lower(),
            defs[word]['def']
        ))
    return sentences


if __name__ == '__main__':
    exclude = get_10000()

    example = input('sentence: ')

    pos = get_pos(example)
    filtered = filter_words(pos, exclude)
    defs = get_definitions(filtered)

    print('\n'.join(format_defs_for_speech(defs)))
