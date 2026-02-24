# -*- coding: UTF-8 -*-
'''
@Project ：Course Design 
@File    ：气泡图.py
@IDE     ：PyCharm 
@Author  ：2022的山大王
@Date    ：2022/5/5 16:21 
'''
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Scatter

def qipao_zhejiang(name):
    print(name)
    Vdata1 = pd.read_csv('data/output.csv')
    data11 = Vdata1
    goods_num = set(data11['商品主键'])
    goods_num = list(goods_num)
    print('商品种类数：', len(goods_num))
    data11 = data11.loc[data11['商品主键'] == goods_num[1]]
    data1 = data11.loc[:, ['商品采价日期', '商品销量']]
    data1 = data1.iloc[:10, :]
    data1 = data1.rename(columns={"商品采价日期": "name", "商品销量": "value"})
    print(data11)
    df = [{'name': row[0].strip(), 'value': row[1]} for row in data1.values]
    goods = list(data1['name'])
    sales1 = list(data1['value'])
    title = str(goods_num[1]) + '在不同时间点销量对比'
    print(goods)
    print(sales1)
    print(title)

    c = (
        Scatter()
            .add_xaxis(goods)
            .add_yaxis(goods_num[1], sales1)
            .set_global_opts(
            title_opts=opts.TitleOpts(title=title),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=10, min_=2),
        )
            .render("out_html/qipao.html")
    )

qipao_zhejiang("浙江省-气泡图")