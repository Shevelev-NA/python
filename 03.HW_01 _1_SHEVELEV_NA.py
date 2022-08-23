
#Создайте два списка  с вопросами и ответами.

questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

print('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!')
counts = 0
hit = 0
user_input = input()


if user_input == "ready":
    for i in range(len(questions)):             #создание цикла для получения индекса вопроса и ответа
        print(questions[i])                     #вывод вопроса по индексу списка, заданного черец цикл, по длинне списка
        user_answer = input("Ваш ответ - ")
        if user_answer == answers[i]:
            counts +=1
            hit +=3
            print("Ответ верный!")
        else:

#СОЗДАЕМ ЦИКЛ ПО ПОПЫТКАМ
            for k in range(2,0,-1):
                if k > 0:
                    user_answer = input(f"Осталось попыток: {k}, попробуйте еще раз! \nВаш ответ - ")
                    if user_answer == answers[i]:
                        counts += 1
                        hit += k
                        print("Ответ верный!")
                        break
                else :
                    print(f"Увы, но нет. Верный ответ: {answers[i]}")
    print(f"Вот и все! Вы ответили на {counts} вопросов из {len(questions)} верно, вы набрали {hit} баллов.")

else:
    print("Кажется, вы не хотите играть. Очень жаль.")


