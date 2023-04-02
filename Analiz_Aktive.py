import yfinance as yf


aapl = yf.Ticker("aapl")

history = aapl.history(period="max")
print(history)
