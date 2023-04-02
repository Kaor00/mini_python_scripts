from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter


api = CurrencyRates()
btc = BtcConverter()

btc_price = btc.get_latest_price('USD')
dollar_rate = api.get_rate("RUB", "USD")
convert = api.convert("RUB", "USD", 1000)

print(f"BTC price: {round(btc_price, 3)}$")
print(f"1P = {round(dollar_rate, 3)}$")
print(f"1000P = {round(convert, 3)}$")
