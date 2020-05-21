from pandas_datareader import data as pdr
from scipy.stats import pearsonr
import yfinance.__init__ as yf
import pandas as pd

yf.pdr_override()

def filter(stocks):
    stockList = []
    for stock in stocks:
        try:
            data = pdr.get_data_yahoo(stock, start="2017-06-01", end="2019-05-31", group_by="ticker")
            if(len(data['Close']) > 0):
                stockList.append(stock)
            else:
                print("data is not available for:", stock)
        except Exception:
            print("unable to download: ", stock)

    return stockList

def correlation (stocks):
    #filter the list
    stocks = filter(stocks)
    print("After applying filter: ", len(stocks))

    # download dataframe
    data = pdr.get_data_yahoo(stocks, start="2017-06-01", end="2019-05-31", group_by="ticker")
    # drop all the row with NaN values
    data = data.dropna()
    #initialize dictionary
    corr_dict = {}
    for stock in stocks:
        corr_dict[stock] = [0.0]*len(stocks)

    #intialize dataframe
    df = pd.DataFrame(corr_dict, index=stocks)
    xPoints = []

    # calculate Pearson's correlation between all the listed companies
    for i in range(len(stocks)):
        for j in range(i, len(stocks)):
            corr, _ = pearsonr(data[stocks[i]]['Close'], data[stocks[j]]['Close'])
            df[stocks[i]][stocks[j]] = '%.2f'%(corr)
            df[stocks[j]][stocks[i]] = '%.2f'%(corr)
            xPoints.append('%.1f'%(corr))
            print(stocks[i], stocks[j], df[stocks[i]][stocks[j]])

    return df, xPoints

# if __name__ == "__main__":
#     df = data = pdr.get_data_yahoo("APOLLOPIPE.NS", start="2019-01-01", end="2019-08-30", group_by="ticker")
#     print(len(df['Close']))
    