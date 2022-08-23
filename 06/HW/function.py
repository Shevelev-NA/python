from pathlib import *
import re
from collections import *
from random import *


"""Импорт модуля и всех его методов через * ,поэтому не нужно писать в начале pathlib
  сайт https://python-scripts.com/pathlib

  Импорт модуля и всех его методов через * , поэтому не нужно писать в начале collections
   сайт https://pythonworld.ru/moduli/modul-collections.html

  импорт модуля RE  для замены символ в методе RE.SPLIT
   https://evileg.com/ru/post/642/ """


def get_words_list_v1(file):
    """ _______________________Вариант проверки списка через модуль PATHLIB____________________________________"""

    words_list_temp_PT = []  # список где будет формироваться временный перечень слов исправленный в котором могут быть задвоения

    """ Импорт списка слов и установка кодировки для русских букв"""
    words_list = Path(file)
    words = words_list.read_text(encoding='utf-8')

    """для усложнения сделан разделитель через разные варианты положения запятой и пробелов, больших букв
         по пробелу не применялось из за возможных парных слов """
    words_list_temp_PT += re.split(', | , | ,|,', words.lower())

    """для усложнения сделан разделитель через разные варианты положения запятой и пробелов
         по пробелу не применялось из за возможных парных слов """
    words_list_white_PT = Counter(words_list_temp_PT)


    # print(Counter(words_list_temp_PT))

    # напрямую не получилось применить метод LIST к words_list_temp_PT
    # поэтому пришлось ввести промежуточную переменную, чтоб потом к ней применить этот метод

    return list(words_list_white_PT)  # формирование списка уникальных элементов


def get_words_list_v2(files):
    """ _______________________Вариант проверки списка через модуль OS____________________________________"""

    words_list_temp = []  # список где будет формироваться временный перечень слов исправленный в котором могут быть задвоения

    """ Импорт списка слов и установка кодировки для русских букв"""
    with open(files, encoding='utf-8') as file:
        for i in file:
            words_list_temp += re.split(', | , | ,|,', i.lower())
            """для усложнения сделан разделитель через разные варианты положения запятой и пробелов
            по пробелу не применялось из за возможных парных слов
            """
    words_list_white = Counter(words_list_temp)

    # print(Counter(words_list_temp))
    # напрямую не получилось применить метод LIST к words_list_temp_PT
    # поэтому пришлось ввести промежуточную переменную, чтоб потом к ней применить этот метод
    return list(words_list_white)  # формирование списка уникальных элементов

# в домашней работе его не использовал


def get_random_word(list_words):
    """ _______________________Функция по перемешиванию букв в слове.  ПРоверка вводимого слова и создание словаря верных ответов_________________"""
    shuffle(list_words)  # перемешиваю исходный список
    list_words_random = []  # список для перемешанных слов без задвоения

    """ Цикл для перемешивангия исходного списка """
    for i in list_words:
        if i not in list_words_random:
            list_words_random.append(i)
    return  list_words_random

def get_shuffle_word(list_words_random):
    user_answer = {}  # Словарь с ответами верно/неверно + значение слова
    get_coins = 10  # колличество баллов по умолчанию за верный ответ

    for keys, values in enumerate(list_words_random):  # с помощью enumerate возвращаю словарь значение - ключ

        # keys - это просто позиционная переменная КЛЮЧ, она может называться как угодно
        # values - это просто позиционная переменная ЗНАЧЕНИЕ, она может называться как угодно
        """Посмотрел тут https://ru.stackoverflow.com/questions/764627/%D0%9F%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D1%88%D0%B0%D1%82%D1%8C-%D0%B1%D1%83%D0%BA%D0%B2%D1%8B-python"""

        sample_word = "".join(sample((values), len(values)))  # Перемешиваю буквы в каждом слове отдельно т.к. каждое слово это список из букв  и обьединяю обратно перемешанные буквы в слова

        """Выдача вопросов пользователю с перемешанными словами"""
        print(f'  Угадайте слово: {sample_word}')
        user_input = input("Введите слово = ")

        """Проверка ответов пользователя и запись ответов в user_answer как словарь. ПРивязка идет через индекс и значение """
        if user_input == values:
            user_answer[values] = True
            print(f'Верно! Вы получаете {get_coins} очков')
        else:
            user_answer[values] = False
            print(f"Неверно! Верный ответ – {values}.")

    return user_answer



def get_write_history(user_name, results):
    """ _______________________Функция заносит рекорд пользователя в файл history.txt________________"""

    """ _______________________Расчет правильных ответов________________"""
    user_result = 0
    for values in results.values():
        if values == True:
            user_result += 10

    """ _______________________Запись в файл имени и итоговый счет игрока ________________"""
    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(f"{user_name} : {user_result}\n")




def get_read_history(file):
    """ _______________________Функция читает истатистику из файла history.txt и
    определяет максимальное значение и количество игр________________"""
    number_of_records = 0   # Всего игр сыграно
    top_score = 0   # Максимальный рекорд
    # открываем файл для чтения
    with open(file, "r", encoding="utf-8") as files:

        # цикл для перебора строк из файла
        for line in files:
            number_of_records += 1
            score = line.strip().split(' : ')[-1]  # [-1] позволяет вывести в строке первый символ с конца
            score_int = int(score)

            # Определяем максимальное значение рекорда через сравнение
            if score_int > top_score:
                top_score = score_int

        return number_of_records, top_score
        # return {'Всего игр сыграно': number_of_records, 'Максимальный рекорд': top_score}


def get_read_full_history(file):
    """ _______________________Функция читает истатистику из файла history.txt р________________"""
        # открываем файл для чтения
    words_list = Path(file)
    return words_list.read_text(encoding='utf-8')




# _________________ВСЕ ЧТО НИЖЕ ЭТО ПРОСТО ДЛЯ ПРОВЕРКИ РАБОТЫ ФУНКЦИЙ_____________________

# user_name = input('Введите ваше имя : ')
# if user_name == "":
#     user_name = "Jon Dow"


# print(f'\nПровека результата отсортированного списка get_words_list_v1() через модуль PATHLIB - \n{get_words_list_v1("words.txt")}')
# print(f'\nПровека результата отсортированного списка get_words_list_v2() через модуль OS - \n{get_words_list_v2("words.txt")}')

# RW_1 = get_random_word(get_words_list_v1("words.txt"))
# print(f'\nПроверка перемешанного списка list_words_random - \n{RW_1}\n')

# user_result_history = get_shuffle_word(RW_1)
# print(f'\nПроверка словаря с ответами верно/не верно user_answer \n{user_result_history}')

# print(f'\nЗапись ис тории игры в файл history.txt \n{get_write_history(user_name, user_result_history)}')

# print(get_read_history('history.txt'))
