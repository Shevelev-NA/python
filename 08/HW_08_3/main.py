import json
import random
import requests # предварительно нужно обновить PIP  и потом установить этот модуль

from utils import load_questions

"""Проверяем что это основной файл для запуска скрипта"""
if __name__ == '__main__':

    data = json.loads(requests.get(r"https://jsonkeeper.com/b/5L9C").text)
    questions = load_questions((data)) #передаем JSON файл в функцию
    random.shuffle(questions) #Перемешиваем список вопросов

    count = 0
    score = 0


    for question in questions:
        """проходим циклом по вопросам (экземплярам класса Question)
        И по этому у нас работают все методы данного класса"""
        question.user_answer = input(question).strip().lower()
        print(question.build_feedback())
        if question.is_correct():
            count += 1
            score += question.score

    print("Вот и все!")
    print(f"Отвечено {count} вопросов из {len(questions)}")
    print(f"Набрано баллов: {score}")


