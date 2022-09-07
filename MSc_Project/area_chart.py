import numpy as np
import pandas as pd
import pandas_datareader.data as web
import plotly.express as px
import plotly.graph_objects as go
import tushare as ts
import plotly.io as pio


pro = ts.pro_api()


code_list = ['000037.SZ','000038.SZ', '000040.SZ', '000032.SZ','000004.SZ']

def get_close_data(code_list, start_d= None, end_d=None):
    global stock_data
    # df = ts.get_k_data(code_list[0], ktype='D', start=start_d, end=end_d)
    df = pro.daily(ts_code=code_list[0], start_date=start_d, end_date=end_d)
    stock_data = df[['trade_date']]
    for code in code_list:
        # df = ts.get_k_data(code, ktype='D', start=start_d, end=end_d)
        df = pro.daily(ts_code=code, start_date=start_d, end_date=end_d)
        stock_data.insert(stock_data.columns.size, code, df['close'])
        stock_data[code] = stock_data[code] / max(stock_data[code])
    return stock_data

stock_data = get_close_data(code_list)

# stock_data = stock_data.sort_values(by='trade_date')
stock_data['trade_date'] = pd.to_datetime(stock_data['trade_date'])


stock_data.columns = ['date','Medical','Financial','Telecom','Energy','Industrial']
print(stock_data)
# Area chart
fig = px.area()

fig.add_trace(go.Scatter(
    name='Medical',
    x=stock_data['date'],
    y=stock_data['Medical'],
    mode='lines',
    stackgroup='one',
    groupnorm='percent'   # 重点参数：分组归一化，选择百分比
))

fig.add_trace(go.Scatter(
    name='Financial',
    x=stock_data['date'],
    y=stock_data['Financial'],
    mode='lines',
    stackgroup='one'   # 默认是堆叠分组统计
))

fig.add_trace(go.Scatter(
    name='Telecom',
    x=stock_data['date'],
    y=stock_data['Telecom'],
    mode='lines',
    stackgroup='one'
))

fig.add_trace(go.Scatter(
    name='Energy',
    x=stock_data['date'],
    y=stock_data['Energy'],
    mode='lines',
    stackgroup='one'
))

fig.add_trace(go.Scatter(
    name='Industrial',
    x=stock_data['date'],
    y=stock_data['Industrial'],
    mode='lines',
    stackgroup='one'
))

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
    yaxis=dict(ticksuffix='%'),
    title = {
        'text': 'Area chart by sectors',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

fig.show()