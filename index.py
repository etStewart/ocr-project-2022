from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.trading.client import TradingClient
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

sma20 = 0
sma50 = 0
    
API_KEY = "PKBFRFWBV2IIXYC9BPQ5"
SECRET_KEY = "9rZHrcqHyVAqh6TrljCTayCfghqTmY9HRpkBK7uE"

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
stock_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)

def GET_ACCOUNT_INFO():
    ACCOUNT = trading_client.get_account()
    return ACCOUNT

def initialize_average():
    current_time = datetime.now()
    last_minute_time = current_time.minute - 50

    initial_data = StockBarsRequest(
        symbol_or_symbols=["SPY", "GLD"],
        timeframe=TimeFrame.Minute,
        start=datetime(2022, 7, 1),
        end=datetime(2022, 9, 1)
    )

    bars = stock_client.get_stock_bars(initial_data)
    panda_bars = bars.df

    print(last_minute_time)

initialize_average()

    