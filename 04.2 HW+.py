words_easy = {
    "family":"семья",
    "hand": "рука",
    "people":"люди",
    "exercise":"упражнение",
    "suggest": "предлагать",
    "except":"кроме",
    "evening": "вечер",
    "minute":"минута",
}

words_medium = {
    "believe":"верить",
    "feel": "чувствовать",
    "make":"делать",
    "open": "открывать",
    "think":"думать",
}

words_hard = {
    "rural":"деревенский",
    "fortune": "удача",
    "exercise":"упражнение",
    "suggest": "предлагать",
    "except":"кроме",
}

levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}
k=0
#Получите у пользователя уровень сложности.
skill = ["легкий", "средний", "сложный"]
answers = {} #будут храниться правильные и неправильные слова
words = {} # положите в него один из словарей в зависимости от выбранной сложности.
x = str(input("Выберите уровень сложности - "  )).lower()


if x in skill:
    if x == skill[0]:
        words = words_easy
    elif x == skill[1]:
        words = words_medium
    elif x == skill[2]:
        words = words_hard
else:
    exit()

print(f'Выбран уровень сложности, мы предложим {len(words)} слов, подберите перевод')

for i, v in words.items():
    print(f'{i}, {len(v)} букв, начинается на {v[0]}\n')
    user_answers = str(input('Введите ответ - '))

    if user_answers ==  v:               # если правильные слова
        print(f'Верно, {i.title()} — это {v}.\n')
        answers[i] = True                       # индекс для вывода правильных слов+добавление в список
        k+=1                                    #счетчик верных слов для опредления ранга

    else:                                  # если не правильные слова
        print(f'Неверно, {i.title()} — это {v}.\n')
        answers[i] = False                  # индекс для вывода не правильных слов +добавление в список

if True in answers.values(): # проверка наличие верно отвеченных слов
    print(f'Правильно отвечены слова:')
    [print(i) for i,v in answers.items() if answers[i] is True]

       #   .items метод чоб делать цикл по ключу и значению ключа
print(f'\nНеправильно отвечены слова:')
[print(i) for i,v in answers.items() if answers[i] is False]

#определение ранга пользователя
print(f'\nВаш ранг:\n{levels[k]}')
