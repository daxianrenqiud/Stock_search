import numpy as np
import pandas as pd
import pandas_datareader.data as web
import plotly.express as px
import plotly.graph_objects as go
import tushare as ts
import plotly.io as pio

pro = ts.pro_api()

df = pro.daily(ts_code='000037.SZ, 000038.SZ, 000040.SZ, 000032.SZ, 000004.SZ', start_date=None, end_date=None)
stock_data = df.sort_values(by='trade_date')
stock_data['trade_date'] = pd.to_datetime(stock_data['trade_date'])

stock_data= stock_data[['ts_code','close','trade_date']]

# stock_data.columns = ['医药','金融','电信','能源','工业']
print(stock_data)

fig = px.area(stock_data, x='trade_date', y='close', color='ts_code')

fig.update_xaxes(
    title_text = 'Date',
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 7, label = '7D', step = 'day', stepmode = 'backward'),
            dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
            dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
            dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
            dict(count = 2, label = '2Y', step = 'year', stepmode = 'backward'),
            dict(step = 'all')])))

fig.update_yaxes(title_text = 'Close Price')
fig.update_layout(showlegend = True,
    title = {
        'text': 'Area chart by sectors',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
# fig.show()


import datetime
today = datetime.datetime.today()
print(today)
date = today.strftime("%Y%m%d")  # date form to str
print('20'+date)