#! /usr/bin/env python3

'''
https://towardsdatascience.com/easiest-guide-to-getting-stock-data-with-python-f74b5f75d179

Get stock market data for multiple tickers
'''

import yfinance as yf
import pandas as pd 
import matplotlib.pyplot as plt 

if __name__ == '__main__':
    data = yf.download('AAPL MSFT SAP PTON LULU PYPL NKE VOO COP COST KO PG')
    data.head()
    data['Adj Close'].plot(figsize=(10,7))
    plt.legend() 
    plt.title('Adusted Close Price', fontsize=16)
    plt.ylabel('Price', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.grid(which='major', color='k', linestyle='-.', linewidth=0.5)
    plt.show()     
