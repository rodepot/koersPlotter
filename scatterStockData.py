
import plotly.graph_objs as go
import numpy as np

def scatterStockData(stockData,stockName,stockColor):
    dataScatter = go.Scatter(x = stockData.index,y = stockData[stockName],line = dict(color=stockColor), legendgroup = stockName, name = stockName, connectgaps=True)    
    return dataScatter

def scatterStockBuy(stockData,stockName,buyDate,stockColor):
    dataScatter = go.Scatter(x = stockData.loc[buyDate:].index, y = np.ones(stockData.loc[buyDate:].index.size)*stockData.loc[buyDate,stockName],line = dict(dash='dash',color=stockColor),legendgroup = stockName,showlegend= False)
    return dataScatter

def scatterUnity(stockData):
    dataScatter = go.Scatter(x = stockData.index, y = np.ones(stockData.index.size),line = dict(dash='dash',color='black'),name = 'one')
    return dataScatter
