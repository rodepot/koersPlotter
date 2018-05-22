
# coding: utf-8

# Dit notebook haalt de koersen van onze aandelen binnen en laat deze met interactieve grafieken zien

# # Data binnen halen en verwerken

# In[1]:


import plotly.offline as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
py.init_notebook_mode(connected=True)
import json as js
import numpy as np
import pandas as pd
import datetime as dt
import pickle
import os

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

def read_price(name,link):
    # routine to check is a cached file is present of the most recent (daily) data. If not then downloaded. If yes, then chache
    # cache is loaded.
    if os.path.isfile(name) == True:
        if pd.to_datetime(dt.datetime.now()).floor('1D') == pd.to_datetime(os.path.getmtime(name),unit='s').floor('1D'):
            f = open(name,'rb')
            df_final = pickle.load(f)
            print('Loaded {} from cache'.format(name))
        else:
            print('Downloading {}'.format(link))
            df_final = downl_price(name,link)
            df_final.to_pickle(name)
            print('Cached {} at {}'.format(link, name))
    elif os.path.isfile(name) == False:
        print('Downloading {}'.format(link))
        df_final = downl_price(name,link)
        df_final.to_pickle(name)
        print('Cached {} at {}'.format(link, name))
    return df_final

def read_ohlcv(name,link):
    # routine to check is a cached file is present of the most recent (daily) data. If not then downloaded. If yes, then chache
    # cache is loaded.
    if os.path.isfile(name) == True:
        if pd.to_datetime(dt.datetime.now()).floor('1D') == pd.to_datetime(os.path.getmtime(name),unit='s').floor('1D'):
            f = open(name,'rb')
            df_final = pickle.load(f)
            print('Loaded {} from cache'.format(name))
        else:
            print('Downloading {}'.format(link))
            df_final = downl_ohlcv(name,link)
            df_final.to_pickle(name)
            print('Cached {} at {}'.format(link, name))
    elif os.path.isfile(name) == False:
        print('Downloading {}'.format(link))
        df_final = downl_ohlcv(name,link)
        df_final.to_pickle(name)
        print('Cached {} at {}'.format(link, name))
    return df_final


# In[2]:


url_Nor = 'http://tools.morningstar.nl/api/rest.svc/timeseries_ohlcv/8qe8f2nger?currencyId=EUR&idtype=Morningstar&frequency=daily&startDate=2008-01-01&performanceType=&outputType=COMPACTJSON&id=0P00009QWG]3]0]E0WWE$$ALL'
url_Ves = 'http://tools.morningstar.nl/api/rest.svc/timeseries_ohlcv/8qe8f2nger?currencyId=EUR&idtype=Morningstar&frequency=daily&startDate=2008-01-01&performanceType=&outputType=COMPACTJSON&id=0P0000BHUH]3]0]E0WWE$$ALL'
url_Bas = 'http://tools.morningstar.nl/api/rest.svc/timeseries_ohlcv/8qe8f2nger?currencyId=EUR&idtype=Morningstar&frequency=daily&startDate=2008-01-01&performanceType=&outputType=COMPACTJSON&id=0P0000GGBW]3]0]E0WWE$$ALL'
url_Int = 'http://tools.morningstar.nl/api/rest.svc/timeseries_ohlcv/8qe8f2nger?currencyId=EUR&idtype=Morningstar&frequency=daily&startDate=2008-01-01&performanceType=&outputType=COMPACTJSON&id=0P0000S9DK]3]0]E0WWE$$ALL'
url_Gee = 'http://tools.morningstar.nl/api/rest.svc/timeseries_ohlcv/8qe8f2nger?currencyId=EUR&idtype=Morningstar&frequency=daily&startDate=2008-01-01&performanceType=&outputType=COMPACTJSON&id=0P0000CJJC]3]0]E0WWE$$ALL'
url_Eck = 'http://tools.morningstar.nl/api/rest.svc/timeseries_price/8qe8f2nger?currencyId=EUR&idtype=Morningstar&frequency=daily&startDate=2008-01-01&priceType=&outputType=COMPACTJSON&id=0P0000U0D2]2]0]ETALL$$ALL'
url_Can = 'http://tools.morningstar.nl/api/rest.svc/timeseries_price/8qe8f2nger?currencyId=EUR&idtype=Morningstar&frequency=daily&startDate=2008-01-01&priceType=&outputType=COMPACTJSON&id=F00000QU91]2]0]ETALL$$ALL'
url_Rob = 'http://tools.morningstar.nl/api/rest.svc/timeseries_price/8qe8f2nger?currencyId=EUR&idtype=Morningstar&frequency=daily&startDate=2008-01-01&priceType=&outputType=COMPACTJSON&id=F00000QDBO]2]0]ETALL$$ALL'
url_Sil = 'http://tools.morningstar.nl/api/rest.svc/timeseries_price/8qe8f2nger?currencyId=EUR&idtype=Morningstar&frequency=daily&startDate=2008-01-01&priceType=&outputType=COMPACTJSON&id=0P0000I5NQ]2]0]ETALL$$ALL'
url_VTS = 'http://tools.morningstar.nl/api/rest.svc/timeseries_price/8qe8f2nger?currencyId=EUR&idtype=Morningstar&frequency=daily&startDate=2008-01-01&priceType=&outputType=COMPACTJSON&id=0P00002DAJ]2]0]ETALL$$ALL'
url_VTB = 'http://tools.morningstar.nl/api/rest.svc/timeseries_price/8qe8f2nger?currencyId=EUR&idtype=Morningstar&frequency=daily&startDate=2008-01-01&priceType=&outputType=COMPACTJSON&id=0P0000896G]2]0]ETALL$$ALL'

buy_Eck = '2017-03-23'
buy_Ves = '2017-02-16'
buy_Bas = '2015-08-18'
buy_Nor = '2017-02-16'
buy_Int = '2016-10-24'
buy_Can = '2015-04-13'
buy_Rob = '2015-06-26'
buy_Gee = '2017-11-21'
buy_Sil = '2015-05-22'
buy_VTS = '2016-03-31'
buy_VTB = '2016-03-31'


# In[3]:


df_Ves = read_ohlcv('Ves',url_Ves)
df_Bas = read_ohlcv('Bas',url_Bas)
df_Int = read_ohlcv('Int',url_Int)
df_Nor = read_ohlcv('Nor',url_Nor)
df_Gee = read_ohlcv('Gee',url_Gee)

df_Eck = read_price('Eck',url_Eck)
df_Can = read_price('Can',url_Can)
df_Rob = read_price('Rob',url_Rob)
df_Sil = read_price('Sil',url_Sil)
df_VTS = read_price('VTS',url_VTS)
df_VTB = read_price('VTB',url_VTB)


# In[4]:


df_Koers = df_Eck.combine_first(df_Ves)
theRest = [df_Bas, df_Int, df_Nor, df_Can, df_Rob, df_Gee, df_Sil, df_VTS, df_VTB]
for dframe in theRest:
    df_Koers = df_Koers.combine_first(dframe)


# In[5]:


df_NKoers = df_Koers.copy()
df_NKoers.Eck /= df_Koers.loc[buy_Eck,'Eck']
df_NKoers.Ves /= df_Koers.loc[buy_Ves,'Ves']
df_NKoers.Bas /= df_Koers.loc[buy_Bas,'Bas']
df_NKoers.Nor /= df_Koers.loc[buy_Nor,'Nor']
df_NKoers.Int /= df_Koers.loc[buy_Int,'Int']
df_NKoers.Can /= df_Koers.loc[buy_Can,'Can']
df_NKoers.Rob /= df_Koers.loc[buy_Rob,'Rob']
df_NKoers.Gee /= df_Koers.loc[buy_Gee,'Gee']
df_NKoers.Sil /= df_Koers.loc[buy_Sil,'Sil']
df_NKoers.VTS /= df_Koers.loc[buy_VTS,'VTS']
df_NKoers.VTB /= df_Koers.loc[buy_VTB,'VTB']


# # grafiek met alle koersen
# De eerste grafiek laat de koersen zien met een horizontale lijn en verticale lijn bij aankoop. 
# De tweede grafiek laat de koersen zijn, maar deze zijn naar 1 genormaliseerd op het moment van aankoop

# In[6]:


trace_Eck = go.Scatter(x = df_Koers.index,y = df_Koers['Eck'],line = dict(color='#d62728'),legendgroup = 'Eck', name = 'vanEck',connectgaps=True)
b_Eck = go.Scatter(x = df_Koers.loc[buy_Eck:].index, y = np.ones(df_Koers.loc[buy_Eck:].index.size)*df_Koers.loc[buy_Eck,'Eck'],line = dict(dash='dash',color='#d62728'),legendgroup = 'Eck',showlegend= False)
trace_Nor = go.Scatter(x = df_Koers.index,y = df_Koers['Nor'],line = dict(color='#2ca02c'),legendgroup = 'Nor', name = 'Nordex',connectgaps=True)
b_Nor = go.Scatter(x = df_Koers.loc[buy_Nor:].index, y = np.ones(df_Koers.loc[buy_Nor:].index.size)*df_Koers.loc[buy_Nor,'Nor'],line = dict(dash='dash',color='#2ca02c'),legendgroup = 'Nor',showlegend= False)
trace_Bas = go.Scatter(x = df_Koers.index,y = df_Koers['Bas'],line = dict(color='#1f77b4'),legendgroup = 'Bas',name = 'BASF',connectgaps=True)
b_Bas = go.Scatter(x = df_Koers.loc[buy_Bas:].index, y = np.ones(df_Koers.loc[buy_Bas:].index.size)*df_Koers.loc[buy_Bas,'Bas'],line = dict(dash='dash',color='#1f77b4'),legendgroup = 'Bas',showlegend= False)
trace_Ves = go.Scatter(x = df_Koers.index,y = df_Koers['Ves'],line = dict(color='#9467bd'),legendgroup = 'Ves',name = 'Vestas',connectgaps=True)
b_Ves = go.Scatter(x = df_Koers.loc[buy_Ves:].index, y = np.ones(df_Koers.loc[buy_Ves:].index.size)*df_Koers.loc[buy_Ves,'Ves'],line = dict(dash='dash',color='#9467bd'),legendgroup = 'Ves',showlegend= False)
trace_Int = go.Scatter(x = df_Koers.index,y = df_Koers['Int'],line = dict(color='#7f7f7f'),legendgroup = 'Int',name = 'InterX',connectgaps=True)
b_Int = go.Scatter(x = df_Koers.loc[buy_Int:].index, y = np.ones(df_Koers.loc[buy_Int:].index.size)*df_Koers.loc[buy_Int,'Int'],line = dict(dash='dash',color='#7f7f7f'),legendgroup = 'Int',showlegend= False)
trace_Can = go.Scatter(x = df_Koers.index,y = df_Koers['Can'],line = dict(color='#ff7f0e'),legendgroup = 'Can',name = 'Candriam',connectgaps=True)
b_Can = go.Scatter(x = df_Koers.loc[buy_Can:].index, y = np.ones(df_Koers.loc[buy_Can:].index.size)*df_Koers.loc[buy_Can,'Can'],line = dict(dash='dash',color='#ff7f0e'),legendgroup = 'Can',showlegend= False)
trace_Rob = go.Scatter(x = df_Koers.index,y = df_Koers['Rob'],line = dict(color='#2ca02c'),legendgroup = 'Rob',name = 'RobAgri',connectgaps=True)
b_Rob = go.Scatter(x = df_Koers.loc[buy_Rob:].index, y = np.ones(df_Koers.loc[buy_Rob:].index.size)*df_Koers.loc[buy_Rob,'Rob'],line = dict(dash='dash',color='#2ca02c'),legendgroup = 'Rob',showlegend= False)
trace_Gee = go.Scatter(x = df_Koers.index,y = df_Koers['Gee'],line = dict(color='#8c564b'),legendgroup = 'Gee',name = 'Geely',connectgaps=True)
b_Gee = go.Scatter(x = df_Koers.loc[buy_Gee:].index, y = np.ones(df_Koers.loc[buy_Gee:].index.size)*df_Koers.loc[buy_Gee,'Gee'],line = dict(dash='dash',color='#8c564b'),legendgroup = 'Gee',showlegend= False)
trace_Sil = go.Scatter(x = df_Koers.index,y = df_Koers['Sil'],line = dict(color='#e377c2'),legendgroup = 'Sil',name = 'Silver',connectgaps=True)
b_Sil = go.Scatter(x = df_Koers.loc[buy_Sil:].index, y = np.ones(df_Koers.loc[buy_Sil:].index.size)*df_Koers.loc[buy_Sil,'Sil'],line = dict(dash='dash',color='#e377c2'),legendgroup = 'Sil',showlegend= False)
trace_VTS = go.Scatter(x = df_Koers.index,y = df_Koers['VTS'],line = dict(color='#bcbd22'),legendgroup = 'VTS',name = 'VTStock',connectgaps=True)
b_VTS = go.Scatter(x = df_Koers.loc[buy_VTS:].index, y = np.ones(df_Koers.loc[buy_VTS:].index.size)*df_Koers.loc[buy_VTS,'VTS'],line = dict(dash='dash',color='#bcbd22'),legendgroup = 'VTS',showlegend= False)
trace_VTB = go.Scatter(x = df_Koers.index,y = df_Koers['VTB'],line = dict(color='#17becf'),legendgroup = 'VTB',name = 'VTBond',connectgaps=True)
b_VTB = go.Scatter(x = df_Koers.loc[buy_VTB:].index, y = np.ones(df_Koers.loc[buy_VTB:].index.size)*df_Koers.loc[buy_VTB,'VTB'],line = dict(dash='dash',color='#17becf'),legendgroup = 'VTB',showlegend= False)

tracer = [trace_Bas, b_Bas, trace_Nor, b_Nor, trace_Eck, b_Eck, trace_Ves, b_Ves, trace_Int, b_Int, trace_Can, b_Can, trace_Rob, b_Rob, trace_Gee, b_Gee, trace_Sil, b_Sil, trace_VTS, b_VTS, trace_VTB, b_VTB]

fig = {'data': tracer}

py.plot(fig, filename='koersen.html')
# py.plot(tracer)


# In[7]:


trace_one = go.Scatter(x = df_NKoers.index, y = np.ones(df_Koers.index.size),line = dict(dash='dash',color='black'),name = 'one')
trace_Eck = go.Scatter(x = df_NKoers.index,y = df_NKoers['Eck'],line = dict(color='#d62728'), name = 'vanEck',connectgaps=True)
trace_Ves = go.Scatter(x = df_NKoers.index,y = df_NKoers['Ves'],line = dict(color='#9467bd'), name = 'Vestas',connectgaps=True)
trace_Bas = go.Scatter(x = df_NKoers.index,y = df_NKoers['Bas'],line = dict(color='#1f77b4'), name = 'BASF',connectgaps=True)
trace_Nor = go.Scatter(x = df_NKoers.index,y = df_NKoers['Nor'],line = dict(color='#2ca02c'), name = 'Nordex',connectgaps=True)
trace_Int = go.Scatter(x = df_NKoers.index,y = df_NKoers['Int'],line = dict(color='#7f7f7f'), name = 'InterX',connectgaps=True)
trace_Can = go.Scatter(x = df_NKoers.index,y = df_NKoers['Can'],line = dict(color='#ff7f0e'), name = 'Candriam',connectgaps=True)
trace_Rob = go.Scatter(x = df_NKoers.index,y = df_NKoers['Rob'],line = dict(color='#2ca02c'), name = 'RobAgri',connectgaps=True)
trace_Gee = go.Scatter(x = df_NKoers.index,y = df_NKoers['Gee'],line = dict(color='#8c564b'), name = 'Geely',connectgaps=True)
trace_Sil = go.Scatter(x = df_NKoers.index,y = df_NKoers['Sil'],line = dict(color='#e377c2'), name = 'Silver',connectgaps=True)
trace_VTS = go.Scatter(x = df_NKoers.index,y = df_NKoers['VTS'],line = dict(color='#bcbd22'), name = 'VTStock',connectgaps=True)
trace_VTB = go.Scatter(x = df_NKoers.index,y = df_NKoers['VTB'],line = dict(color='#17becf'), name = 'VTBond',connectgaps=True)


tracer = [trace_Bas,trace_Eck, trace_Ves,trace_Nor,trace_Int,trace_Can,trace_Rob,trace_Gee,trace_Sil,trace_VTS,trace_VTB,trace_one]

fig = {'data': tracer}

py.plot(fig,filename='koersen_norm.html')

