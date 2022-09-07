import requests
import re
import pandas as pd
import plotly.express as px

# 获取全部板块及板块id
url = 'http://quotes.money.163.com/old/#query=hy001000&DataType=HS_RANK&sort=PERCENT&order=desc&count=24&page=0'

r = requests.get(url)

html = r.text
# 替换非字符为空，便于下面的正则
html = re.sub('\s', '', html)
# 正则获取 板块及id所在区域
labelHtml = re.findall(r'</span>主要行业\(新\)</a>(.*?)</span>证监会行业\(新\)', html)[0]
# 正则板块和id，结果为由元组组成的列表
label = re.findall(r'"qid="(hy.*?)"qquery=.*?"title="(.*?)">', labelHtml)
# 转化为dataframe类型
dfLabel = pd.DataFrame(label, columns=['id', '板块'])


# 根据板块id和翻页获取页面数据（json格式）
def get_json(hy_id, page):
    query = 'PLATE_IDS:' + str(hy_id)
    params = {
        'host': 'http://quotes.money.163.com/hs/service/diyrank.php',
        'page': page,
        'query': query,
        'fields': 'NO,SYMBOL,NAME,PRICE,PERCENT,UPDOWN,OPEN,YESTCLOSE,HIGH,LOW,VOLUME,ANNOUNMT,UVSNEWS',
        # 你可以不用这么多字段
        'sort': 'PERCENT',
        'order': 'desc',
        'count': '24',
        'type': 'query',
    }
    url = 'http://quotes.money.163.com/hs/service/diyrank.php?'
    r = requests.get(url, params=params)
    j = r.json()

    return j


# 空列表用于存取每页数据
dfs = []
# 遍历全部板块
for hy_id, 板块 in dfLabel.values:
    # 获取页数
    j = get_json(hy_id, 0)
    pages = j['pagecount']

    for page in range(pages):
        j = get_json(hy_id, page)
        data = j['list']
        df = pd.DataFrame(data)
        df['板块'] = 板块
        dfs.append(df)
    print(f'已爬取{len(dfs)}个板块数据')

result = pd.concat(dfs)
print(result)


