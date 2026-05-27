import time
import requests

PREVIOUS_PRICE = None

URL_BINANCE = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
URL_DISCORD_WEBHOOK = "https://discordapp.com/api/webhooks/1509165941483900968/PV5nIh6U0waMWVOPfrn28O9pGC66mKGQEMY5EryreMtjRhEN3qPDPDftcKmOPr2ECQX8"

def enviar_mensagem_discord(conteudo):
    
    data = {"content": conteudo}
    try:
        resposta = requests.post(URL_DISCORD_WEBHOOK, json=data)
        if resposta.status_code == 204:
            print("Alerta enviado com sucesso para o Discord!")
        else:
            print(f"Erro ao enviar para o Discord: {resposta.status_code}")
    except Exception as e:
        print(f"Falha na rede ao tentar avisar o Discord: {e}")

                           

def monitorate_bitcoin():
    global PREVIOUS_PRICE
    try:
        response = requests.get(URL_BINANCE).json()
        current_price = float(response["price"])
        bitcoin_symbol = response["symbol"]
        print(f"Preço atual do bitcoin: {current_price}")
        print(f"Símbolo: {bitcoin_symbol}")

        difference = current_price - PREVIOUS_PRICE

        if difference > 0:
            mensagem = f"🟩 **Subiu!** BTC: **${current_price:,.2f}** (+${difference:,.2f})"
            enviar_mensagem_discord(mensagem)
        elif difference < 0:
            mensagem = f"🟩 **Desceu!** BTC: **${current_price:,.2f}** (+${difference:,.2f})"
            enviar_mensagem_discord(mensagem)    

    except Exception as e:
        print(f"Erro ao conectar na API da Binance: {e}")   


while True:
    monitorate_bitcoin()
    time.sleep(5)



