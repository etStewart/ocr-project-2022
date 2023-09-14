from __future__ import (absolute_import, division, print_function, unicode_literals)

import backtrader as bt
import datetime
import os.path
import sys

if __name__ == '__main__':

    account = bt.Cerebro()
    account.broker.setcash(100000.0)

    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, '../../datas/orcl-1995-2014.txt')

    datafeed = bt.feed.YahooFinanceCSVData(
        dataname = datapath,
        fromdate = datetime.datetime(2000, 1, 1),
        todate = datetime.datetime(2000, 12, 1),
        reverse = False
    )

    account.adddata(datafeed)

    print('Starting Portfolio Value: %.2f' % account.broker.getvalue())

    account.run()

    print('Final Portfolio Value: %.2f' % account.broker.getvalue())
