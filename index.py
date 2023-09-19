from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime

import backtrader as bt

name = 'orcl'


class Strategy(bt.Strategy):

    params = dict(
        fast_period=10,
        slow_period=30
    )

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        if isinstance(dt, float):
            dt = bt.num2date(dt)
        print('%s, %s' % (dt.isoformat(), txt))

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

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.fast_period)
        sma2 = bt.ind.SMA(period=self.p.slow_period)
        self.crossover = bt.ind.CrossOver(sma1, sma2)

    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy(data, size=6)

        elif self.crossover < 0:
            self.close()


if name == 'orcl':
    stock = 'orcl.csv'

account = bt.Cerebro()
account.addstrategy(Strategy)

data = bt.feeds.YahooFinanceCSVData(
    dataname=stock,
    fromdate=datetime.datetime(1996, 1, 1),
    todate=datetime.datetime(2011, 5, 24),
    reverse=None)

account.adddata(data)

account.broker.setcash(100.0)

print('Starting Portfolio Value: %.2f' % account.broker.getvalue())

account.run()

print('Final Portfolio Value: %.2f' % account.broker.getvalue())
