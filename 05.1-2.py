def get_hashtags(text):

    words = text.split(" ")
    hashtags = []
    for word in words:
        if word[0] == "#":
            hashtags.append(word[1:])
        else:
            pass
    return hashtags


# Не удаляйте код ниже, он нужен для проверки

words = input()
result = get_hashtags(words)
print(result)