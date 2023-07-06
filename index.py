from __future__ import (absolute_import, division, print_function, unicode_literals)
# Importing necessary libraries
import backtrader as bt

if __name__ == '__main__':
    # Create a cerebro instance
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(100000.0)

    # Print the starting portfolio value
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Run the strategy
    cerebro.run()

    # Print the final portfolio value
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
