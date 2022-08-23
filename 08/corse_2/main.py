import json
import requests

from utils import load_random_word
from Player import Player

"""Код ниже будет выполняться только если файл main"""
if __name__ == '__main__':

    """Загрузка слов из внешнего источника"""
    req = json.loads(requests.get(r'https://jsonkeeper.com/b/ZIBP').text)

    """передаем список слов JSON в функцию для получения объектов класса BasicWord"""
    """Получаем случайный элемент последовательности"""
    words = load_random_word(req)
    words.get_print()

    """имя пользователя"""
    player = Player(input('В введите имя игрока\n'))

    """Поздоровайтесь с пользователем."""
    player.hello_player(words.check_len_words(), words.base_word)

    """Цикл по угадыванию слов"""
    i = 0

    while i < words.check_len_words():
        """ Ввод ответа пользователя"""
        words.input_answer = input("Введите слово - ").lower().strip()
        if words.input_answer != "стоп":
            if words.len_user_input_answer() < 3:
                print("слишком короткое слово")
            elif words.check_input_words() is not True:
                print("неверно")
            elif player.cheсk_using_words(words.input_answer) is True:
                print("уже использовано")
            else:
                player.add_user_words(words.input_answer)
                i += 1
        else:
            break
    print(f"Игра завершена, вы угадали {player.count_words()} из {words.check_len_words()} слов!")
