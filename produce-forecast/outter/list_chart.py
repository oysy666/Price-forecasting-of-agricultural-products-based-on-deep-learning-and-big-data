# -*- coding: UTF-8 -*-
'''
@Project ：Course Design 
@File    ：list_chart.py
@IDE     ：PyCharm 
@Author  ：2022的山大王
@Date    ：2022/5/5 18:52 
'''
import pandas as pd

def list_(name,value):
    data = pd.read_csv('out_data/' + name + '.csv')

    data = data.loc[data['商品主键'] == value]
    dict_return = {}  # 存放需要的数据
    data_list = e = data
    num = []
    n = data_list.shape[0]
    for i in range(1, n):
        num.append(str(i))

    dict_return['diff_list'] = [{'Ranking': item[0], '商品主键': item[1], '商品价格': item[2],
                                 '商品采价日期': item[3], '商品销量': item[4], '销售额': item[5]}
                                for item in list(zip(num, data_list['商品主键'], data_list['商品价格'],
                                                     data_list['商品采价日期'], data_list['商品销量'],
                                                     data_list['销售额']))]  # 将数据制作成滚动图需要的数据格式
    list_chart = []  #将数据添加到列表
    for i in dict_return['diff_list']:
        list_chart.append(i)

    return list_chart

# a = list_('绍兴市','商品1')
# print(a)