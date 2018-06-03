
# coding: utf-8

# Dit notebook haalt de koersen van onze aandelen binnen en laat deze met interactieve grafieken zien

# # Data binnen halen en verwerken

# 20180603 JWW Cleaned up a bit 

# In[1]:


import plotly.offline as py

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

stock = [
        ['BASF','2015-08-18',url_Bas,'ohlcv','#d62728'],
        ['InterX','2016-10-24',url_Int,'ohlcv','#9467bd'],
        ['Nordex','2017-02-16',url_Nor,'ohlcv','#1f77b4'],
        ['Vestas','2017-02-16',url_Ves,'ohlcv','#17becf'], 
        ['Geely','2017-11-21',url_Gee,'ohlcv','#2ca02c'],
        ['vanEck','2017-03-23',url_Eck,'price','#7f7f7f'],
        ['Candriam','2015-04-13',url_Can,'price','#ff7f0e'],
        ['RobAgri','2015-06-26',url_Rob,'price','#2ca02c'],
        ['Silver','2015-05-22',url_Sil,'price','#8c564b'],
        ['VTStock','2016-03-31',url_VTS,'price','#e377c2'],
        ['VTBond','2016-03-31',url_VTB,'price','#bcbd22'],   
        ]



# In[3]: Get all data and put it in one variable (df_Koers)
from getStockData import read_stock

ii = 0
df_Koers = read_stock(stock[ii][0],stock[ii][2],stock[ii][3])
#loop over remaining stocks
for ii in range(1,len(stock)):
    df_Koers = df_Koers.combine_first(read_stock(stock[ii][0],stock[ii][2],stock[ii][3]))


# In[5]: Normalize data to date of purchase

df_NKoers = df_Koers.copy()
#loop over stocks
for ii in range(0,len(stock)):
    df_NKoers[stock[ii][0]] /= df_Koers.loc[stock[ii][1],stock[ii][0]]



# In[6]: Plot all stock data and write to HTML
    
from scatterStockData import scatterStockData, scatterStockBuy, scatterUnity
# De  grafiek laat de koersen zien met een horizontale lijn en verticale lijn bij aankoop. 

tracer = []
#loop over stocks
for ii in range(0,len(stock)):
    tracer.append(scatterStockData(df_Koers,stock[ii][0],stock[ii][4]))
    tracer.append(scatterStockBuy(df_Koers,stock[ii][0],stock[ii][1],stock[ii][4])) 

fig = {'data': tracer}

py.plot(fig, filename='koersen.html')



# In[7]: Plot the normalized data
# De grafiek laat de koersen zien, maar deze zijn naar 1 genormaliseerd op het moment van aankoop

tracer = []
#loop over stocks
for ii in range(0,len(stock)):
    tracer.append(scatterStockData(df_NKoers,stock[ii][0],stock[ii][4]))
#scatter a line at unity
tracer.append(scatterUnity(df_NKoers))

fig = {'data': tracer}

py.plot(fig,filename='koersen_norm.html')
