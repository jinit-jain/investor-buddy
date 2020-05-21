from pandas_datareader import data as pdr
from scipy.stats import pearsonr
import yfinance.__init__ as yf
import pandas as pd
from math import isnan

yf.pdr_override()

def filter(stocks):
    stockList = []
    # data_map = pd.DataFrame()
    for stock in stocks:
        try:
            data = pdr.get_data_yahoo(stock, start="2017-06-01", end="2019-05-31", group_by="ticker")
            if(len(data['Close']) > 0):
                # print(len(data['Close']))
                stockList.append(stock)
                # data_map[stock] = data['Close']
                # close_map.append(data['Close'])
            else:
                print("data is not available for:", stock)
                # return stockList
        except Exception:
            print("unable to download: ", stock)

    return stockList

def correlation (stocks):
    #filter the list
    try:
        data = pd.read_csv('stock_history.csv', encoding='utf-8')
    except FileNotFoundError:
        stocks = filter(stocks)
        print("After applying filter: ", len(stocks))
    
        # download dataframe
        unfiltered_data = pdr.get_data_yahoo(stocks, start="2017-06-01", end="2019-05-31", group_by="ticker")
        # print(unfiltered_data)
        data = pd.DataFrame()
        for column in unfiltered_data.columns:
            # print(column)
            if column[1] == 'Close':
                data[column[0]] = unfiltered_data[column]  
        data.to_csv('stock_history.csv', index=False, header=True)
        
    stocks = data.columns
    # filter data
    for stock in stocks:
        stock_mean_nan = data[stock].isnull().mean()
        # If stock history has 10% values as null values, remove that stock
        if stock_mean_nan >= 0.1:
            data.pop(stock)
        else:
            close = [float(num) for num in data[stock]]
            for i in range(len(close)):
                if isnan(close[i]):
                    if i==0:
                        close[i] = data[stock].sum()/len(close)
                    else:
                        close[i] = close[i-1]
            # print(close)   
            data[stock] = close
            if data[stock].isnull().mean() != 0:
                print(stock, data[stock].isnull().mean())
            
    #initialize dictionary
    stocks = data.columns
    corr_dict = {}
    for stock in stocks:
        corr_dict[stock] = [0.0]*len(stocks)

    #intialize dataframe
    df = pd.DataFrame(corr_dict, index=stocks)
    xPoints = []

    # calculate Pearson's correlation between all the listed companies
    for i in range(len(stocks)):
        
        for j in range(i, len(stocks)):
            corr, _ = pearsonr([float(num) for num in data[stocks[i]]], [float(num) for num in data[stocks[j]]])
            df[stocks[i]][stocks[j]] = '%.2f'%(corr)
            df[stocks[j]][stocks[i]] = '%.2f'%(corr)
            xPoints.append('%.1f'%(corr))
            # print(stocks[i], stocks[j], df[stocks[i]][stocks[j]])

    return df, xPoints

# if __name__ == "__main__":
#     df = data = pdr.get_data_yahoo("APOLLOPIPE.NS", start="2019-01-01", end="2019-08-30", group_by="ticker")
#     print(len(df['Close']))
    