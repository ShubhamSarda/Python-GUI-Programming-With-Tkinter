import requests 
import json

api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=3889ce63-c733-403d-8b7d-c41a2438b4ea")
api = json.loads(api_request.content)

print("----------------")
print("----------------")

coins = [
  {
    "symbol":"BTC",
    "amount_owned": 2,
    "price_per_coin": 3200
  }, 
  {
    "symbol":"EOS",
    "amount_owned": 100,
    "price_per_coin": 2.05
  }
]

total_pl = 0

for i in range(0, 5):
  for coin in coins:
    if api["data"][i]["symbol"] == coin["symbol"]:
      total_paid = coin["amount_owned"] * coin["price_per_coin"]
      current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
      pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
      total_pl_coin = pl_percoin * coin["amount_owned"]
      
      total_pl = total_pl + total_pl_coin

      print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
      print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
      print("Number Of Coin:", coin["amount_owned"])
      print("Total Amount Paid:", "${0:.2f}".format(total_paid))
      print("Current Value:", "${0:.2f}".format(current_value))
      print("P/L Per Coin:", "${0:.2f}".format(pl_percoin))
      print("Total P/L With Coin:", "${0:.2f}".format(total_pl_coin))
      print("----------------")

print("Total P/L For Portfolio:", "${0:.2f}".format(total_pl))
