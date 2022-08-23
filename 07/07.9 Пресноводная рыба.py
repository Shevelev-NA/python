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





for i in fish:
    for key, value  in i.items():
        if value == "fresh":
            fresh_water += {i["specie"]}
        elif value == "sea":
            sea_water += {i["specie"]}

print(f'Морские: {", ".join(sea_water)}')

print(f'Пресноводные: {", ".join(fresh_water)}')
