import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()


def speech_to_text():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak now...")

        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text

    except:
        return "Could not understand audio"



def text_to_speech(text):

    engine.say(text)
    engine.runAndWait()