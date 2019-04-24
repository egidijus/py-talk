#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, timeout=10, phrase_time_limit=10)
        # Speech recognition using Google Speech Recognition
        data = ""
        try:
            # Uses the default API key
            # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            data = r.recognize_google(audio)
            print("You said: " + data)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}"
                .format(e))

    return data


def jarvis(data):
    print("you said:" + data)

    if "how are you" in data:
        speak("I am fine")

    elif "what time is it" in data:
        speak(ctime())

    elif "where is" in data:
        data = data.replace("where is ", "")
        speak("Hold on Giddy, I will show you where " + data + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" +
                  data.replace(" ", "+") + "/&amp;")

    else:
        speak("I'm sorry i don't understand")


# initialization
time.sleep(2)
speak("Hi Giddy, what can I do for you?")
data = recordAudio()
jarvis(data)
