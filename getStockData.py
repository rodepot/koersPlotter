import datetime as dt
import pickle
import os
import pandas as pd

def downl_price(name,link):
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

def read_stock(name,link,typ):
    # routine to check is a cached file is present of the most recent (daily) data. If not then downloaded. If yes, then chache
    # cache is loaded.
    if os.path.isfile("data/"+name) == True:
        if pd.to_datetime(dt.datetime.now()).floor('1D') == pd.to_datetime(os.path.getmtime("data/"+name),unit='s').floor('1D'):
            f = open("data/"+name,'rb')
            df_final = pickle.load(f)
            print('Loaded {} from cache'.format(name))
        else:
            print('Downloading {}'.format(link))
            if typ == 'ohlcv':
                df_final = downl_ohlcv(name,link)
            elif typ == 'price':
                df_final = downl_price(name,link)
            df_final.to_pickle("data/"+name)
            print('Cached {} at {}'.format(link, name))
    elif os.path.isfile("data/"+name) == False:
        print('Downloading {}'.format(link))
        if typ == 'ohlcv':
            df_final = downl_ohlcv(name,link)
        elif typ == 'price':
            df_final = downl_price(name,link)
        df_final.to_pickle("data/"+name)
        print('Cached {} at {}'.format(link, name))
    return df_final
#url_Ves = 'http://tools.morningstar.nl/api/rest.svc/timeseries_ohlcv/8qe8f2nger?currencyId=EUR&idtype=Morningstar&frequency=daily&startDate=2008-01-01&performanceType=&outputType=COMPACTJSON&id=0P0000BHUH]3]0]E0WWE$$ALL'
#df_Ves = read_ohlcv('Ves',url_Ves)
