import requests
import time

from models.crypto import Crypto
from services.crypto_service import CryptoService



def catch_volume_and_currentprice():
    try:
        URL_VARIATION_BINANCE = "https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT"

        URL_WEEBHOOK_DISCORD = "https://discordapp.com/api/webhooks/1509547644438057041/jUP-kUu4iaEKYVCZLmSnPjybD8s3EY8zYL9wow7zBvUmrOi7ebMpz3sFX1R45dSIB7IR"

        response = requests.get(URL_VARIATION_BINANCE).json()
        current_price = float(response["lastPrice"])
        current_volume = float(response["volume"])

        print(f"Preço atual: {current_price:,.2f}")
        print(f"Volume atual: {current_price:,.2f}")
    except Exception as e:
        print(f"Erro ao se comunicar com a API da Binance: {e}")

def send_message_to_discord(content):
    pass

catch_volume_and_currentprice()
    
    

    

