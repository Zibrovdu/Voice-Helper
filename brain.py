from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import random


def make_dataset(config):
    dataset = []  # [[example1, intent1], [example2, intent2], ...]

    for intent, intent_value in config['intents'].items():
        for example in intent_value['examples']:
            dataset.append([example, intent])

    corpus = [example for example, intent in dataset]
    y = [intent for example, intent in dataset]

    return corpus, y


def vectorazion_x(corpus):
    vectorizer = CountVectorizer()
    x = vectorizer.fit_transform(corpus)
    return vectorizer, x


def classificator(X, y):
    clf = LogisticRegression()
    clf.fit(X, y)
    return clf


