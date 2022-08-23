class BasicWord:
    """Клас BasicWord - в нем исходное слово и набор допустимых слов"""

    def __init__(self, base_word=None, base_word_correct=None, user_input_answer=None):
        self.base_word = base_word  # исходное слово
        self.base_word_correct = base_word_correct  # набор допустимых подслов.
        self.input_answer = user_input_answer

    """проверка введенного слова в списке допустимых подслов (вернет bool)"""

    def check_input_words(self):
        return self.input_answer in self.base_word_correct

    """ подсчет количества подслов"""

    def check_len_words(self):
        len_words = self.base_word_correct
        return len(len_words)

    def get_print(self, ):
        print(f'{self.base_word}:{self.base_word_correct}')

    def len_user_input_answer(self):
        return len(self.input_answer)

    def __repr__(self):
        return self.base_word, self.base_word_correct, self.input_answer

    def __str__(self):
        return self.base_word


"""Далее указаны методы для самоконтроля"""
print(BasicWord.__doc__)  # Можно посмотреть описание класса
