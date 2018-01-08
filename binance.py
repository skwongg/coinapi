import requests
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

API_KEY=os.environ.get("BINAN_API_KEY")
SECRET_KEY=os.environ.get("BINAN_SECRET_KEY")
BASE_URL = "https://www.binance.com/api/v1"

def check_heartbeat():
    r = requests.get("{0}/ping".format(BASE_URL))
    if r.status_code:
        return True
    else:
        raise


def get_all_coins():
    r = requests.get(BASE_URL + "/ticker/allPrices")
    all_coins = r.json()
    for coin in all_coins:
        print(coin['symbol'], coin['price'])
    return all_coins, len(all_coins)

get_all_coins()
