# Пользователи для добавления
a = ['Киселёв / Всеволод / Эдуардович / 342 020 / 14 ноября 2001 года / +7 (908) 161-64-28 / главный инженер',
'Довлатова / Эмилия / Ефимовна / 342 000 / 18 мая 2001 года / +7 (924) 588-50-15 / технолог',
'Аверин / Мартын / Егорович / 217 340 / 12 февраля 1981 года / +7 (933) 768-22-15 / технолог',
'Князева / Августа / Егоровна / 320 021 / 2 июля 1984 года / +7 (965) 886-27-01 / расфасовщик',
'Шанская / Аграфена / Семёновна / 116 404 / 7 июля 1982 года / +7 (954) 940-47-96 / психолог для рыб']

# print(a[0].split(' / '))  # просто для проверки работы индеса по списку а
# print(len(a))  #если так смотреть список длиной 5

employees = {
"": {"f": "", "i": "", "o": "", "pass": "", "birthday": "","phone": "", "position": ""}
}

""" превращаем определенную строчку в список слов"""
def user_list(index):
    return a[index].split(' / ') # из за ображения по индексу строки  список стал длиной 4 (0,1,2,3,4)

"""получаем определенное слова из строчки выбранной"""

def user_list_index(first, second):  # first атрибут для определения строчки 0-4 , second для определения фрагмента данной строчки
    return user_list(first)[second]

new_dic = {}

def gg(index2):
    """Обращаемся к словарю для получения его ключей и привязки ключа к значению слова из а"""

    i = -1
    # u = 0
    for value in employees.values():
        for key1, value1 in value.items():
            i+=1 # счетчик слов в предложении а

            new_dic[user_list(index2)[0]] = value # копирую в новый словарь полученные данные из списка а + ключи

            value[key1] = user_list(index2)[i]
            print(key1, value[key1]) # вывод текста как в задании

        print("-")

for i in range(len(a)):
    gg(i)  # перебор строк из списка а по длинне списка

print(new_dic)





