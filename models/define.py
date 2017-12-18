from PyDictionary import PyDictionary
from models import words


def generate_definitions(word_list, lemmatizer):
    defs = {}  # dict of words and their definitions (specific to part of speech)
    dictionary = PyDictionary()
    for word, pos in word_list:
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
            lemmatized_word = words.lemmatize(word, lemmatizer)
            definitions = dictionary.meaning(lemmatized_word)
            # given that POS_Tagger tags words, if the POS is not found for that word, grabs the first ("default") one
            if not part or part not in definitions:
                part = list(definitions.keys())[0]
            defs[lemmatized_word] = {
                'pos': part,
                'def': definitions[part][0]
            }

        except TypeError:
            continue
    return defs


def parse_speakable_definitions(definitions):
    words = dict(definitions)
    definitions = [word + ": " + words[word]['pos'] + ": " + words[word]['def'] for word in words]
    return definitions
