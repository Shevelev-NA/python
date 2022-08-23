fish = [

    {"specie": "Белуга", "water": "fresh"},
    {"specie": "Карась", "water": "fresh"},
    {"specie": "Красноперка", "water": "fresh"},

    {"specie": "Морской окунь", "water": "sea"},
    {"specie": "Тунец", "water": "sea"},
    {"specie": "Скумбрия", "water": "sea"},

]

sea_water = []
fresh_water = []

for one_fish in fish:

    if one_fish["water"] == "sea":
        sea_water.append(one_fish)
    elif one_fish["water"] == "fresh":
        fresh_water.append(one_fish)

print(sea_water, fresh_water)