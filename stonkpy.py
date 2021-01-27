import alpaca_trade_api as tradeapi
import matplotlib
import pprint
import numpy

# https://github.com/alpacahq/alpaca-trade-api-python/ 



api = tradeapi.REST(API_KEY_PAPER, SECRET_PAPER, base_url='https://paper-api.alpaca.markets')

def listPos(api):


account = api.get_account()
print(api.list_positions())