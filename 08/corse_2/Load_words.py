import json
import requests  # импорт функции

"""Проверяем что это основной файл для запуска скрипта"""
if __name__ == '__main__':
    data = json.loads(requests.get(r"https://jsonkeeper.com/b/5L9C").text)
    questions = load_questions((data))  # передаем JSON файл в функцию
    random.shuffle(questions)  # Перемешиваем список вопросов
