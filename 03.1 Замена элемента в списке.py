#Замените часть слов так, чтобы
# получились корректные числительные
# женского рода (одна, две, три и т. д.).



numbers = ["нула", "една", "две", "три", "четири", "пет", "шест"]

number_change = ["ноль","одна","две","три","четыре","пять","шесть"]

for i in range(len(numbers)):
    numbers[i] = number_change[i]
    print(numbers[i])