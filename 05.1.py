text = "The quick brown fox jumps over the lazy dog"

def text_length(): #вернет количество символов без пробелов,
    return int(len(text)) - int(text.count(" "))

def text_length_full(): #вернет количество символов c пробелами,
    return len(text)

def text_word_count():
    return int(text.count(" "))+1 #вернет количество слов (количество пробелов + 1).


# Не удаляйте код ниже, он нужен для вызова и тестирования функции

print(text_length())
print(text_length_full())
print(text_word_count())