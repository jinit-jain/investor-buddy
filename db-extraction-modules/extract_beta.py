# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:12:32 2020

@author: siddh
"""

from csv import reader
import yfinance as yf
import pandas as pd

beta = []

symbols = list()
with open('finalDB.csv', 'r', encoding='utf-8') as f1:
    ip1 = reader(f1)
    next(ip1)
    for row in ip1:
        symbols.append(row[0])

with open('tempBeta.csv', 'r', encoding='utf-8') as temp:
    t1 = reader(temp)
    for value in t1:
        beta.append(float(value[0]))
        print(beta[-1])

df = pd.read_csv('finalDB.csv', encoding='utf-8')

skipper = 'ARIES'
cont = True
try:
    for symbol in symbols:
        if cont:
            if symbol == skipper:
                print('starting from', skipper, "...")
                cont = False
            continue
        nse_symbol = "{}.NS".format(symbol)
        # print(symbol, type(symbol))
        info = yf.Ticker(nse_symbol).info
        value = 9999
        if not info['beta'] is None:
            value = float(info['beta'])
        beta.append(value)
        print(symbol, value)
except Exception:
    temp_store = pd.DataFrame({'beta': beta})
    temp_store.to_csv('tempBeta.csv', index=False, header=False)
else:
    df['beta'] = beta  
    df.to_csv('finalBetaDB.csv', index=False, header=True)