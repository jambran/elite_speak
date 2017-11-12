import pyttsx3
import os


def parse_definitions(definitions):
    words = dict(definitions)
    definitions = []
    for word in words:
        definitions.append(word + ": " + words[word]['pos'] + ": " + words[word]['def'])
    return definitions


def speak_many_things(definitions):
    for string in definitions:
        speak_thing(string)


def speak_thing(definition):
    command = 'say \"' + definition + '\"'
    os.system(command)


def say_definitions(definitions):
    defs = parse_definitions(definitions)
    speak_many_things(defs)
