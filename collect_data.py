from datetime import datetime, timedelta
import itertools

import pandas as pd
from pytrends.request import TrendReq
from yahoofinancials import YahooFinancials
import numpy as np


#----------------------pytrends--------------------------
def historical_pytrends(start = (datetime.now() - timedelta(days=265)).strftime("%Y-%m-%d"), 
                        end = datetime.now().strftime("%Y-%m-%d"), keys = ["stock","call","put"], cat = "0", geo="", gprop=""):
    df = pd.DataFrame()
    pytrends = TrendReq(hl='en-US')

    pytrends.build_payload(keys,
                        cat,
                        start+" "+end,
                        geo,
                        gprop)
    
    data = pytrends.interest_over_time() #--> 265 maxim!!!
    data.drop('isPartial', axis=1, inplace=True)

    return data#data.iloc[1:] --> treu 1a columna que no hi ha el % de millora

def get_all_pytrends(start = (datetime.now() - timedelta(days=265)).strftime("%Y-%m-%d"), 
                        end = datetime.now().strftime("%Y-%m-%d"), total_days=2000):
    keys = [['Bitcoin',"Tesla","Apple","Gold","Oil"],
          ["stock","call","put"],
          ["stock up","stock down","bear market","bull market","recession"]]
    #for i in range()
    for i, group in enumerate(keys):
      l = []
      for index in range(total_days//265):
        start = (datetime.now() - timedelta(days=265*(index+1))).strftime("%Y-%m-%d")
        end = (datetime.now() - timedelta(days=265*index)).strftime("%Y-%m-%d")
        l.append(historical_pytrends(start, end, keys=group))
      if i == 0:
        df = pd.concat(l)
      else:
        df = df.join(pd.concat(l))


    df = df_add_improve_cols(df)

    return df 

#----------------------yahoo--------------------------
def historical_yahoo_one(start = (datetime.now() - timedelta(days=20000)).strftime("%Y-%m-%d"),
                    end= datetime.now().strftime("%Y-%m-%d"), ticker = "BTC-USD", rename=True, featuring=True):#,"TSLA",'WFC', 'BAC', 'C' ,'EURUSD=X', 'JPY=X', 'GBPUSD=X', 'PRLAX', 'QASGX', 'HISFX']):

    yahoo_financials = YahooFinancials(ticker)
    historical_stock_prices = yahoo_financials.get_historical_price_data(start, end, 'daily')
    data = pd.DataFrame(historical_stock_prices[ticker]['prices'])
    if rename:
        data.columns = [x +'_'+ticker if x!='formatted_date' else x for x in data.columns]
    if featuring:
        c_open = np.nan_to_num(np.asarray(data['open_'+ticker]))
        c_close = np.nan_to_num(np.asarray(data['close_'+ticker]))

        data[ticker + "%"] = ((c_close / c_open) -1) * 100
        data[ticker + "_Y"] = data.apply(lambda row: classificator(row, str(ticker) + "%"),axis=1)
        data[ticker + "_Vol"] = np.asarray(data['volume_'+ticker])
        data[ticker + "_YPred"] = np.append(data.apply(lambda row: classificator(row, str(ticker) + "%"),axis=1)[1:],[None])
    return data

def get_all_yahoo():
    tech_stocks = ['AAPL', 'MSFT', 'INTC']
    bank_stocks = ['WFC', 'BAC', 'C']
    commodity_futures = ['GC=F', 'SI=F', 'CL=F']
    cryptocurrencies = ['BTC-USD', 'ETH-USD', 'XRP-USD']
    currencies = ['EURUSD=X', 'JPY=X', 'GBPUSD=X']
    mutual_funds = ['PRLAX', 'QASGX', 'HISFX']
    us_treasuries = ['^TNX', '^IRX', '^TYX']
    global_tickers = [tech_stocks, bank_stocks, commodity_futures, cryptocurrencies, currencies, mutual_funds, us_treasuries]
    #for i,ticker in enumerate(tech_stocks):
    for i,ticker in enumerate(itertools.chain.from_iterable(global_tickers)):
        print(i, ticker)
        if i == 0:
          df = historical_yahoo_one(ticker=ticker).set_index('formatted_date')
        else:
          data = historical_yahoo_one(ticker=ticker).set_index('formatted_date')
          df = df.join(data)#.reset_index()
    return df#.set_index('formatted_date')

#----------------------utils--------------------------
def classificator(row, location):
    if row[location] >= 1.25:
      return 4
    elif row[location] >= 0.35:
      return 3
    elif row[location] <= -1.25:
      return 0
    elif row[location] <= -0.35:
      return 1
    else:
      return 2

def df_add_improve_cols(df):
    for col in df:
          dfx = df[col]
          df[col+"%"] = np.asarray([((dfx[x] / dfx[x-1]+1e-3) -1) * 100 if x>0 else 0 for x in range(len(dfx))])
    return df.iloc[1:] #we cannot calculate improvement on 1st row

def parser(s):
    return datetime.strptime(s, '%Y-%m-%d')

if __name__ == "__main__":
    df_test = historical_yahoo_one()
    df_test.to_csv("test_yahoo.csv",index=True)

    df_pytrends = get_all_pytrends()
    df_pytrends.to_csv("pytrends_data.csv",index=True)

    df_yahoo = get_all_yahoo()
    df_yahoo.to_csv("yahoo_data.csv",index=True)  


    catfish_sales = pd.read_csv('pytrends_data.csv', parse_dates=[0], index_col=0, date_parser=parser)#squeeze=True --> .squeeze(col)
    print(catfish_sales.head())