# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:孙少平
# @Date:2023/3/28 23:42

# 修改excel中的表格内容

import os
import pandas as pd


def main(dir_path, file):
    # 获取当前目录位置
    current_path = os.path.abspath(__file__)
    log_path_list = current_path.split('/')[:-2]
    # 拼接文件路径
    path = '/'.join(log_path_list) + '/' + dir_path + '/' + file
    data = pd.read_csv(path)
    chang_dict = {
        '商品1': '黄瓜',
        '商品2': '西红柿',
        '商品3': '白菜',
        '商品4': '青椒',
        '商品5': '土豆',
        '商品6': '南瓜',
        '商品7': '茄子',
        '商品8': '生菜',
        '商品9': '娃娃菜',
        '商品10': '菠菜',
        '商品11': '韭菜',
        '商品12': '胡萝卜',
        '商品13': '西兰花',
        '商品14': '油麦菜',
        '商品15': '蒜黄',
        '商品16': '上海青',
        '商品17': '香菜',
        '商品18': '豆角',
        '商品19': '小葱',
        '商品20': '茼蒿',
        '商品21': '香菇',
        '商品22': '木耳',
        '商品23': '蒜苔',
        '商品24': '芹菜',
        '商品25': '红薯',
        '商品26': '大蒜',
        '商品27': '生姜'
    }
    data['商品主键'] = data['商品主键'].map(chang_dict)
    data.to_csv(path)
    print(f'{file}数据替换完成...')


if __name__ == '__main__':
    # csv_list = ['嘉兴市.csv', '宁波市.csv', '温州市.csv', '绍兴市.csv', '舟山市.csv', '衢州市.csv', '金州市.csv']
    csv_list = ['output.csv']
    for file in csv_list:
        main('data', file)
