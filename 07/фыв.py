От
Оскар
Агзигитов
всем
0
8: 37
PM
encoding = 'utf-8'
обязательно
прописывать?
Спасибо
От
меня
всем
0
8: 43
PM
+
тоже
не
понял
От
Анастасия
Марочкина
всем
0
8: 49
PM
https: // pyneng.readthedocs.io / ru / latest / book / 11
_modules / if_name_main.html
От
Валентин
всем
0
8: 50
PM
Спасибо!
От
Serafim
Serbinovich
всем
0
8: 50
PM
Спасибо))
От
Serafim
Serbinovich
всем
0
9: 02
PM
NonType))
Простите
за
духоту)))
От
Дмитрий
Пестич
всем
0
9: 07
PM
мне
кажется
в
round
надо
обернуть
всю
строку, или
указать
количество
знаков
после
запятой, а
то
выводит
0
0
был
От
меня
всем
0
9: 0
8
PM
lf
От
меня
всем
0
9: 13
PM
У
меня
вопрос
как
добавить
все
строчки
в
словарь, а
не
только
1
в
функции
gg()
я
вношу
индекс
из(а)
от
1 - 4
и
у
меня
все
добавляется
в
словарь, но
переписывается
предыдущее
значение.
    словарь
в
переменной
а
ой
словарь
employees
geyrn
7
пункт
7
От
Михаил
всем
0
9: 13
PM
Вопрос
есть
по
кортежам
и
функциям
От
меня
всем
0
9: 15
PM
да
запусти
да
От
Михаил
всем
0
9: 17
PM
Так
а
там
же
задание
выполняется
просто
вбивая
руками
данные
в
словарь, нет?
От
меня
всем
0
9: 18
PM
давай
От
Дмитрий
Мартынюк
всем
0
9: 18
PM
employees = {}
a0 = 'Киселёв / Всеволод / Эдуардович / 342 020 / 14 ноября 2001 года / +7 (908) 161-64-28 / главный инженер'.split(
    ' / ')
a1 = 'Довлатова / Эмилия / Ефимовна / 342 000 / 18 мая 2001 года / +7 (924) 588-50-15 / технолог'.split(' / ')
a2 = 'Аверин / Мартын / Егорович / 217 340 / 12 февраля 1981 года / +7 (933) 768-22-15 / технолог'.split(' / ')
a3 = 'Князева / Августа / Егоровна / 320 021 / 2 июля 1984 года / +7 (965) 886-27-01 / расфасовщик'.split(' / ')
a4 = 'Шанская / Аграфена / Семёновна / 116 404 / 7 июля 1982 года / +7 (954) 940-47-96 / психолог для рыб'.split(' / ')

a = [a0, a1, a2, a3, a4]

for j in a:
    b = {}
b['f'] = j[0]
b['i'] = j[1]
b['o'] = j[2]
b['pass'] = j[3]
b['birthday'] = j[4]
b['phone'] = j[5]
b['position'] = j[6]
employees[j[0]] = b

# Не удаляйте код ниже, он важен для проверки!

for employee in employees.values():
    for
key, value in employee.items():
print(key, value)
print("-")
