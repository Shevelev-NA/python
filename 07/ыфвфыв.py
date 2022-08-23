address = "123 north anywhere street"

for word, initial in {"NORTH":"N", "SOUTH":"S" }.items():
    address = address.replace(word.lower(), initial)
print(address)

initial