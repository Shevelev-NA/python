# В списке хранится информация о прудах, где живут рыбы. Удалите из списка все пруды, где живут тунцы.

ponds = [
    {"pk": 1, "volume": 10000, "fish": "тунец"},
    {"pk": 192,"volume": 20000, "fish": "морская камбала"},
    {"pk": 206,"volume": 10000, "fish": "треска"},
    {"pk": 322,"volume": 25000, "fish": "тунец"},
    {"pk": 420,"volume": 20000, "fish": "морская камбала"},
    {"pk": 704,"volume": 10000, "fish": "треска"},
    {"pk": 920,"volume": 25000, "fish": "тунец"},
]
for i in ponds:
    if i["fish"] == "тунец":
        i.clear()

print(ponds)

for p in ponds:
    if "pk" in p:
        print(p['pk'])
