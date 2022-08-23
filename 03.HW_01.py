
#Создайте два списка  с вопросами и ответами.

questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

print('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!')
counts = 0
user_input = input()


if user_input == "ready":
    for i in range(len(questions)):
        print(questions[i])
        user_answer = input("Ваш ответ - ")
        if user_answer == answers[i]:
            counts +=1
            print("Ответ верный!")
        else:
            counts +=0
            print(f"Неправильно. Правильный ответ: {answers[i]}")
else:
    print("Кажется, вы не хотите играть. Очень жаль.")

print(f"Вот и все! Вы ответили на {counts} вопросов из {len(questions)} верно, это {round(100 * counts / (len(questions)))} процентов.")

