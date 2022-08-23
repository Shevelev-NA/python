from random import *
k= ['123456','1234','abcde']
g=[] #список для перемешанных слов без задвоения
user_answer = {} # Словарь с ответами верно/неверно + значение слова
shuffle(k) # перемешиваю исходный список
get_coins = 10 # колличество баллов по умолчанию за верный ответ
""" Цикл для перемешивангия исходного списка """
for i in k:
    if i not in g:
        g.append(i)
print(g) # проверка перемешанного списка
"""Посмотрел тут https://ru.stackoverflow.com/questions/764627/%D0%9F%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D1%88%D0%B0%D1%82%D1%8C-%D0%B1%D1%83%D0%BA%D0%B2%D1%8B-python"""

for keys, values in enumerate(map(list, g)): # с помощью map возвращаю список слова по буквам
    shuffle(values) # Перемешиваю буквы в каждом слове отдельно т.к. каждое слово это список из букв
    values[keys] = "".join(values) # обьединяю обратно перемешанные буквы в слова.

    """Выдача вопросов пользователю с перемешанными словами """
    print(f'Угадайте слово: {values[keys]}')
    user_input = input("Введите слово = ")

    if user_input == g[keys]:
        user_answer[values[keys]] = True
        print(f'Верно! Вы получаете {get_coins} очков')
    else:
        user_answer[values[keys]] = False
        print(f"Неверно! Верный ответ – {g[keys]}.")

print(user_answer) # Проверка словаря с ответами верно/не верно







