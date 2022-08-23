from Classes import BasicWord


class Player(BasicWord):
    def __init__(self, name):
        self.name_user = name  # имя пользователя
        self.user_words = []  # использованные слова пользователя

    """получение количества использованных слов"""
    def count_words(self):
        return len(self.user_words)

    """проверка использования данного слова до этого"""
    def cheсk_using_words(self, user_input_words):
        return user_input_words in self.user_words

    """добавление слова в использованные слова"""
    def add_user_words(self, user_input_words):
        self.user_words.append(user_input_words)

    """Приветствие пользователя"""
    def hello_player(self, count_words, base_word):
        print(f'Привет, {self.name_user}!\n'
              f'Составьте {count_words} слов из слова {base_word}. \n'
              f'Слова должны быть не короче 3 букв.\n'
              f'Чтобы закончить игру, угадайте все слова или напишите "стоп" \n'
              f'Поехали, ваше первое слово?')

    def __repr__(self):
        return self.name_user, self.user_words

    def __str__(self):
        return self.name_user
