from Classes import BasicWord
import random


def load_random_word(link):
    list_base_words = []
    for i in link:
        base_word_correct = i['subwords']
        base_word = i['word']

        """Создаем экземпляр класса BasicWord"""
        list_base_words.append(BasicWord(base_word, base_word_correct))
    return random.choice(list_base_words)
