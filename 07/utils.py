import json

""" Импортируем файл формата json список студентов"""
with open("students.json", encoding="utf-8") as file:
    f_students = json.load(file)
    # вывод для проверки значений (можно отключить)
    print(f"f_students -> {f_students}")

""" Импортируем файл формата json список профессий"""
with open("professions.json", encoding="utf-8") as file:
    f_professions = json.load(file)
    # вывод для проверки значений (можно отключить)
    print(f"f_professions -> {f_professions}")


