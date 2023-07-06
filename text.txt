# Importing the required modules from the libraries
from datetime import datetime, timedelta
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.trading.client import TradingClient
from alpaca.data.timeframe import TimeFrame

# Initializing SMA_20 and SMA_50 to 0 and symbol to "SPY"
SMA_20 = 0
SMA_50 = 0

# Setting the API key and secret key to API_KEY and SECRET_KEY respectively
API_KEY = "PKBFRFWBV2IIXYC9BPQ5"
SECRET_KEY = "9rZHrcqHyVAqh6TrljCTayCfghqTmY9HRpkBK7uE"

# Initializing the TradingClient and StockHistoricalDataClient with the API key and secret key
trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
stock_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)

# Defining a function get_account_info() which returns the account information
def get_account_info():
    account = trading_client.get_account()
    return account

# Defining a function get_bar_from_50_min(symbol) which gets the stock bars for the last 50 minutes for the given symbol
def get_bar_from_50_min():
    now = datetime.now()
    time_50_minutes_ago = now - timedelta(minutes=50)
    
    request_params = StockBarsRequest(symbol_or_symbols="SPY", start=time_50_minutes_ago, end=now, timeframe=TimeFrame.Minute)

    bars = stock_client.get_stock_bars(request_params)
    
    # Printing the time 50 minutes ago and the bars for that time period.
    print(time_50_minutes_ago)
    

get_bar_from_50_min()
