from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest
    
API_KEY = "PKBFRFWBV2IIXYC9BPQ5"
SECRET_KEY = "9rZHrcqHyVAqh6TrljCTayCfghqTmY9HRpkBK7uE"

stock_client = StockHistoricalDataClient(
    API_KEY, SECRET_KEY)

multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=["SPY", "GLD", "TLT"])

latest_multisymbol_qoutes = stock_client.get_stock_latest_quote(multisymbol_request_params)

gld_latest_ask_price = latest_multisymbol_qoutes["GLD"].ask_price
spy_latest_ask_price = latest_multisymbol_qoutes["SPY"].ask_price
tlt_latest_ask_price = latest_multisymbol_qoutes["TLT"].ask_price

print("The current price of TLT is " + str(tlt_latest_ask_price))
print("The current price of SPY is " + str(spy_latest_ask_price))
print("The current price of GLD is " + str(gld_latest_ask_price))

"""
async def get_account_info():
    print("Hello World")

async def get_last_bars():
    print("Hello World")

async def get_realtime_price():
    print("Hello World")
"""
