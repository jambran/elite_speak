from PyDictionary import PyDictionary
from models import words


def generate_definitions(word_list, lemmatizer):
    """
    Gets dictionary definitions for passed words. Only deals with nouns,
    verbs, adjectives, and adverbs as there aren't really any other types
    with "obscure" lexical items. Uses PyDictionary for lookup
    """
    defs = {}  # dict of words and their definitions (specific to part of speech)
    dictionary = PyDictionary()
    # Just gets the broad POS (i.e. we don't care if its a plural or singular noun)
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
            #Lemmatizes word to (hopefully) have better getting correct POS
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
    """
    Formats the definitions to be handled by a TTS engine
    """
    words = dict(definitions)
    definitions = [word + ": " + words[word]['pos'] + ": " + words[word]['def'] for word in words]
    return definitions
