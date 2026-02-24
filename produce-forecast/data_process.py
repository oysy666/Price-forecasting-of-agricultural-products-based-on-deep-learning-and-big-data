# -*- coding: GBK -*-
'''
@Project ：project 
@File    ：data_process.py
@IDE     ：PyCharm 
@Author  ：2022的山大王
@Date    ：2022/5/4 10:52 
'''
import pandas as pd
import numpy as np

def read_file(file):
    data1 = pd.read_csv(file[0],encoding='GBK')
    data2 = pd.read_csv(file[1],encoding='GBK')
    data3 = pd.read_csv(file[2],encoding='GBK')
    data4 = pd.read_csv(file[3],encoding='GBK')
    data5 = pd.read_csv(file[4],encoding='GBK')
    data6 = pd.read_csv(file[5],encoding='GBK')
    data = data1, data2, data3, data4, data5, data6
    return data

# 删除每一个文件里的主键ID列，合并6个文件
def drop_id(data):
    all_data = pd.concat((data[0].iloc[:, 0:-1], data[1].iloc[:, 0:-1], data[2].iloc[:, 0:-1],
                          data[3].iloc[:, 0:-1], data[4].iloc[:, 0:-1], data[5].iloc[:, 0:-1]), ignore_index=True)
    return all_data

# 数据添加
def expend_colums(all_data):
    # 增加销量和销售额,先用空值填充
    all_data['商品销量'] = "NaN"
    all_data['销售额'] = "NaN"
    # 获取行数
    row = all_data.shape
    # 随机数并存为列表
    row_data = np.random.randint(0, 1000, row[0])
    # 填充数据
    all_data['商品销量'] = row_data
    all_data['销售额'] = all_data['商品价格'] * all_data['商品销量']
    print("填充数据完成：\n", all_data.iloc[:5,:])
    return all_data

# 数据处理(删除不符合要求的数据)
def process_data(all_data):
    # 由于数据中包含浙江省的数所以要去除，删除所有采价地为浙江省的数据
    # 查询浙江省的数据
    index = all_data[all_data['商品采价地区名称'] == '浙江省'].index.tolist()
    print("处理前数据量为：", all_data.shape)
    print("含有浙江省的数据量为：", len(index))
    all_data.drop(index, inplace=True)
    # 参数：inplace=True
    # 是在原文件进行更改，Flase表示不更改，需要赋值
    # 删除商品采价地区名称列的空行数据
    all_data.dropna(subset=['商品采价地区名称'], inplace=True)
    # 验证浙江省数据是否删除干净
    index1 = all_data[all_data['商品采价地区名称'] == '浙江省'].index.tolist()
    print("去除后的浙江省数据为：", index1)
    print('处理后的数据量为：', all_data.shape)
    return all_data

# 数据集成（用商品1、2、3替换商品种类）
def replace_data(all_data):
    # 城市数量
    city_num = set(all_data['商品采价地区名称'])
    print('城市数量：', len(city_num), city_num)
    # 商品种类数
    goods_num = set(all_data['商品主键'])
    print('商品种类数：', len(goods_num))
    # 用商品1、2、3替换原商品种类
    goods = []
    for i in range(1, int(len(goods_num))+1):
        goods.append('商品'+str(i))
    print(goods)
    data_id_l = list(goods_num)
    new_dict = {}
    for i in range(0, 27):
        new_dict[data_id_l[i]] = goods[i]  # 字典赋值，左边为key，右边为value
    all_data['商品主键'].replace(new_dict, inplace=True)
    print("替换后的数据为：\n", all_data)
    return all_data, city_num

# 数据时间处理
def date_data(all_data,num):
    # 先将日期中“日”删去,若“商品销量”和“销售额”以外的属性相同，则将“商品销量”和“销售额”数值相加
    import datetime
    all_data['商品采价日期'] = pd.to_datetime(all_data['商品采价日期'])
    all_data['商品采价日期'] = all_data['商品采价日期'].apply(lambda x: datetime.datetime.strftime(x, '%Y-%m'))
    print('处理日期后的数据为：\n', all_data.head(3))
    all_data = all_data.groupby(['商品采价地区名称', '商品主键', '商品采价日期', '商品采价地区编码']).sum()
    print(all_data)
    # 输出数据,以商品采价地为单位
    city_num = num
    print(city_num)
    i = 0
    city_num2 = list(city_num)
    for c in city_num:
        c = all_data.loc[c, :]
        name = city_num2[i]
        i = i + 1
        c.to_csv('out_data/'+ name + '.csv', sep=',', index=True)
        print(name)


    # all_data.to_csv('./data/output.csv',sep=',', index=True)
    return print('数据处理完成！')
# 可视化
def visualization():
    return

if __name__ == '__main__':
    file = 'data/cata_6008_1.csv', 'data/cata_6008_2.csv', 'data/cata_6008_3.csv', 'data/cata_6008_4.csv',\
           'data/cata_6008_5.csv', 'data/cata_6008_6.csv'
    data = read_file(file=file)
    all_data = drop_id(data)
    all1_data = expend_colums(all_data)
    all2_data = process_data(all1_data)
    all3_data, num = replace_data(all2_data)
    all4_data = date_data(all3_data,num=num)
    visualization()
