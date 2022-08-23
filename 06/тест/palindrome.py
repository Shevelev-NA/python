
def is_palindrome(word):
    x = word.lower()
    reversed_str = x[::-1]
    if x == reversed_str:
        return True

try:
    # assert is_palindrome("level") == True
    assert is_palindrome("sagas") == True
    # assert is_palindrome("hero") == False
    # assert is_palindrome("drama") == False

except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")

else:
    print("Все хорошо, все работает")

