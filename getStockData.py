import datetime as dt
import pickle
import os
import pandas as pd

import yfinance as yf
#msft = yf.Ticker("MSFT")
#msft.info
#msft.history(period="max")


def downl_morningstar(name,link):
    # Routine to read in price jsons from Morningstar, this is most often with ETFs and indexes. Name and link are both strings.
    # returns a pandas dataframe
    df_data = pd.read_json(link)
    df_data.columns = ['datum',name]
    df_data = df_data.set_index(df_data['datum'])
    df_data.index.name = None
    df_final = df_data.drop('datum',axis=1)
    df_final.index = pd.to_datetime(df_final.index,unit='ms').round('1D')
    return df_final

def downl_ohlcv(name,link):
    # Routine to read in ohlcv jsons from Morningstar, this is most often with ETFs and indexes. Name and link are both strings.
    # returns a pandas dataframe
    df_data = pd.read_json(link)
    df_data.columns = ['datum','open','low','high','close','volume']
    df_data[name] = (df_data['open']+df_data['close'])/2
    df_data = df_data.set_index(df_data['datum'])
    df_data.index.name = None
    df_final = df_data.drop(['datum','open','high','low','close','volume'],axis=1)
    df_final.index = pd.to_datetime(df_final.index,unit='ms').round('1D')
    return df_final

def stockHist(ticker):
    stock = yf.Ticker(ticker)
    df = pd.DataFrame(stock.history(period="max"))
#    stock = yf.Ticker('EZJ.L')
#    print(stock.info)
    return df


def read_stock(name, stock):
    # routine to check is a cached file is present of the most recent (daily) data. If not then downloaded. If yes, then chache
    # cache is loaded.
    pickleFile = "data/"+name+'.pkl'
    baseURL = 'http://tools.morningstar.nl/api/rest.svc/timeseries_price/8qe8f2nger?currencyId=EUR&idtype=Morningstar&frequency=daily&startDate=2008-01-01&priceType=&outputType=COMPACTJSON&'
    link = baseURL + stock['url_morningstar']
    if os.path.isfile(pickleFile):
        if pd.to_datetime(dt.datetime.now()).floor('1D') == pd.to_datetime(os.path.getmtime(pickleFile),unit='s').floor('1D'):
            f = open(pickleFile,'rb')
            df_final = pickle.load(f)
            print('Loaded {} from cache'.format(name))
        else:
            print('Downloading {}'.format(link))
            df_final = downl_morningstar(name,link)
            df_final.to_pickle(pickleFile)
            print('Cached {} at {}'.format(link, name))
    else:
        print('Downloading {}'.format(link))
        df_final = downl_morningstar(name,link)
        df_final.to_pickle(pickleFile)
        print('Cached {} at {}'.format(name, link))
    return df_final
#url_Ves = 'http://tools.morningstar.nl/api/rest.svc/timeseries_ohlcv/8qe8f2nger?currencyId=EUR&idtype=Morningstar&frequency=daily&startDate=2008-01-01&performanceType=&outputType=COMPACTJSON&id=0P0000BHUH]3]0]E0WWE$$ALL'
#df_Ves = read_ohlcv('Ves',url_Ves)
