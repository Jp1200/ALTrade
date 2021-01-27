import alpaca_trade_api as tradeapi
import matplotlib
import pprint
import numpy

# https://github.com/alpacahq/alpaca-trade-api-python/ 
def read_keys(file_name):
    f = open(file_name, 'r')
    KEYS = f.readlines()

    keys= []
    for key in KEYS:
        keys.append(key.strip())
    f.close()
    return keys[0], keys[1]

API_KEY_PAPER, SECRET_PAPER = read_keys('keys_paper.txt')

api = tradeapi.REST(API_KEY_PAPER, SECRET_PAPER, base_url='https://paper-api.alpaca.markets')

def listPos(api):
    positions = api.list_positions()
    for position in positions:
        print(position)

    return positions

account = api.get_account()
print(api.list_orders())
print(listPos(api))