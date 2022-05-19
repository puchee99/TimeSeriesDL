from datetime import datetime, timedelta

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

def all_pytrends(start = (datetime.now() - timedelta(days=265)).strftime("%Y-%m-%d"), 
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

a="abv"

#----------------------yahoo--------------------------


#----------------------utils--------------------------
def df_add_improve_cols(df):
    for col in df:
          dfx = df[col]
          df[col+"%"] = np.asarray([((dfx[x] / dfx[x-1]+1e-3) -1) * 100 if x>0 else 0 for x in range(len(dfx))])
    return df.iloc[1:] #we cannot calculate improvement on 1st row


if __name__ == "__main__":
    df = all_pytrends()
    df.to_csv("pytrends_data.csv",index=False) 
