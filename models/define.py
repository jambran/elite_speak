from PyDictionary import PyDictionary


def generate_definitions(words):
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
            if not part or part not in definitions:
                part = list(definitions.keys())[0]
            defs[word] = {
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
