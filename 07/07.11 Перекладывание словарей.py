# Наш формат:
#
# {"count": 5, "specie": "Тунец" , "avg_size": 30 }

order = [
 {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
 {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
 {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = {}


for i in order:

    order_converted['count'] = int(i["skolko"])
    order_converted['specie'] = i["poroda"].title()
    order_converted['avg_size'] = int((i["sred_razmer"])*0.1)

    for k, c in order_converted.items():
        print(k, c)
#
