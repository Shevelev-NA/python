def hours_to_days(a, b=24):
    return a//b



# не изменяйте код дальше, это проверка
values = [int(x) for x in input().split(" ")]
print(hours_to_days(*values))