import random
import sys
import webbrowser

import speech_recognition as sr
from win32com.client import Dispatch

from brain import make_dataset, vectorazion_x, classificator
from dataset import BOT_CONFIG

corpus, y = make_dataset(config=BOT_CONFIG)
vectorizer, X = vectorazion_x(corpus=corpus)
clf = classificator(X=X, y=y)


def get_intent(question):
    return clf.predict(vectorizer.transform([question]))[0]


def get_answer_by_intent(intent):
    phrases = BOT_CONFIG['intents'][intent]['responses']
    return random.choice(phrases)


def get_failure_phrase():
    phrases = BOT_CONFIG['failure_phrases']
    return random.choice(phrases)


def bot(question):
    intent = get_intent(question)
    if intent:
        return get_answer_by_intent(intent)
    # Ответ-заглушка
    return get_failure_phrase()


def talk(words):
    print(words)
    speak = Dispatch("SAPI.SpVoice").Speak
    speak(words)


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # talk('Говорите')
        print('ready')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source=source, duration=1)
        audio = r.listen(source)

    try:
        question = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали " + str(question))
    except sr.UnknownValueError:
        talk("Я вас не понимаю")
        question = command()

    return question


def makeSomething(question):
    if 'открыть сайт' in question:
        talk("Уже открываю")
        url = "https://itproger.com"
        webbrowser.open(url)
    elif 'стоп' in question:
        talk('Да, конечно, без проблем')
        sys.exit()
    elif 'как тебя зовут' in question:
        talk("Меня зовут Соня")
    else:
        print(bot(question))
        talk(bot(question))



while True:
    makeSomething(command())
