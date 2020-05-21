# -*- coding: utf-8 -*-
"""
Created on Thu May 21 04:06:27 2020

@author: siddh
"""
from csv import reader, writer
# import pandas as pd

no_beta_symbol = []

rows = []

with open('BetaDB.csv', 'r', encoding='utf-8') as f1:
    ip1 = reader(f1)
    fields = next(ip1)
    rows.append(fields)
    for row in ip1:
        if float(row[-1]) != 9999:
            rows.append(row)

print(len(rows))

with open('finalBetaDB.csv', 'a+', newline='') as write_obj:
    csv_writer = writer(write_obj)
    for row in rows:
        csv_writer.writerow(row)

# print(len(no_beta_symbol))
# for symbol in no_beta_symbol:
#     print(symbol)