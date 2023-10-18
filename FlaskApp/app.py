# Importing necessary modules
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import backtrader as bt
import datetime
from flask import Flask, render_template, request

# Creating a Flask app
app = Flask(__name__)

# Defining the home route
@app.route("/")
@app.route("/home")
def home():
    # Rendering the home page
    return render_template("index.html")

# Defining the result route which accepts both POST and GET requests
@app.route("/result", methods=["POST", "GET"])
def result():
    # Converting the form data to a dictionary
    output = request.form.to_dict()

    # Extracting the stock name, investment amount and start date from the form data
    stock_name = output["stock_name"]
    investment = float(output["investment"])
    start_date = int(output["start_date"])

    # Defining a class for the trading strategy
    class Strategy(bt.Strategy):

        # Defining the parameters for the fast and slow moving averages
        params = dict(
            fast_period=10,
            slow_period=30
        )

        # Defining a function to log messages with dates
        def log(self, txt, dt=None):
            dt = dt or self.datas[0].datetime.date(0)
            if isinstance(dt, float):
                dt = bt.num2date(dt)
            print('%s, %s' % (dt.isoformat(), txt))

        # Defining a function to handle order notifications and print the order status and execution details
        def notify_order(self, order):
            if order.status in [order.Submitted, order.Accepted]:
                self.log('ORDER ACCEPTED/SUBMITTED', dt=order.created.dt)
                self.order = order
                return

            if order.status in [order.Expired]:
                self.log('EXPIRED')

            elif order.status in [order.Completed]:
                if order.isbuy():
                    self.log(
                        'BUY EXECUTED, Price: %.2f, Cost: %.2f' %
                        (
                            order.executed.price,
                            order.executed.value
                        ))

                else:
                    self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f' %
                             (
                                 order.executed.price,
                                 order.executed.value
                             ))

            self.order = None

        # Defining an initialization function to create two simple moving averages and a crossover indicator
        def __init__(self):
            sma1 = bt.ind.SMA(period=self.p.fast_period)
            sma2 = bt.ind.SMA(period=self.p.slow_period)
            self.crossover = bt.ind.CrossOver(sma1, sma2)

        # Defining a next function to execute buy and sell orders based on the crossover signal
        def next(self):
            if not self.position:
                if self.crossover > 0:
                    self.buy(data, size=investment)

            elif self.crossover < 0:
                self.close()

    # If this is the main module, then:
    if __name__ == '__main__':

        # Create a Cerebro object and add the strategy
        account = bt.Cerebro()
        account.addstrategy(Strategy)

        # Create a data feed from Yahoo Finance CSV file with the given stock name and date range
        data = bt.feeds.YahooFinanceCSVData(
            dataname="orcl.csv",
            fromdate=datetime.datetime(start_date, 1, 1),
            todate=datetime.datetime(2014, 12, 31),
            reverse=None)

        # Add the data feed to Cerebro
        account.adddata(data)

        # Set the initial cash for the broker
        account.broker.setcash(1000000000.0)

        # Get the starting value of the portfolio
        starting_value = account.broker.getvalue()

        # Run Cerebro
        account.run()

        # Get the end value of the portfolio
        end_value = account.broker.getvalue()

        # Calculate the earned amount by subtracting the starting value from the end value
        earned = end_value - starting_value

        # Print the final portfolio value
        print('Final Portfolio Value: %.2f' % account.broker.getvalue())

    # Render the index.html template with the earned amount as a variable
    return render_template("index.html", earned=earned)

# If this is the main module, then run the app in debug mode and on port 5000.
if __name__ == "__main__":
    app.run(debug=True, port=5000)
