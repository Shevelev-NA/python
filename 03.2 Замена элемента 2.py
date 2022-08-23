managers = ["Алексей", "Денис", "Юля", "Руслан",  "Алексей", "Денис", "Юля"]

name_old = "Денис"
name_new = "Татьяна"

for index, item in enumerate(managers):
    if item == name_old:
        managers[index] = name_new
[print(manager) for manager in managers]



