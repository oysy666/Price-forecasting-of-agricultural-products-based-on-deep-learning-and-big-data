# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press 双击 Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas
import pandas as pd
import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    Vdata = pd.read_csv('data/output.csv')
    data1 = Vdata.loc[Vdata['商品采价地区名称'] == '丽水市']
    data1 = data1.loc[data1['商品采价日期'] == '2017-02']
    goods_num = set(data1['商品主键'])
    print('商品种类数：', len(goods_num))
    price_num = set(data1['商品价格'])
    print('商品种类数：', len(price_num))
    print(data1)
    data1 = data1.loc[:, ['商品主键','商品销量']]
    data1 = data1.iloc[:5, :]
    data1 = data1.rename(columns={"商品主键": "name", "商品销量": "value"})
    df = [{'name': row[0].strip(), 'value': row[1]} for row in data1.values]
    print(df)
    return

def bar_data(name):
    # Use a breakpoint in the code line below to debug your script.
    print(name)  # Press Ctrl+F8 to toggle the breakpoint.
    Vdata1 = pd.read_csv('data/output.csv')
    data11 = Vdata1 # .loc[Vdata1['商品采价地区名称'] == '丽水市']
    # price_num = set(data11['商品价格'])
    # price_num = list(price_num)
    # print('价格种类数：', price_num)
    # data11 = data11.loc[data11['商品价格'] == price_num[5]]
    # print(data11)
    goods_num = set(data11['商品主键'])
    goods_num = list(goods_num)
    print('商品种类数：', len(goods_num))
    data11 = data11.loc[data11['商品主键'] == goods_num[1]]
    print(data11)
    data1 = data11.loc[:, ['商品采价日期', '商品销量']]
    data1 = data1.iloc[:10, :]
    data1 = data1.rename(columns={"商品采价日期": "name", "商品销量": "value"})
    df = [{'name': row[0].strip(), 'value': row[1]} for row in data1.values]
    print(df)
    print(list(data1['name']))
    print(list(data1['value']))
    goods = list(data1['name'])
    sales1 = list(data1['value'])
    from pyecharts import options as opts
    from pyecharts.charts import Bar

    c = (
        Bar()
            .add_xaxis(
            ['2016-12', '2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06', '2017-07', '2017-08', '2017-09']
        )
            .add_yaxis("商家", [1362, 821, 1293, 1698, 2531, 1510, 2064, 1638, 1937, 1466])
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            title_opts=opts.TitleOpts(title="商品在不同时间点销量对比"),
        )
           .render("out_html/bar.html")
    )
    from pyecharts import options as opts
    from pyecharts.charts import Bar
    from pyecharts.faker import Faker

    c = (
        Bar()
            .add_xaxis(Faker.choose())
            .add_yaxis("商家A", Faker.values(), stack="stack1")
            .add_yaxis("商家B", Faker.values(), stack="stack1")
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-堆叠数据（全部）"))
            #.render("bar_stack0.html")
    )
    # from pyecharts import options as opts
    # from pyecharts.charts import Map
    # from pyecharts.faker import Faker
    #
    # citys = ['杭州市', '宁波市', '温州市', '嘉兴市', '湖州市', '绍兴市', '金华市', '衢州市', '舟山市', '台州市', '丽水市']
    # row = []
    # for i in citys:
    #     row_data = np.random.randint(0, 100)
    #     row.append(row_data)
    #
    # print(citys, row)
    #
    # c = (
    #     Map()
    #         .add("商家A", [list(z) for z in zip(citys,row)], "浙江")
    #         .set_global_opts(
    #         title_opts=opts.TitleOpts(title="Map-浙江地图"), visualmap_opts=opts.VisualMapOpts()
    #     )
    #         .render("map_浙江.html")
    # )
    return

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    bar_data("柱状图数据")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
