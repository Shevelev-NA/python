

def  get_grade(grade):
    grades = {2: "Плохо", 3: "Удовлетворительно", 4: "Хорошо", 5: "Отлично"}
    if grade not in ["", " "]:
        i= int(grade)
        if  2<=i<=5 :
            return grades[grade]

# Код вашей функции должен быть выше

try:
    assert get_grade(2) == "Плохо"
    assert get_grade(3) == "Удовлетворительно"
    assert get_grade(4) == "Хорошо"
    assert get_grade(5) == "Отлично"
    assert get_grade("") == "Ошибка"
except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")
else:
    print("Все хорошо, все работает")

