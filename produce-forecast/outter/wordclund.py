# -*- coding: UTF-8 -*-
'''
@Project ：Course Design 
@File    ：wordclund.py
@IDE     ：PyCharm 
@Author  ：2022的山大王
@Date    ：2022/5/5 17:39 
'''


import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import WordCloud
import random


def ciyun_zhejiang(name):
    """
    商品1：黄瓜
    商品2：西红柿
    商品3：白菜
    商品4：青椒
    商品5：土豆
    商品6：南瓜
    商品7：茄子
    商品8：生菜
    商品9：娃娃菜
    商品10：菠菜
    商品11：韭菜
    商品12：胡萝卜
    商品13：西兰花
    商品14：油麦菜
    商品15：蒜黄
    商品16：上海青
    商品17：香菜
    商品18：豆角
    商品19：小葱
    商品20：茼蒿
    商品21：香菇
    商品22：木耳
    商品23：蒜苔
    商品24：芹菜
    商品25：红薯
    商品26：大蒜
    商品27：生姜
    :param name:
    :return:
    """
    Vdata1 = pd.read_csv('out_data/' + name + '.csv')
    data11 = Vdata1
    price_num = set(data11['商品采价日期'])
    price_num = list(price_num)
    n = len(price_num)
    date = price_num[random.randint(0, n - 1)]
    data11 = data11.loc[data11['商品采价日期'] == date]
    data1 = data11.loc[:, ['商品主键', '商品销量']]
    data1 = data1.iloc[:, :]
    data1 = data1.rename(columns={"商品主键": "name", "商品销量": "value"})
    df = [(row[0].strip(), row[1]) for row in data1.values]
    # print(df)
    # goods = list(data1['name'])
    # sales1 = list(data1['value'])
    title = name + str(date) + '商品销量词云'
    # print(goods)
    # print(sales1)
    # print(title)
    c = (
        WordCloud()
        .add(series_name='词云', data_pair=df, word_size_range=[10, 100])
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title=title, title_textstyle_opts=opts.TextStyleOpts(font_size=20, color='#99CC00')
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    return c

# ciyun_zhejiang("绍兴市")
