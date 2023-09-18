from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime
import os.path
import sys

import backtrader as bt


class Strategy(bt.Strategy):

    params = dict(
        fast_period=10,
        slow_period=30
    )

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.fast_period)
        sma2 = bt.ind.SMA(period=self.p.slow_period)
        self.crossover = bt.ind.CrossOver(sma1, sma2)

    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()

        elif self.crossover < 0:
            self.close()


account = bt.Cerebro()
account.addstrategy(Strategy)

data = bt.feeds.YahooFinanceCSVData(
    dataname='orcl.csv',
    fromdate=datetime.datetime(1996, 1, 1),
    todate=datetime.datetime(2014, 12, 31),
    reverse=None)

account.adddata(data)

account.broker.setcash(100000.0)

print('Starting Portfolio Value: %.2f' % account.broker.getvalue())

account.run()

print('Final Portfolio Value: %.2f' % account.broker.getvalue())


'''
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
'''


'''
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED, %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))
                self.buyprice = order.executed.price
            elif order.issell():
                self.log('SELL EXECUTED, %.2f' % order.executed.price)
            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        self.order = None
'''


'''
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, '../ocr-project-2022/orcl-1995-2014.txt')
'''
