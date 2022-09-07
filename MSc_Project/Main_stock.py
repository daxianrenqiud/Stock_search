import tushare as ts
import sys
import re
import matplotlib.pyplot as plt
import datetime
import json
import webbrowser
import plotly.express as px
import pandas as pd
import plotly.offline as py
import plotly.io as pio
import plotly.graph_objects as go
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from stock_interface import Ui_MainWindow
from multiple import *
from index import *
from urllib import request, parse
from functools import partial
from pyecharts.charts import Map
from pyecharts import options as opts


def translate(i):
    """
    This is a translation function
    :param i: Text to be translated
    :return: Text after translation
    """
    req_url = 'http://fanyi.youdao.com/translate'  # Create connection interfaces
    # Create the data to be submitted
    Form_Date = {'i': i, 'doctype': 'json', 'form': 'AUTO', 'to': 'AUTO', 'smartresult': 'dict',
                 'client': 'fanyideskweb', 'salt': '1526995097962', 'sign': '8e4c4765b52229e1f3ad2e633af89c76',
                 'version': '2.1', 'keyform': 'fanyi.web', 'action': 'FY_BY_REALTIME', 'typoResult': 'false'}

    data = parse.urlencode(Form_Date).encode('utf-8')  # Data conversion
    response = request.urlopen(req_url, data)  # Submit data and parse
    html = response.read().decode('utf-8')  # Server return results read
    translate_results = json.loads(html)  # Load in json format
    translate_results = translate_results['translateResult'][0][0]['tgt']  # json format retrieval
    return translate_results


# Individual stock visualisation
def process_data(code, start_d, end_d):
    """
    Get and process data function
    :param code: Stock code to be searched
    :param start_d: Start date
    :param end_d: End date
    :return: Complete sorted data by date format
    """
    df = pro.daily(ts_code=code, start_date=start_d, end_date=end_d)  # get data
    # Processing date formats and sorting
    df = df.sort_values(by='trade_date')
    df['trade_date'] = pd.to_datetime(df['trade_date'])
    df.set_index("trade_date", inplace=True)
    return df


def show_profit(code, start_d, end_d):
    """
    This function visualises the profit of a individual function
    :param code: Stock code to be searched
    :param start_d: Start date
    :param end_d: End date
    :return: Profit Line Chart
    """
    df = process_data(code, start_d, end_d)  # Get the completed processing data
    df['earn_rate'] = df['close'].pct_change()
    # Setting the plotting parameters
    plt.figure(figsize=(10, 5))
    plt.title('Daily earn rate')
    plt.xlabel('Data')
    plt.ylabel('earn_rate')
    plt.plot(df['earn_rate'], label='earn_rate')
    plt.grid(True)
    plt.legend()
    plt.savefig('./images/earn_rate.jpg')


def show_volume(code, start_d, end_d):
    """
    This function visualises the volume of a individual function
    :param code: Stock code to be searched
    :param start_d: Start date
    :param end_d: End date
    :return: Volume Line Chart
    """
    df = process_data(code, start_d, end_d)  # Get the completed processing data
    # Setting the plotting parameters
    plt.figure(figsize=(10, 5))
    plt.title('Daily Volume')
    plt.xlabel('Data')
    plt.ylabel('Volume')
    plt.plot(df['vol'], label='volume')
    plt.grid(True)
    plt.legend()
    plt.savefig('./images/volume.jpg')


def show_close(code, start_d, end_d):
    """
    This function visualises the closing price of a individual function
    :param code: Stock code to be searched
    :param start_d: Start date
    :param end_d: End date
    :return: Closing price Line Chart
    """
    df = process_data(code, start_d, end_d)  # Get the completed processing data
    # Setting the plotting parameters
    plt.figure(figsize=(10, 5))
    plt.title('Closing Price')
    plt.xlabel('Data')
    plt.plot(df['close'], label='close')
    plt.grid(True)
    plt.legend()
    plt.savefig('./images/close.jpg')


def show_closing(code, start_d, end_d):
    """
    This function visualises the closing price and company information of a individual function
    :param code: Stock code to be searched
    :param start_d: start date
    :param end_d: end date
    :return: Closing price Line Chart and company information data
    """
    df = process_data(code, start_d, end_d)  # Get the completed processing data
    # Get company information data
    company = pro.stock_company(exchange='', ts_code=code,
                                fields='ts_code,province,city,main_business,business_scope')
    # Setting the plotting parameters
    plt.figure(figsize=(10, 5))
    plt.title('Daily Closing Price')
    plt.xlabel('Data')
    plt.ylabel('closing')
    plt.plot(df['close'], label='close')
    plt.grid(True)
    plt.legend()
    plt.savefig('./images/close.jpg')
    # process company information data
    com_data = company.values.tolist()
    str(com_data)
    return com_data


def show_hl(code, start_d, end_d):
    """
    This function visualises the highest price and lowest price of a individual function
    :param code: Stock code to be searched
    :param start_d: Start date
    :param end_d: End date
    :return: highest price and lowest price Line Chart
    """
    df = process_data(code, start_d, end_d)  # Get the completed processing data
    # Setting the plotting parameters
    plt.figure(figsize=(10, 5))
    plt.title('Daily highest and lowest price')
    plt.xlabel('Data')
    plt.ylabel('Price')
    plt.plot(df['high'], c='r', label='high')
    plt.plot(df['low'], c='g', label='low')
    plt.grid(True)
    plt.legend()
    plt.savefig('./images/HL.jpg')


def show_oc(code, start_d, end_d):
    """
    This function visualises the opening price and closing price of a individual function
    :param code: Stock code to be searched
    :param start_d: Start date
    :param end_d: End date
    :return: opening price and closing price Line Chart
    """
    df = process_data(code, start_d, end_d)  # Get the completed processing data
    # Setting the plotting parameters
    plt.figure(figsize=(10, 5))
    plt.title('Daily opening and closing price')
    plt.xlabel('Data')
    plt.ylabel('Price')
    plt.plot(df['open'], c='m', label='open')
    plt.plot(df['close'], c='c', label='close')
    plt.grid(True)
    plt.legend()
    plt.savefig('./images/OC.jpg')


def show_today(code):
    """
    This is a function that visualises the real-time closing price of a stock
    :param code: Stock code to be searched
    :return: Today's real-time closed price line chart
    """
    code = re.sub("\D", "", code)  # Adjust the code format
    start_date = datetime.datetime.now().strftime('%Y-%m-%d')  # Adjust the date format
    df = ts.get_hist_data(code, ktype='15', start=start_date)  # Get real-time data
    df = df.sort_values(by='date')  # Sort by date
    # Setting the plotting parameters
    plt.figure(figsize=(15, 5))
    plt.title('Today Price')
    plt.plot(df['close'], label='close')
    plt.grid(True)
    plt.legend()
    plt.gcf().autofmt_xdate()
    plt.savefig('./images/today.jpg')


# Multiple stock visualisation
def get_close_data(code_list, start_d, end_d):
    """
    This is a function that gets the closing price of multiple stocks
    :param code_list: List of stocks to be searched
    :param start_d: Start date
    :param end_d: End date
    :return: Data for multiple stock closing prices
    """
    global stock_data
    df = pro.daily(ts_code=code_list[0], start_date=start_d, end_date=end_d)  # Get data
    stock_data = df[['trade_date']]  # Create data only date
    # Loop to add multiple stocks at normalised closing prices
    for code in code_list:
        df = pro.daily(ts_code=code, start_date=start_d, end_date=end_d)
        stock_data.insert(stock_data.columns.size, code, df['close'])
        stock_data[code] = stock_data[code] / max(stock_data[code])  # normalisation
    return stock_data


def close_image(code_list):
    """
    This is a function that plots the closing price of multiple stocks on a line chart
    :param code_list: List of stocks to plot
    :return: Multiple stock closing price line chart
    """
    # Setting the plotting parameters
    plt.figure(figsize=(10, 5))
    plt.title('Price Proportion Comparsion')
    plt.xlabel('Date')
    plt.ylabel('Price Proportion')
    stock_data['trade_date'] = pd.to_datetime(stock_data['trade_date'])
    # Loop plotting
    for code in code_list:
        plt.plot(stock_data['trade_date'], stock_data[code], label=code)
    plt.grid(True)
    plt.legend()
    plt.savefig('./images/mutiple_price.jpg')


def get_earn_data(code_list, start_d, end_d):
    """
    This is a function that gets the earn data of multiple stocks
    :param code_list: List of stocks to be searched
    :param start_d: Start date
    :param end_d: End date
    :return: Data for multiple stock earn rate
    """
    global earn_data
    df = pro.daily(ts_code=code_list[0], start_date=start_d, end_date=end_d)  # Get data
    earn_data = df[['trade_date']]  # Create data only date
    # Loop to add multiple stock earn rate
    for code in code_list:
        df = pro.daily(ts_code=code, start_date=start_d, end_date=end_d)
        earn_data.insert(earn_data.columns.size, code, df['close'].pct_change())  # Add the earn rate
    return earn_data


def earn(code_list):
    """
    This is a function that processes data, sorted by earning rate
    :param code_list: List of stocks to be searched
    :return: Data sorted by earn rate
    """
    meanlist = []
    # Loop to add earn rate
    for code in code_list:
        m = stock_data[code].mean()
        meanlist.append([code, m])
    # For loop to sort data by earn rate
    for index in range(1, len(meanlist)):
        i = index - 1
        while i >= 0 and (meanlist[index][1] < meanlist[i][1]):
            meanlist[i + 1], meanlist[i] = meanlist[i], meanlist[index]
            i = i - 1
    return meanlist


def earn_image(code_list):
    """
    This is a function that plots a line graph of the earned rate
    :param code_list: List of stocks to be searched
    :return: Earn rate line graph
    """
    # Setting the plotting parameters
    plt.figure(figsize=(10, 5))
    plt.title('Yield Comparison')
    plt.xlabel('Date')
    plt.ylabel('Yield')
    earn_data['trade_date'] = pd.to_datetime(earn_data['trade_date'])
    # Loop plotting
    for code in code_list:
        plt.plot(earn_data['trade_date'], earn_data[code], label=code)
    plt.grid(True)
    plt.legend()
    plt.savefig('./images/mutiple_earn.jpg')


def color_image(code_list):
    """
    This is a function that plots multiple stock closing prices with colour mapping
    :param code_list: List of stocks to be searched
    :return: Closing price line chart with colour mapping for multiple stocks
    """
    # Setting the plotting parameters
    plt.figure(figsize=(10, 5))
    plt.title('Color Price Proportion Comparsion')
    plt.xlabel('Date')
    plt.ylabel('Price Proportion')
    stock_data['trade_date'] = pd.to_datetime(stock_data['trade_date'])
    newlist = earn(code_list)
    colorlist = ['r', 'm', 'b', 'c', 'g']  # Create color list
    plotlst = []
    # Create a list, add stocks and colours to be ploted in order of earn rate
    for i in newlist:
        for j in i:
            if type(j) is str:
                plotlst.append(j)
    for c in colorlist:
        plotlst.append(c)
    # Plotted in descending order of earn rate.
    for code in range(0, len(newlist)):
        if code > 0 and code == len(plotlst) - 1:
            plt.plot(stock_data['trade_date'], stock_data[plotlst[code]], label=plotlst[code], color='g')
        else:
            plt.plot(stock_data['trade_date'], stock_data[plotlst[code]], label=plotlst[code], color=colorlist[code])
    plt.grid(True)
    plt.legend()
    plt.savefig('./images/color_price.jpg')


def show_treemap():
    """
    This is a function that plots the stock market Treemap
    :return: Stock market Treemap(html)
    """
    big_data = pd.read_excel(r'./big_data.xlsx')
    fig = px.treemap(big_data,
                     path=['Sectors', 'Company Name', ],
                     # Specify the hierarchy, each level should be a category type variable
                     values='Total Assets (Billion)',  # Name of column to be aggregated
                     color='Change',
                     range_color=[-0.05, 0.05],  # Colour range max. min.
                     hover_data={'Change': ':.2%',
                                 'Total Assets (Billion)': ':.2f'},  # Format of mouse hover display data
                     height=1080,
                     width=1920,
                     color_continuous_scale='Geyser',
                     color_continuous_midpoint=0,  # The middle value of the colour change is set to the growth rate=0
                     )
    fig.update_traces(textinfo='label+value', textfont=dict(size=24))  # Show business name and market value，24
    py.plot(fig, filename='stock.html')
    pio.write_image(fig, './images/treemap.jpg')


def create_map():
    """
    This is a function that maps the industry distribution
    :return:  Industry map(heml)
    """
    # Create and add data by industry
    Finance = [['北京', 1], ['安徽', 1]]
    Industrial = [['天津', 3], ['河北', 3], ['山西', 3], ['辽宁', 3], ['黑龙江', 3],
                  ['上海', 3], ['福建', 3], ['江西', 3], ['河南', 3], ['湖北', 3],
                  ['青海', 3]]
    Manufacturing = [['内蒙古', 5], ['江苏', 5], ['浙江', 5], ['广东', 5]]
    Agriculture = [['吉林', 7], ['山东', 7], ['广西', 7], ['贵州', 7], ['西藏', 7],
                   ['陕西', 7], ['甘肃', 7], ['宁夏', 7], ['新疆', 7]]
    Tourism = [['湖南', 9], ['海南', 9], ['重庆', 9], ['四川', 9], ['云南', 9]]
    (  # Create a map and add the data to be drawn
        Map(opts.InitOpts(width='2060px', height='860px'))
            .add(series_name="Industry Map", data_pair=Finance, maptype="china", )
            .add(series_name="Industry Map", data_pair=Industrial, maptype="china", )
            .add(series_name="Industry Map", data_pair=Manufacturing, maptype="china", )
            .add(series_name="Industry Map", data_pair=Agriculture, maptype="china", )
            .add(series_name="Industry Map", data_pair=Tourism, maptype="china", )
            # Global configuration items
            .set_global_opts(title_opts=opts.TitleOpts(title="Industry Map"),
                             # Setting the standard display
                             visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                               pieces=[{"min": 1, "max": 2, "label": 'Finance'},
                                                                       {"min": 3, "max": 4, "label": 'Industrial'},
                                                                       {"min": 5, "max": 6, "label": 'Manufacturing'},
                                                                       {"min": 7, "max": 8, "label": 'Agriculture'},
                                                                       {"min": 9, "max": 10, "label": 'Tourism'}]), )
            # Series configuration items
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False), )  # Label name display, default is True
            .render("IndustryMap.html")  # Generate local html files
    )
    webbrowser.open("IndustryMap.html")

def show_areachart():
    """
    This is a function that creates an area chart for sectors
    :return: Area chart(html)
    """
    # Obtaining and processing data from various industries
    stock_data = get_close_data(['000037.SZ', '000038.SZ', '000040.SZ', '000032.SZ', '000004.SZ'], None, None)
    stock_data['trade_date'] = pd.to_datetime(stock_data['trade_date'])
    stock_data.columns = ['date', 'Medical', 'Financial', 'Telecom', 'Energy', 'Industrial']
    # Area chart
    fig = px.area()
    # Set the parameters and add the data for each sector to be plotted
    fig.add_trace(go.Scatter(name='Medical', x=stock_data['date'],
                             y=stock_data['Medical'],
                             stackgroup='one'))  # Default is stacked group statistics)) groupnorm='percent'
    fig.add_trace(go.Scatter(name='Financial', x=stock_data['date'],
                             y=stock_data['Financial'], stackgroup='one'))
    fig.add_trace(go.Scatter(name='Telecom', x=stock_data['date'],
                             y=stock_data['Telecom'], stackgroup='one'))
    fig.add_trace(go.Scatter(name='Energy', x=stock_data['date'],
                             y=stock_data['Energy'], stackgroup='one'))
    fig.add_trace(go.Scatter(name='Industrial', x=stock_data['date'],
                             y=stock_data['Industrial'], stackgroup='one'))
    # Add date range button
    fig.update_xaxes(
        title_text='Date',
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=7, label='7D', step='day', stepmode='backward'),
                dict(count=1, label='1M', step='month', stepmode='backward'),
                dict(count=6, label='6M', step='month', stepmode='backward'),
                dict(count=1, label='1Y', step='year', stepmode='backward'),
                dict(count=2, label='2Y', step='year', stepmode='backward'),
                dict(step='all')])))

    fig.update_yaxes(title_text='Closing Price')
    # Setting the layout
    fig.update_layout(showlegend=True,
                      title={
                          'text': 'Area chart by sectors',
                          'y': 0.95,
                          'x': 0.5,
                          'xanchor': 'center',
                          'yanchor': 'top'})

    py.plot(fig, filename='areachart.html')


# Main user interface
class Interface(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        """ Initialise the interface and make the button binding function """
        super(Interface, self).__init__(parent)
        self.completer = QCompleter(items_list)
        self.setupUi(self)
        self.search.clicked.connect(self.closing)

        self.volume.clicked.connect(partial(self.search_info, 0))
        self.rate.clicked.connect(partial(self.search_info, 1))
        self.hl.clicked.connect(partial(self.search_info, 2))
        self.oc.clicked.connect(partial(self.search_info, 3))
        self.today.clicked.connect(partial(self.search_info, 4))

        self.oned.clicked.connect(partial(self.timeinterval, 1))
        self.fived.clicked.connect(partial(self.timeinterval, 5))
        self.onem.clicked.connect(partial(self.timeinterval, 30))
        self.sixm.clicked.connect(partial(self.timeinterval, 180))
        self.oney.clicked.connect(partial(self.timeinterval, 365))
        self.twoy.clicked.connect(partial(self.timeinterval, 730))
        self.fivey.clicked.connect(partial(self.timeinterval, 1825))
        self.max.clicked.connect(partial(self.timeinterval, 0))

        self.industrymap.clicked.connect(create_map)
        self.treemap.clicked.connect(show_treemap)
        self.areachart.clicked.connect(show_areachart)
        self.init_lineedit()
        self.exit.clicked.connect(self.close)


    def printf(self, mes):
        """
        This is the function that prints the company information to the interface
        :param mes: Information to be printed
        :return: Information is presented in the textbrower control
        """
        mes = ' ' * 250 + mes
        self.textBrowser.append(mes)
        self.cursot = self.textBrowser.textCursor()  # Binding textbrowser control
        self.textBrowser.moveCursor(self.cursot.End)

    def init_lineedit(self):
        """
        This is a function that sets the stock code to auto-completion
        :return: Autocomplete with lineedit
        """
        # Setting the matching mode There are three：
        # Qt.MatchStartsWith Beginning match (default)
        # self.completer.setFilterMode(Qt.MatchContains)
        # Set complementary mode
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        # Setting complements to lineedit
        self.code.setCompleter(self.completer)

    def datecalculator(self, date, n):
        """
        This is a function to calculate the date
        :param date: Date to be calculated
        :param n: Number of days to be counted
        :return: Date after calculation
        """
        date = datetime.datetime.strptime(date, "%Y%m%d")  # str to date format
        date = date + datetime.timedelta(days=-n)
        date = date.strftime("%Y%m%d")  # date form to str
        return date

    def timeinterval(self, n):
        """
        A function that controls the date range
        :param n: Determine if the date is set
        :return: Implement date range buttons to control the date of the displayed
        """
        code = self.code.text()
        if n == 0:
            show_close(code, start_d=None, end_d=None)
            self.label.setPixmap(QPixmap("./images/close.jpg"))
            self.label.setScaledContents(True)  # Image size to fit label
        else:
            # When the end date is None
            if len(self.end.text()) == 0:
                today = datetime.datetime.today()
                end_d = today.strftime('%y%m%d')
                start_d = today + datetime.timedelta(days=-n)
                start_d = start_d.strftime("%Y%m%d")
            else:
                end_d = self.end.text()
                start_d = self.datecalculator(self.end.text(), n)
            show_close(code, start_d, end_d)
            self.label.setPixmap(QPixmap("./images/close.jpg"))
            self.label.setScaledContents(True)  # Image size to fit label

    def closing(self):
        """
        This is a function that displays a closed price line chart of a stock to the interface
        :return: The interface shows the closing price and company information
        """
        code = self.code.text()
        start_d = self.start.text()
        end_d = self.end.text()
        company = show_closing(code, start_d, end_d)
        company = translate(company)
        self.label.setPixmap(QPixmap("./images/close.jpg"))
        self.label.setScaledContents(True)  # Image size to fit label
        self.printf(company)

    def search_info(self, n):
        """
        This is a function that visualises a individual stock in the interface
        :param n: Determine which line graph to display
        :return: Various line graphs
        """
        code = self.code.text()
        start_d = self.start.text()
        end_d = self.end.text()
        self.label.setScaledContents(True)  # Image size to fit label
        if n == 0:
            show_volume(code, start_d, end_d)
            self.label.setPixmap(QPixmap("./images/volume.jpg"))
        if n == 1:
            show_profit(code, start_d, end_d)
            self.label.setPixmap(QPixmap("./images/earn_rate.jpg"))
        if n == 2:
            show_hl(code, start_d, end_d)
            self.label.setPixmap(QPixmap("./images/hl.jpg"))
        if n == 3:
            show_oc(code, start_d, end_d)
            self.label.setPixmap(QPixmap("./images/oc.jpg"))
        if n == 4:
            show_today(code)
            self.label.setPixmap(QPixmap("./images/today.jpg"))


# Index search interface by sector
class Index(QWidget, Ui_Index_Form):
    def __init__(self):
        """ Initialise the interface and make the button binding function """
        super(Index, self).__init__()
        self.setupUi(self)
        self.SSE100I.clicked.connect(partial(self.table_data, 0))
        self.SSECS.clicked.connect(partial(self.table_data, 1))
        self.SSEINT.clicked.connect(partial(self.table_data, 2))
        self.SSEHC.clicked.connect(partial(self.table_data, 3))
        self.SSEMT.clicked.connect(partial(self.table_data, 4))
        self.SSEIN.clicked.connect(partial(self.table_data, 5))
        self.SSETC.clicked.connect(partial(self.table_data, 6))
        self.SSEEN.clicked.connect(partial(self.table_data, 7))
        self.SSENR.clicked.connect(partial(self.table_data, 8))
        self.SSEFN.clicked.connect(partial(self.table_data, 9))

    def table_data(self, n):
        """
        This is a function to obtain information on the indices for each sector
        :param n: Decide on the index information to be obtained
        :return: Information obtained on indices by sector
        """
        if n == 0:
            data = pro.daily(ts_code='000001.SZ')
            return self.show_table(data)
        elif n == 1:
            data = pro.daily(ts_code='000036.SZ')
            return self.show_table(data)
        elif n == 2:
            data = pro.daily(ts_code='000039.SZ')
            return self.show_table(data)
        elif n == 3:
            data = pro.daily(ts_code='000037.SZ')
            return self.show_table(data)
        elif n == 4:
            data = pro.daily(ts_code='000033.SZ')
            return self.show_table(data)
        elif n == 5:
            data = pro.daily(ts_code='000004.SZ')
            return self.show_table(data)
        elif n == 6:
            data = pro.daily(ts_code='000040.SZ')
            return self.show_table(data)
        elif n == 7:
            data = pro.daily(ts_code='000032.SZ')
            return self.show_table(data)
        elif n == 8:
            data = pro.daily(ts_code='000068.SZ')
            return self.show_table(data)
        elif n == 9:
            data = pro.daily(ts_code='000038.SZ')
            return self.show_table(data)

    def show_table(self, data):
        """
        This is a function that binds information about each industry index to a tableview
        :param data: Data to be rendered in the tableview
        :return: Presenting data by sector
        """
        # Get the ranks of a dataframe
        self.model = QStandardItemModel(data.shape[0], data.shape[1])
        # Set the content of the horizontal header
        self.model.setHorizontalHeaderLabels(data.columns.values)
        for row in range(data.shape[0]):
            for column in range(data.shape[1]):
                sss = data[data.columns.values[column]][data.index.values[row]]
                sss = str(sss)
                item = QStandardItem(sss)
                # Set the text value for each position
                self.model.setItem(row, column, item)
        self.tableView.setModel(self.model)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Horizontal tabs expand the remaining window sections to fill the table
        self.tableView.horizontalHeader().setStretchLastSection(True)
        # Horizontally, table size expanded to appropriate size
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


# Multiple stock search interface
class Multiple(QWidget, Ui_Form):
    def __init__(self):
        """ Initialise the interface and make the button binding function """
        super(Multiple, self).__init__()
        self.completer = QCompleter(items_list)
        self.setupUi(self)
        self.init_lineedit()

        self.price.clicked.connect(partial(self.show_image, 0))
        self.earn.clicked.connect(partial(self.show_image, 1))
        self.color.clicked.connect(partial(self.show_image, 2))

        self.oned.clicked.connect(partial(self.timeinterval, 1))
        self.fived.clicked.connect(partial(self.timeinterval, 5))
        self.onem.clicked.connect(partial(self.timeinterval, 30))
        self.sixm.clicked.connect(partial(self.timeinterval, 180))
        self.oney.clicked.connect(partial(self.timeinterval, 365))
        self.twoy.clicked.connect(partial(self.timeinterval, 730))
        self.fivey.clicked.connect(partial(self.timeinterval, 1825))
        self.max.clicked.connect(partial(self.timeinterval, 0))

    # Add auto-completion
    def init_lineedit(self):
        """
        This is a function that sets the stock code to auto-completion
        :return: Implementing auto-completion for lineedit
        """
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        # Set complements to lineedit
        self.code1.setCompleter(self.completer)
        self.code2.setCompleter(self.completer)
        self.code3.setCompleter(self.completer)
        self.code4.setCompleter(self.completer)
        self.code5.setCompleter(self.completer)

    def show_image(self, n):
        """
        This is a function that displays line graphs of information
        about multiple functions onto the interface
        :param n: Determine the graphs to be displayed
        :return: Presenting graphs to the interface
        """
        code_list = []
        start_d = self.start.text()
        end_d = self.end.text()
        # Get the stock code entered by the user and store it in code_list
        lst = [self.code1.text(), self.code2.text(), self.code3.text(), self.code4.text(), self.code5.text()]
        for i in range(len(lst)):
            if lst[i] != '':
                code_list.append(lst[i])
        self.image.setScaledContents(True)  # Image size to fit label
        if n == 0:
            get_close_data(code_list, start_d, end_d)
            close_image(code_list)
            self.image.setPixmap(QPixmap("./images/mutiple_price.jpg"))
        if n == 1:
            get_earn_data(code_list, start_d, end_d)
            earn_image(code_list)
            self.image.setPixmap(QPixmap("./images/mutiple_earn.jpg"))
        if n == 2:
            get_close_data(code_list, start_d, end_d)
            color_image(code_list)
            self.image.setPixmap(QPixmap("./images/color_price.jpg"))

    def timeinterval(self, n):
        """
        A function that controls the date range
        :param n: Determine if the date is set
        :return: Implement date range buttons to control the date of the displayed
        """
        code_list = []
        # Get the stock code entered by the user and store it in code_list
        lst = [self.code1.text(), self.code2.text(), self.code3.text(), self.code4.text(), self.code5.text()]
        for i in range(len(lst)):
            if lst[i] != '':
                code_list.append(lst[i])
        if n == 0:
            get_close_data(code_list, start_d=None, end_d=None)
            color_image(code_list)
            self.image.setPixmap(QPixmap("./images/color_price.jpg"))
            self.label.setScaledContents(True)  # Image size to fit label
        else:
            if len(self.end.text()) == 0:
                today = datetime.datetime.today()
                end_d = today.strftime('%y%m%d')
                start_d = today + datetime.timedelta(days=-n)
                start_d = start_d.strftime("%Y%m%d")
            else:
                end_d = self.end.text()
                start_d = Interface.datecalculator(self.end.text(), n)
            get_close_data(code_list, start_d, end_d)
            color_image(code_list)
            self.image.setPixmap(QPixmap("./images/color_price.jpg"))
            self.label.setScaledContents(True)  # Image size to fit label


if __name__ == '__main__':
    # Setting tushare token and initialize
    ts.set_token('35d921c70ecbeff9d5e2249bf5eed7ca28a146aeab40f1b3c65a93e2')
    pro = ts.pro_api()

    # Setting the plot format
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # List of codes to be completed
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,market,list_date')
    items_list = data['ts_code'].values.tolist()

    # Create interfaces
    app = QtWidgets.QApplication(sys.argv)
    main = Interface()
    multiple = Multiple()
    index = Index()

    # The main interface is bound to other interfaces
    main.toolButton.clicked.connect(multiple.show)
    main.index.clicked.connect(index.show)
    main.show()

    sys.exit(app.exec_())
