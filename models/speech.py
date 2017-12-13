import os
import speech_recognition as sr
from models import define


def say_many(definitions):
    for string in definitions:
        say(string)


def say(definition):
    command = 'say \"' + definition + '\"'
    os.system(command)


def say_definitions(definitions):
    defs = define.parse_speakable_definitions(definitions)
    say_many(defs)


def listen():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source, duration=1)
        r.dynamic_energy_threshold = True
        audio = r.listen(source)
        print("Done!")
    heard = ""
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        heard = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return heard
