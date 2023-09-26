from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt

import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/result", methods=["POST", "GET"])
def result():
    output = request.form.to_dict()

    stock_name = output["stock_name"]
    investment = float(output["investment"])
    start_date = int(output["start_date"])

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
                    self.buy(data, size=investment)

            elif self.crossover < 0:
                self.close()

    if __name__ == '__main__':

        account = bt.Cerebro()
        account.addstrategy(Strategy)

        data = bt.feeds.YahooFinanceCSVData(
            dataname="orcl.csv",
            fromdate=datetime.datetime(start_date, 1, 1),
            todate=datetime.datetime(2014, 12, 31),
            reverse=None)

        account.adddata(data)

        account.broker.setcash(1000000000.0)

        starting_value = account.broker.getvalue()

        account.run()

        end_value = account.broker.getvalue()

        earned = end_value - starting_value

        print('Final Portfolio Value: %.2f' % account.broker.getvalue())

    return render_template("index.html", earned=earned)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
