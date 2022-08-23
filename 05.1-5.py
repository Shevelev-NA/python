def remove_from_string(string, *symbols_to_remove):

  for symbol in symbols_to_remove:
    string = string.replace(symbol,"")
  return string

print(remove_from_string("О! Смотри, можно удалить все знаки препинания сразу?", "?", "!", ",", ".", "–"))


