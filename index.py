# Import necessary libraries
from __future__ import (absolute_import, division, print_function, unicode_literals)
import backtrader as bt
import datetime
import os.path
import sys

# Define the trading strategy
class Strategy(bt.Strategy):

    # Define a log function for better debugging and tracking
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    # Initialize the strategy
    def __init__(self):
        self.dataclose = self.datas[0].close

    # Define what to do on each iteration of the trading loop
    def next(self):
        self.log('Close, %.2f' % self.dataclose[0])

# Main function to run the strategy
if __name__ == '__main__':

    # Create a cerebro entity which is the main object of Backtrader
    account = bt.Cerebro()

    # Define data feed parameters
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, '../../datas/orcl-1995-2014.txt')

    # Create a data feed
    data = bt.feeds.YahooFinanceCSVData(
        dataname=datapath,
        fromdate=datetime.datetime(2000, 1, 1),
        todate=datetime.datetime(2000, 12, 31),
        reverse=False)

    # Add the data feed to cerebro
    account.adddata(data)

    # Set our desired cash start
    account.broker.setcash(100000.0)

    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % account.broker.getvalue())

    # Run over everything
    account.run()

    # Print out the final result
    print('Final Portfolio Value: %.2f' % account.broker.getvalue())
