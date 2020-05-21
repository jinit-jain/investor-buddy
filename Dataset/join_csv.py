# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:50:03 2020

@author: siddh
"""

from csv import reader
import pandas as pd

companies = dict()
output_file = "finalDB.xlsx"

# with open('EQUITY_L.csv', 'r') as f1:
#     ip1 = reader(f1)
#     next(ip1)
#     for row in ip1:
#         companies[row[0]] = row[1]


ip2 = pd.read_excel(output_file)
# ip2.rename(columns={'Symbol ':'Symbol'}, inplace=True)
# ip2["Company"] = ip2['Symbol'].map(companies)
# print(ip2.columns)
# print(ip2)
#  if isinstance(x, str) else x
ip2.applymap(lambda x: x.strip())
ip2.to_csv('finalDB.csv', index=False, header=True)