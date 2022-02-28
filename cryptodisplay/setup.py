# Importa librerías y clases fundamentales para esta sencilla aplicación web.
import datetime
from binance.client import Client


# Define una función para logearse en la api de Binance
def log_in_client():
    
    a = open("api_key.txt","r")
    api_key = a.read().strip()

    b = open("api_secret.txt","r")
    api_secret = b.read().strip()

    a.close()
    b.close()

    client = Client(api_key, api_secret)
    print("Logged in")
    return client

# Define una función que devuelve los valores actuales de criptomedas específicas.
def get_prices():
    #An example portfolio
    portfolio = {'ADABTC':'0','LTCBTC':'0','UNIBTC':'0','ETHBTC':'0'}
    client = log_in_client()
    tickers = client.get_ticker()

    for crypto in tickers:
        print(f"asset: {crypto['symbol']}")
        for asset in portfolio:
            if crypto['symbol'] == asset:
                portfolio[asset] = crypto['askPrice']
    
    return portfolio


# Define una función que devuelve la hora actual.
def get_time():

    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time