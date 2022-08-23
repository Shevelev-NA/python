numbers = []
letters = []

for number in range(10):
    numbers += str(number)
for letter in range(97,123):
    letters += chr(letter)

# Не удаляйте код ниже: он нужен для проверки.

print("".join(numbers),"".join( letters))

