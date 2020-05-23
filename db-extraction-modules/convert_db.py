# -*- coding: utf-8 -*-
"""
Created on Mon May 18 19:44:34 2020

@author: siddh
"""
import csv
from csv import writer
# import pandas as pd
import yfinance as yf
# from . 

file1 = "EQUITY_L.csv"
output_file = "db2.csv"
# file2 = "NSE-Stock-LIST-1411-Stocks-Generated-on-25may2017.xlsx"
# symbols = dict()
tickers = list()
companies = list()
sectors = list()
sub_sectors = list()

def append_row(file_name, row):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(row)

with open(file1, 'r') as read_csv:
    ip1 = csv.reader(read_csv)
    next(ip1)
    for row in ip1:
        tickers.append(row[0])
        companies.append(row[1])
        # symbols.setdefault(row[1], []).append(row[0])

print_company_info = False
true_ticker = "VIDEOIND"
for ticker in tickers:
    if not print_company_info:
        if ticker == true_ticker:
            print_company_info = True
        # sectors.append('')
        # sub_sectors.append('')
        # print('..')
        continue
    nsTicker = "{}.NS".format(ticker)
    # print(nsTicker)
    dt = yf.Ticker(nsTicker).info
    sector, sub_sector = '', ''
    if 'sector' in dt:
        sector = dt['sector']
    if 'industry' in dt:
        sub_sector = dt['industry']
    # sectors.append(sector)
    # sub_sectors.append(sub_sector)
    row = [ticker, sector, sub_sector]
    append_row(output_file, row)
    print(ticker, ",", sector, ",", sub_sector)


# ip2 = pd.read_excel(file2)
# db = pd.DataFrame({'Ticker': tickers, 'Company': companies, 'Sector': sectors, 'Sub-sector': sub_sectors})

# db.to_csv('companiesDatasetUpd.csv', index=False, header=True)

# ip2["Company"] = ip2['Symbol'].map(companies)
# print(ip2.columns)

# outputDB = ip2.filter(['Symbol', 'Company', 'Sector', 'Sub Sector'], axis=1)

# outputDB.to_csv('companiesDataset.csv', index=False, header=True)