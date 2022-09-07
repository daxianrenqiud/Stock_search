import plotly.express as px
import pandas as pd
import plotly.offline as py

df = pd.read_excel(r'./big_data.xlsx')
fig = px.treemap(df,
                 path=[px.Constant("Industry Sectors"),'Sectors', 'Company Name', ],  # 指定层次结构，每一个层次都应该是category型的变量
                 values='Total Assets (Billion)',  # 需要聚合的列名
                 color='Change',
                 range_color=[-0.03, 0.03],  # 色彩范围最大最小值
                 hover_data={'Change': ':.2%',
                             'Total Assets (Billion)': ':.2f'},  # 鼠标悬浮显示数据的格式
                 height=1080,
                 width=1920,
                 color_continuous_scale='Geyser',
                 color_continuous_midpoint=0,  # 颜色变化中间值设置为增长率=0
                 )

fig.update_traces(textinfo='label+value', textfont=dict(size=24))  # 显示企业名称和市值，字体24
py.plot(fig, filename='stock.html')
