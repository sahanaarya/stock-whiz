import yfinance as yf
import argparse

# define the ticker symbol
# TODO: pass this in as command line arg
tickerSymbol = 'AAPL'

# retrieve data on ticker
tickerData = yf.Ticker(tickerSymbol)

# get the historical prices for this ticker as dataframe
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-30')