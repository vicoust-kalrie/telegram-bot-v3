import requests

def harga_btc():

    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    data = requests.get(url).json()

    return data["bitcoin"]["usd"]
