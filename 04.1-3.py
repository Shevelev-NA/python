text = "734 122 мне 877 119 022 кажется 127 0 0 1 за 192 168 нами 255 255 следят 32 32 2 5"
just_words = []
t = []

k = text.split(" ")

for i in k:
    if i.isdigit() is True:
        t.append(i)
    else:
        just_words.append(i)
print(t)
print(just_words)
print(" ".join(just_words))











