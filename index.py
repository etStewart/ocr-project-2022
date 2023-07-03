from datetime import datetime
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.trading.client import TradingClient
from alpaca.data.timeframe import TimeFrame

SMA_20 = 0
SMA_50 = 0
   
API_KEY = "PKBFRFWBV2IIXYC9BPQ5"
SECRET_KEY = "9rZHrcqHyVAqh6TrljCTayCfghqTmY9HRpkBK7uE"

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
stock_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)

def get_account_info():
    account = trading_client.get_account()
    return account

def initialize_average():
    now = datetime.datetime.now()
    time_50_minutes_ago = now - datetime.timedelta(minutes=50)

    initial_data = StockBarsRequest(
        symbol_or_symbols=["SPY", "GLD"],
        timeframe=TimeFrame.Minute,
        start=time_50_minutes_ago,
        end=now
    )

print(get_account_info())



    