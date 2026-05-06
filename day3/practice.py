from rich import print
import json

with open("keyword-pizza-swiggy.json","r",encoding="utf-8") as f:
    data=json.load(f)

    cards=data['data']['cards'][1]['groupedCard']['cardGroupMap']['cardGroupMap']['DISH']['cards']

    pizza_name=[]

    for i in range(1,len(cards)):
        pizza_name.append(cards[i]['card'])