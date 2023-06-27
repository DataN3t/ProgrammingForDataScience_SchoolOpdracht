## Programming for Data Science - Final Assignment - Trading Bot ##

## Importeren Libraries

import pandas as pd
import backtrader as bt
import matplotlib.pyplot as plt
import numpy as np
import io
import requests

## Loggings na 6e college
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


## Toevoegen Yahoo API data na feedback college 7 ## 
## Op practisch niveau wordt hier in mijn code verder niets mee gedaan ##
## Maar wel om te laten zien dat ik het begrepen heb ##

import yfinance as yf

def yahoo_SP500_Data():
    sp500_yahoo = yf.download('^GSPC', start='2000-01-01', end='2023-06-20')
    print(sp500_yahoo.head())

yahoo_SP500_Data()


## Toevoegen Trading Strategy ## 
## Deze is gebaseerd op de 3 moving averages ##

class ThreeMovingAverages(bt.Strategy):
    params = (("short", 50), ("mid", 100), ("long", 200))

    def __init__(self):
        self.data_close = self.datas[0].close
        self.order = None

        # Moving average indicators
        self.sma_short = bt.indicators.SimpleMovingAverage(self.data_close, period=self.params.short)
        self.sma_mid = bt.indicators.SimpleMovingAverage(self.data_close, period=self.params.mid)
        self.sma_long = bt.indicators.SimpleMovingAverage(self.data_close, period=self.params.long)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                print('BUY EXECUTED, %.2f' % order.executed.price)
            elif order.issell():
                print('SELL EXECUTED, %.2f' % order.executed.price)
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            logging.info('Order Canceled/Margin/Rejected')

        self.order = None

    def next(self):
        if self.order:
            return

        if not self.position:
            if self.sma_short > self.sma_mid and self.sma_short > self.sma_long:
                self.order = self.buy()
        else:
            if self.sma_short < self.sma_mid or self.sma_short < self.sma_long:
                self.order = self.sell()
                

## Aangepaste SP500 data feed ##

class SP500DataFeed(bt.feeds.PandasData):
    lines = ('open', 'high', 'low', 'close', 'adj_close', 'volume')
    params = (
        ('open', 'Open'),
        ('high', 'High'),
        ('low', 'Low'),
        ('close', 'Close'),
        ('adj_close', 'Adj Close'),
        ('volume', 'Volume'),
    )

# Cerebro backtesting broker
cerebro = bt.Cerebro()

## Data transformatie stappen na college 7 en na feedback presentatie ##
## Data transformatie nog niet uitgevoerd op de data ##

url = "https://raw.githubusercontent.com/DataN3t/ProgrammingForDataScience_SchoolOpdracht/main/SPX_data.csv"
s = requests.get(url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')), parse_dates=True, index_col='Date')

data = SP500DataFeed(dataname=df)
print(df.head())
cerebro.adddata(data)

## Data opschonen/transformatie en voorbereiden voor backtrader ##
df_cleaned = df.copy()

df_cleaned.dropna(inplace=True)
# Feature Engineering
df_cleaned['Log_Returns'] = np.log(df_cleaned['Adj Close'] / df_cleaned['Adj Close'].shift(1))
# Normaliseren
df_cleaned['Normalized_Adj_Close'] = df_cleaned['Adj Close'] / max(df_cleaned['Adj Close'])

# Rolling Statistics
window = 21  ## 21 dagen als trading maand##
df_cleaned['Rolling_Mean'] = df_cleaned['Adj Close'].rolling(window=window).mean()

# Filteren op tijd / periode spread zoals aangegeven tijdens college 7
filtered_df = df_cleaned[df_cleaned.index >= '1920-01-01']
print(filtered_df.head())


# Strategie toevoegen aan Cerebro ##

cerebro.addstrategy(ThreeMovingAverages)

# Broker parameters
funnymunnycoins = 1000000 # funny munny coins 

# broker parameters settings 
cerebro.broker.setcash(funnymunnycoins)
cerebro.broker.setcommission(commission=0.0)
cerebro.broker.set_slippage_perc(perc=0, slip_open=True, slip_limit=True, slip_match=True, slip_out=True)
cerebro.broker.set_margin(1.0)
cerebro.addsizer(bt.sizers.AllInSizer)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

results = cerebro.run()
portfolio_value = cerebro.broker.getvalue()
print('Final Portfolio Value: %.2f' % portfolio_value)

cerebro.plot()


