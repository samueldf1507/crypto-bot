import requests
import time

URL_BINANCE = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"

URL_WEEBHOOK_DISCORD = "https://discordapp.com/api/webhooks/1509547644438057041/jUP-kUu4iaEKYVCZLmSnPjybD8s3EY8zYL9wow7zBvUmrOi7ebMpz3sFX1R45dSIB7IR"

PREVIOUS_PRICE = None

def send_message_to_discord(content):
    data = {"content": content}
    try:
        response = requests.post(URL_WEEBHOOK_DISCORD , json=data)
        if response.status_code == 204:
            print("Mensagem enviada com sucesso para o Discord!")
        else:
            print("Erro ao tentar se conectar com sucesso")    

    except Exception as e:
        print(f"Falha na rede ao tentar avisar o Discord: {e}")

def monitorate_ethereum():
    global PREVIOUS_PRICE
    try:
        response = requests.get(URL_BINANCE).json()
        current_price = float(response["price"])
        

        if PREVIOUS_PRICE is None:
            PREVIOUS_PRICE = current_price
            return

        difference = current_price - PREVIOUS_PRICE

        if difference > 0:
            message = f"\U0001F7E9 Subiu! ETH = {current_price:,.2f} ({difference:,.1f})"  
            send_message_to_discord(message)
        elif difference < 0:
            message = f"\U0001F7E5 Desceu! ETH = {current_price:,.2f} ({difference:,.1f})"
            send_message_to_discord(message)

        else:
            print("mimimi")

        PREVIOUS_PRICE = current_price      
    except Exception as e:
        print(f"Erro ao tentar se conectar com a API da Binance")   

while True:
    monitorate_ethereum()
    time.sleep(5) 

