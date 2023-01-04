import speech_recognition as sr
import os
import sys
import webbrowser
from win32com.client import Dispatch


def talk(words):
    print(words)
    speak = Dispatch("SAPI.SpVoice").Speak
    speak(words)


talk("Привет, спроси у меня что-либо")


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        talk('Говорите')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source=source, duration=1)
        audio = r.listen(source)

    try:
        zadanie = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали " + str(zadanie))
    except sr.UnknownValueError:
        talk("Я вас не понимаю")
        zadanie = command()

    return zadanie


def makeSomething(zadanie):
    if 'открыть сайт' in zadanie:
        talk("Уже открываю")
        url = "https://itproger.com"
        webbrowser.open(url)
    elif 'стоп' in zadanie:
        talk('Да, конечно, без проблем')
        sys.exit()
    elif 'как тебя зовут' in zadanie:
        talk("Меня зовут Соня")


while True:
    makeSomething(command())
