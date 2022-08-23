import json

def load_students(files):
    """ Импортируем файл формата json список студентов students.json """
    with open(files, 'r', encoding="utf-8") as file:
        f_students = json.load(file)
        return f_students

        # вывод для проверки значений (можно отключить)
        # print(f"f_students -> {f_students}")

def load_professions(files):
    """ Импортируем файл формата json список профессий  professions.json """
    with open(files, 'r', encoding="utf-8") as file:
        f_professions = json.load(file)
        return f_professions

        # вывод для проверки значений (можно отключить)
        # print(f"f_professions -> {f_professions}")


def get_student_by_pk(input_pk : int):
    """Получает словарь с данными студента по его pk"""
    for i in list_student:
      if (input_pk) ==  str(i['pk']):
          return i
    return False

def get_print_student_by_pk(student_by_pk):
    """Функция вывода на печать информации о выбранном пользователе """
    if student_by_pk != False:
        print(f'Студент {student_by_pk["full_name"]}')
        print(f'Знает: {", ".join(student_by_pk["skills"])}')
        print(f'\nВыберите специальность для оценки студента {student_by_pk["full_name"]}')
    else:
        print("У нас нет такого студента")


def get_profession_by_title(titles):
     """Получает словарь с инфо о профе по названию """
     for i in list_professions:
        if titles == i['title']:
            return i
     print("У нас нет такой специальности")
     quit()


def get_print_profession_by_title(profession_by_title):
    """Функция вывода на печать информации о выбранном направлении """
    if profession_by_title != False:
        print(f'Направление включает: {", ".join(profession_by_title["skills"])}')
        return profession_by_title

def check_fitness(student, profession):
   """Проверка соответствия знаний студента выбранной профессии"""

   """Делаю из полученных значений множество и применяю метод пересечения"""
   student_know = ', '.join(set(student['skills']).intersection(set(profession['skills'])))
   student_do_not_know = ', '.join(set(profession['skills']).difference(set(student['skills'])))

   """Проверка пригодности выбранной проффесии"""
   len_student_know = len(student_know.split())
   len_student_do_not_know = len(student_do_not_know.split())

   status = int((len_student_know*100)/(len_student_do_not_know+len_student_know))
   print(f'\nПригодность {status}%')

   if status != 0:
       """Полученный результат анализа вывожу на печать"""
       print(f"Студент {student['full_name']} знает {student_know}")  # сделал можество из обьектов
       print(f"Студент {student['full_name']} не знает {student_do_not_know}")  # сделал можество из обьектов
   else:
       print(f"Студент {student['full_name']} ничего не знает")  # сделал можество из обьектов


"""__________ВСЕ ЧТО ВЫШЕ ЭТО ФУНКЦИИ_________"""


""" переменные для загрузки файлов с данными по студентам и профессии"""
list_student = load_students('students.json')
list_professions = load_professions('professions.json')

"""пользовательски ввод данных"""
pk = input(f"Введите номер студента:\n")
get_print_student_by_pk(get_student_by_pk(pk)) # функция вывода на печать инфы по студенту

""" условие для контроля работы программы"""
if get_student_by_pk(pk) != False:
    title = input().title()
    get_print_profession_by_title(get_profession_by_title(title))  # функция вывода на печать инфо по выбранной профессии

    """Проверка соответствия знаний студента выбранной профессии"""

    check_fitness(get_student_by_pk(pk), get_profession_by_title(title))

