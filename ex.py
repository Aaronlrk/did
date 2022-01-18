import json
import random
from collections import OrderedDict

file_data=OrderedDict()

order_list = []
name = ['Lucy', 'Aaron', 'Kate', 'Belle', 'Sol']

coffee=['Americano', 'Latte', 'Chocomilk', 'Juice', 'Water']

for i in range(1,21):
    temp = { "name" : random.choice(name),
             "num" : i,
             "coffee" : random.choice(coffee)
        }
    order_list.append(temp)

print(json.dumps(order_list, ensure_ascii=False,indent="\t"))

with open('data.json','w',encoding="utf-8") as make_file:
    json.dump(order_list,make_file,ensure_ascii=False, indent= "\t")