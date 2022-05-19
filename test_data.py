from collect_data import get_all_yahoo, get_all_pytrends, parser

import pandas as pd

if __name__ == "__main__":

    catfish_sales = pd.read_csv('pytrends_data.csv', parse_dates=[0], index_col=0, date_parser=parser)#squeeze=True --> .squeeze(col)
    print(catfish_sales.head())