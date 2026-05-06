# task link : [https://actowizsolutions41121.slack.com/archives/C0B0N7ENNC9/p1777538761406169,
#               https://actowizsolutions41121.slack.com/archives/C0B0N7ENNC9/p1777546378085179]

# have attached a "Item Listing" JSON from SIWGGY for keyword PIZZA
# your task is to create a list of "item name"
# https://www.swiggy.com/search?query=Pizza

# example list ["pizza1", "pizza2"....]

# Now we are required to collect the restaurant name as well
# so, we are going to change the structure,
# we will extract data in Key value pairs
# {
# "restaurantName: "myRestaurant",
# "itemName": "myItem"
# }
# And then we will save these dictionaries in  a list

# as we saved the name

import json
from rich import print

with open('keyword-pizza-swiggy.json', "r", encoding='utf-8') as f:
  # load json file
  data = json.load(f)

  # get cards list path
  cards = data['data']['cards'][1]['groupedCard']['cardGroupMap']['DISH']['cards']
  pizzas = []
  restaurent = []
  image_url = []
  price = []
  final_price = []
  isVag = []
  ratings = []
  rating_count = []
  offers = []
  restaurent_address = []
  restaurent_locality = []
  restaurent_avg_rating = []
  restaurent_dil_time = []
  restaurent_min_dil_time = []
  restaurent_max_dil_time = []
  # run loop for getting all the data from the cards list and store into list
  for i in range(1, len(cards)):
    pizzas.append(cards[i]['card']['card']['info']['name'])
    restaurent.append(cards[i]['card']['card']['restaurant']['info']['name'])
    image_url.append(cards[i]['card']['card']['info'].get('imageId', ''))
    price.append(cards[i]['card']['card']['info']['price'])
    final_price.append(cards[i]['card']['card']['info'].get('finalPrice', 0))
    isVag.append(cards[i]['card']['card']['info'].get('isVag',0))
    ratings.append(cards[i]['card']['card']['info']['ratings']['aggregatedRating'].get('rating', 0))
    rating_count.append(cards[i]['card']['card']['info']['ratings']['aggregatedRating'].get('ratingCount', 0))
    offers.append(cards[i]['card']['card']['info'].get('offerTags', {"title": "no offer available"}))
    restaurent_address.append(cards[i]['card']['card']['restaurant']['info']['address'])
    restaurent_locality.append(cards[i]['card']['card']['restaurant']['info'].get('locality',''))
    restaurent_avg_rating.append(cards[i]['card']['card']['restaurant']['info']['avgRating'])
    restaurent_dil_time.append(cards[i]['card']['card']['restaurant']['info']['sla'].get('deliveryTime', None))
    restaurent_min_dil_time.append(cards[i]['card']['card']['restaurant']['info']['sla'].get('minDeliveryTime', None))
    restaurent_max_dil_time.append(cards[i]['card']['card']['restaurant']['info']['sla'].get('maxDeliveryTime', None))

restaurent_with_pizza = []

for i in range(len(pizzas)):
  # append all the data key, value pairs into new list
  restaurent_with_pizza.append({
    "restaurentname": restaurent[i],
    "itemname": pizzas[i],
    "image_url": "https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_208,h_208,c_fit/" + image_url[i],
    "price": float(price[i] / 100),
    "final_price": float(final_price[i] / 100 if final_price[i] > 0.0 else float(price[i] / 100)),
    "discount": float(float(price[i] / 100) - float(final_price[i] / 100)) if final_price[i] > 0.0 else float(0),
    "isVag": bool(final_price[i]),
    "ratings": float(ratings[i]),
    #"offer": offers.get('title', 'No offer available') for offer in offers[i],
    "offers":offers[i],
    "rating_count": rating_count[i],
    "restaurent_address": restaurent_address[i],
    "restuarent_url": "https://www.google.com/maps/search/" + restaurent[i] + restaurent_address[i],
    "restaurent_locality": restaurent_locality[i],
    "restaurent_avg_rating": restaurent_avg_rating[i],
    "restaurent_dilivery_time": restaurent_dil_time[i],
    "restaurent_minimum_dilivery_time": restaurent_min_dil_time[i],
    "restaurent_maximum_dilivery_time": restaurent_max_dil_time[i],
  })

print(restaurent_with_pizza)

with open('swiggy_data.json', 'w', encoding='utf-8') as f:
  # create new json file and store all the data
  json.dump(restaurent_with_pizza, f, indent=4)