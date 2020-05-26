
# coding: utf-8

# Dit notebook haalt de koersen van onze aandelen binnen en laat deze met interactieve grafieken zien

# # Data binnen halen en verwerken

# 20180603 JWW Cleaned up a bit 

# In[1]:

import pandas as pd
import plotly.offline as py
from getStockData import read_stock
import datetime
from scatterStockData import scatterStockData, scatterStockBuy, scatterUnity

# In[2]:
baseURLohlcv = 'http://tools.morningstar.nl/api/rest.svc/timeseries_ohlcv/8qe8f2nger?currencyId=EUR&idtype=Morningstar&frequency=daily&startDate=2008-01-01&performanceType=&outputType=COMPACTJSON&'
baseURLprice = 'http://tools.morningstar.nl/api/rest.svc/timeseries_price/8qe8f2nger?currencyId=EUR&idtype=Morningstar&frequency=daily&startDate=2008-01-01&priceType=&outputType=COMPACTJSON&'

url_Nor = 'id=0P00009QWG]3]0]E0WWE$$ALL'
url_Ves = 'id=0P0000BHUH]3]0]E0WWE$$ALL'
url_Bas = 'id=0P0000GGBW]3]0]E0WWE$$ALL'
url_Int = 'id=0P0000S9DK]3]0]E0WWE$$ALL'
url_Gee = 'id=0P0000CJJC]3]0]E0WWE$$ALL'
url_Coo = 'id=0P000001HE]3]0]E0WWE$$ALL'
url_Eck = 'id=0P0000U0D2]2]0]ETALL$$ALL'
url_Can = 'id=F00000QU91]2]0]ETALL$$ALL'
url_Rob = 'id=F00000QDBO]2]0]ETALL$$ALL'
url_Sil = 'id=0P0000I5NQ]2]0]ETALL$$ALL'
url_VTS = 'id=0P00002DAJ]2]0]ETALL$$ALL'
url_VTB = 'id=0P0000896G]2]0]ETALL$$ALL'
url_Gol = 'id=0P00002DCW]2]0]ETALL$$ALL'
url_VAP = 'id=0P0000Z13D]2]0]ETALL$$ALL'
url_EAS = 'id=0P0000MM6D]2]0]ETALL$$ALL'

stock = [
        ['BASF','2015-08-18',baseURLohlcv+url_Bas,'ohlcv','#d62728'],
        ['InterX','2016-10-24',baseURLohlcv+url_Int,'ohlcv','#9467bd'],
        ['Nordex','2017-02-16',baseURLohlcv+url_Nor,'ohlcv','#1f77b4'],
        ['Vestas','2017-02-16',baseURLohlcv+url_Ves,'ohlcv','#17becf'], 
        ['Geely','2017-11-21',baseURLohlcv+url_Gee,'ohlcv','#2ca02c'],
        ['Cooper','2018-06-07',baseURLohlcv+url_Coo,'ohlcv','#cca0cc'], 
        ['vanEck','2017-03-23',baseURLprice+url_Eck,'price','#7f7f7f'],
        ['Candriam','2015-04-13',baseURLprice+url_Can,'price','#ff7f0e'],
        ['RobAgri','2015-06-26',baseURLprice+url_Rob,'price','#2ca02c'],
        ['Silver','2015-05-22',baseURLprice+url_Sil,'price','#8c564b'],
        ['VTStock','2016-03-31',baseURLprice+url_VTS,'price','#e377c2'],
        ['VTBond','2016-03-31',baseURLprice+url_VTB,'price','#bcbd22'],  
        ['Gold','2018-08-31',baseURLprice+url_Gol,'price','#ac1d22'],
        ['VAsiaPac','2018-12-24',baseURLprice+url_VAP,'price','#a01de2'],	
        ]

stock = [
        ['BASF','2015-08-18',baseURLprice+url_Bas,'price','#d62728'],
#        ['InterX','2016-10-24',baseURLprice+url_Int,'price','#9467bd'],
        ['Nordex','2017-02-16',baseURLprice+url_Nor,'price','#1f77b4'],
        ['Vestas','2017-02-16',baseURLprice+url_Ves,'price','#17becf'],
        ['Geely','2017-11-21',baseURLprice+url_Gee,'price','#2ca02c'],
        ['Cooper','2018-06-07',baseURLprice+url_Coo,'price','#cca0cc'],
        ['vanEck','2017-03-23',baseURLprice+url_Eck,'price','#7f7f7f'],
        ['Candriam','2015-04-13',baseURLprice+url_Can,'price','#ff7f0e'],
        ['RobAgri','2015-06-26',baseURLprice+url_Rob,'price','#2ca02c'],
        ['Silver','2015-05-22',baseURLprice+url_Sil,'price','#8c564b'],
        ['VTStock','2016-03-31',baseURLprice+url_VTS,'price','#e377c2'],
        ['VTBond','2016-03-31',baseURLprice+url_VTB,'price','#bcbd22'],
        ['Gold','2018-08-31',baseURLprice+url_Gol,'price','#ac1d22'],
        ['VAsiaPac','2018-12-24',baseURLprice+url_VAP,'price','#a01de2'],
        ['EasyJet','2020-05-14',baseURLprice+url_EAS,'price','#9467bd'],
        ]

investments = {
        'BASF':{'datum_aankoop':'2015-08-18','url_morningstar':url_Bas,'color':'#d62728'},
#        'InterX':{'datum_aankoop':'2016-10-24','url_morningstar':url_Int,'color':'#9467bd'},
        'Nordex':{'datum_aankoop':'2017-02-16','url_morningstar':url_Nor,'color':'#1f77b4'},
        'Vestas':{'datum_aankoop':'2017-02-16','url_morningstar':url_Ves,'color':'#17becf'},
        'Geely':{'datum_aankoop':'2017-11-21','url_morningstar':url_Gee,'color':'#2ca02c'},
        'Cooper':{'datum_aankoop':'2018-06-07','url_morningstar':url_Coo,'color':'#cca0cc'},
        'vanEck':{'datum_aankoop':'2017-03-23','url_morningstar':url_Eck,'color':'#7f7f7f'},
        'Candriam':{'datum_aankoop':'2015-04-13','url_morningstar':url_Can,'color':'#ff7f0e'},
        'RobAgri':{'datum_aankoop':'2015-06-26','url_morningstar':url_Rob,'color':'#2ca02c'},
        'Silver':{'datum_aankoop':'2015-05-22','url_morningstar':url_Sil,'color':'#8c564b'},
        'VTStock':{'datum_aankoop':'2016-03-31','url_morningstar':url_VTS,'color':'#e377c2'},
        'VTBond':{'datum_aankoop':'2016-03-31','url_morningstar':url_VTB,'color':'#bcbd22'},
        'Gold':{'datum_aankoop':'2018-08-31','url_morningstar':url_Gol,'color':'#ac1d22'},
        'VAsiaPac':{'datum_aankoop':'2018-12-24','url_morningstar':url_VAP,'color':'#a01de2'},
        'EasyJet':{'datum_aankoop':'2020-05-14','url_morningstar':url_EAS,'color':'#9467bd'},
        }

today = str(datetime.date.today())
ytd = str(datetime.date.today() - datetime.timedelta(12*365/12))


# In[3]: Get all data and put it in one variable (df_Koers)

df_Koers = pd.DataFrame()
#loop over stocks
for stock in investments:
    df_Koers = df_Koers.combine_first(read_stock(stock, investments[stock]))


# In[5]: Normalize data to date of purchase

df_NKoers = df_Koers.copy()
df_DKoers = df_Koers.copy()

#loop over stocks
for stock in investments:
    # TODO: drop_na()
    df_NKoers[stock] /= df_Koers.loc[investments[stock]['datum_aankoop'],stock]
    print('Normalizing stock: {}'.format(stock))
    laatsteKoers = df_Koers.iloc[-1,df_Koers.columns.get_loc(stock)]
    if laatsteKoers > 0:
        pass
    else:
        laatsteKoers = df_Koers.iloc[-2,df_Koers.columns.get_loc(stock)]
    print('Last close: {}\n'.format(laatsteKoers))
    df_DKoers[stock] /= laatsteKoers

# In[6]: Plot all stock data and write to HTML
    
# De  grafiek laat de koersen zien met een horizontale lijn en verticale lijn bij aankoop. 

tracer = []
#loop over stocks
print('Generating "./html/koersen.html" and "./html/log_koersen.html"')
for stock in investments:
    print('\t{}'.format(stock))
    tracer.append(scatterStockData(df_Koers,stock,investments[stock]['color']))
    tracer.append(scatterStockBuy(df_Koers,stock,investments[stock]['datum_aankoop'],investments[stock]['color'])) 

fig = {'data': tracer, 'layout': {
        'xaxis': {'title': 'Datum', 'range': [ytd,today]},
        'yaxis': {'title': 'Koers [EUR]', 'type': 'linear'}
    }}

py.plot(fig, filename='./html/koersen.html')

fig = {'data': tracer, 'layout': {
        'xaxis': {'title': 'Datum', 'range': [ytd,today]},
        'yaxis': {'title': 'Koers [EUR]', 'type': 'log'}
    }}

py.plot(fig, filename='./html/log_koersen.html')


# In[7]: Plot the normalized data
# De grafiek laat de koersen zien, maar deze zijn naar 1 genormaliseerd op het moment van aankoop

tracer = []
#loop over stocks
print('Generating "./html/koersen_norm.html" and "./html/log_koersen_norm.html"')
for stock in investments:
    print('\t{}'.format(stock))
    tracer.append(scatterStockData(df_NKoers,stock,investments[stock]['color']))
#scatter a line at unity
tracer.append(scatterUnity(df_NKoers))

fig = {'data': tracer, 'layout': {
        'xaxis': {'title': 'Datum', 'range': [ytd,today]},
        'yaxis': {'title': 'Koers aankoop genormaliseerd [-]', 'type': 'linear'}
    }}

py.plot(fig,filename='./html/koersen_norm.html')

fig = {'data': tracer, 'layout': {
        'xaxis': {'title': 'Datum', 'range': [ytd,today]},
        'yaxis': {'title': 'Koers aankoop genormaliseerd [-]', 'type': 'log'}
    }}

py.plot(fig,filename='./html/log_koersen_norm.html')

# In[7]: Plot the normalized data
# De grafiek laat de koersen zien, maar deze zijn naar 1 genormaliseerd op het moment van aankoop

tracer = []
#loop over stocks
print('Generating "./html/koersen_norm_sluit.html" and "./html/log_koersen_norm_sluit.html"')
for stock in investments:
    print('\t{}'.format(stock))
    tracer.append(scatterStockData(df_DKoers,stock,investments[stock]['color']))
#scatter a line at unity
tracer.append(scatterUnity(df_DKoers))

fig = {'data': tracer, 'layout': {
        'xaxis': {'title': 'Datum', 'range': [ytd,today]},
        'yaxis': {'title': 'Koers sluit genormaliseerd [-]', 'type': 'linear'}
    }}

py.plot(fig,filename='./html/koersen_norm_sluit.html')

fig = {'data': tracer, 'layout': {
        'xaxis': {'title': 'Datum', 'range': [ytd,today]},
        'yaxis': {'title': 'Koers sluit genormaliseerd [-]', 'type': 'log'}
    }}

py.plot(fig,filename='./html/log_koersen_norm_sluit.html')

