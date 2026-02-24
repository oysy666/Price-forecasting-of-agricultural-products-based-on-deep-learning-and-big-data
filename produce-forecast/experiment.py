# -*- coding: UTF-8 -*-
'''
@Project ：flask-pyecharts 
@File    ：experiment.py
@IDE     ：PyCharm 
@Author  ：2022的山大王
@Date    ：2022/5/12 16:56 
'''

'''
图表数据整理
'''

import pandas as pd

def experiment0(name, value, y):

    data = pd.read_csv('out_data/' + name + '.csv')
    data = data.loc[data['商品主键'] == value]
    data['商品采价日期'] = pd.to_datetime(data['商品采价日期'])
    data['年月'] = data['商品采价日期'].apply(lambda x: x.strftime( '%Y-%m'))
    data['年'] = data['商品采价日期'].dt.year
    data['月'] = data['商品采价日期'].dt.month
    data1 = data.loc[data['商品主键'] == value]
    data1 = data1.loc[data['年'] == y]
    data1 = data1.loc[:, ['月', '商品销量']]
    data1 = data1.rename(columns={"月": "name", "商品销量": "value"})
    # print(list(data1['name']))
    # print(list(data1['value']))
    if not list(data1['value']):  # 判断有无空值
        print('无'+str(y)+'年'+value+'数据')
        date = ['无日期']
        sales1 = [0]
        return [date, sales1]
    else:
        # print('you')
        mon = list(data1['name'])
        mon1 = []
        for i in mon:
            i = str(i) + '月'
            mon1.append(i)
        # print(mon1)
        date = mon1
        sales1 = list(data1['value'])
        title = value + '在不同时间点销量对比'
        # print(date)
        # print(sales1)
        # print(title)

        return [date, sales1]

# experiment0('丽水市', '商品11', 2016)

def experiment1(name, value):

    data = pd.read_csv('out_data/' + name + '.csv')
    data = data.loc[data['商品主键'] == value]
    data1 = data.loc[:, ['商品采价日期', '商品价格', '商品销量']]
    # data1 = data1.rename(columns={"月": "name", "商品销量": "value"})
    date = list(data1['商品采价日期'])
    sales1 = list(data1['商品价格'])
    sales2 = list(data1['商品销量'])
    title = value + '在不同时间点销量对比'
    # print(title)

    return [date, sales1, sales2]