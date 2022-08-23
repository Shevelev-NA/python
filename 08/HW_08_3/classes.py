class Question:
    def __init__(self, text, difficulty, right_answer):
        self.text = text
        self.difficulty = difficulty
        self.right_answer = right_answer
        self.user_answer = None
        self.score = 10 * self.difficulty

    def is_correct(self):
        """Проверка на верность ответа пользователя"""
        return self.user_answer == self.right_answer

    def build_feedback(self):
        """Вывод сообщения об ответе пользователя"""
        match self.is_correct():
            case True:
                return f"Ответ верный получено {self.score} баллов"
            case False :
                return f"Ответ не верный, верный ответ {self.right_answer}"

    def __repr__(self):
        """Выводим информация об экземпляре класса (вопросе) в читаемом виде(расшифровка"""
        return (f"Вопрос: {self.text}?\n" \
                f"Сложность {self.difficulty}/5 ")