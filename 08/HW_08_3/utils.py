from classes import Question

def load_questions(json_questions):
    """загружаем список вопросов из json файла(ссылки) и соотносим его с классом Question"""
    questions = []
    for item in json_questions:
        text = item["q"]
        difficulty = int(item["d"])
        right_answer = item["a"]

        """ Каждый вопрос это новый экземпляр класса Question"""
        questions.append(Question(text, difficulty, right_answer))
    return questions

