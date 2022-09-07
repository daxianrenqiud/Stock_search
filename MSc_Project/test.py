from pyecharts.charts import Map
from pyecharts import options as opts

from lxml import html, etree
import requests

from bs4 import BeautifulSoup
import webbrowser

webbrowser.open("IndustryMap.html")
# def create_map():
#     Finance = [['北京', 1], ['安徽', 1]]
#     Industrial = [['天津', 3], ['河北', 3], ['山西', 3], ['辽宁', 3], ['黑龙江', 3],
#                   ['上海', 3], ['福建', 3], ['江西', 3], ['河南', 3], ['湖北', 3],
#                   ['青海', 3]]
#     Manufacturing = [['内蒙古', 5], ['江苏', 5], ['浙江', 5], ['广东', 5]]
#     Agriculture = [['吉林', 7], ['山东', 7], ['广西', 7], ['贵州', 7], ['西藏', 7],
#                    ['陕西', 7], ['甘肃', 7], ['宁夏', 7], ['新疆', 7]]
#     Tourism = [['湖南', 9], ['海南', 9], ['重庆', 9], ['四川', 9], ['云南', 9]]
#     (
#         Map(opts.InitOpts(width='2060px', height='860px'))
#         .add(series_name="Industry Map",data_pair=Finance,maptype="china",)
#         .add(series_name="Industry Map",data_pair=Industrial,maptype="china",)
#         .add(series_name="Industry Map",data_pair=Manufacturing,maptype="china",)
#         .add(series_name="Industry Map",data_pair=Agriculture,maptype="china",)
#         .add(series_name="Industry Map",data_pair=Tourism,maptype="china",)
#         # Global configuration items
#         .set_global_opts(title_opts=opts.TitleOpts(title="Industry Map"),
#         # Setting the standard display
#         visualmap_opts=opts.VisualMapOpts(is_piecewise= True,pieces=[{"min": 1, "max": 2, "label": 'Finance'},
#                                                                      {"min": 3, "max": 4, "label": 'Industrial'},
#                                                                      {"min": 5, "max": 6, "label": 'Manufacturing'},
#                                                                      {"min": 7, "max": 8, "label": 'Agriculture'},
#                                                                      {"min": 9, "max": 10, "label": 'Tourism'}]),)
#         # Series configuration items
#         .set_series_opts(label_opts=opts.LabelOpts(is_show=False),) # Label name display, default is True
#         .render("IndustryMap.html") # Generate local html files
#     )
# create_map()
