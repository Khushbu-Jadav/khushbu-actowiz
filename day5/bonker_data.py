# task link : https://actowizsolutions41121.slack.com/archives/C0B0N7ENNC9/p1777872610987929

import json
from rich.traceback import install
from rich import print

install()

new_bonker_data = []

with open('bonker.json', 'r') as f:
  # load json file
  old_data = json.load(f)


  for product in old_data['products']:
    # store updated data into 'new_bonker_data' list
    new_bonker_data.append(
      {
        "productName": product['variants'][0]['name'].split("-")[0].strip(),
        "vendor": product['vendor'],
        "productUrl": "https://www.bonkerscorner.com/products/" + product['variants'][0]['name'].split('-')[0].strip().replace(" ", "-"),
        "productPrice": float(product['variants'][0]['price']/100),
        "variantCount": len(product['variants']),
        "variantOptions": [{
          "optionName": "Size",
          "optionValues":[size['name'].split('-')[1].strip() for size in product['variants']]
          }],
        "variants": [ 
          {
              "variantName": product['variants'][i]['name'].split("-")[1].strip(),
              "variantId": product['variants'][i]['id'],
              "variantUrl": "https://www.bonkerscorner.com/products/" + product['variants'][0]['name'].split('-')[0].strip().replace(" ", "-") + "?variant=" + str(product['variants'][i]['id']),
              "variantPrice": float(product['variants'][i]['price'] / 100)
          } for i in range(len(product['variants']))],
      }
    )

print(new_bonker_data)

with open("new_bonker_data.json", "w", encoding="utf-8") as f:
  # create updated data json file
  json.dump(new_bonker_data, f, indent=4)