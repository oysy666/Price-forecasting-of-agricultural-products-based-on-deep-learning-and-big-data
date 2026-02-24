# -*- coding: UTF-8 -*-
'''
@Project ：Course Design 
@File    ：leida_zhejiang.py
@IDE     ：PyCharm 
@Author  ：2022的山大王
@Date    ：2022/5/5 15:53 
'''
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Radar, Timeline
def lei_zhejiang(name, value,y):
    data = pd.read_csv('out_data/' + name + '.csv')
    data = data.loc[data['商品主键'] == value]
    data['商品采价日期'] = pd.to_datetime(data['商品采价日期'])
    data['年月'] = data['商品采价日期'].apply(lambda x: x.strftime('%Y-%m'))
    data['年'] = data['商品采价日期'].dt.year
    data['月'] = data['商品采价日期'].dt.month
    data1 = data.loc[data['商品主键'] == value]
    data1 = data1.loc[data['年'] == y]
    data1 = data1.loc[:, ['月', '销售额']]
    data1 = data1.iloc[:50, :]
    data1 = data1.rename(columns={"月": "name", "销售额": "value"})
    mon = list(data1['name'])
    mon1 = []
    for i in mon:
        i = str(i) + '月'
        mon1.append(i)
    df = [{'name': str(row[0]).split('.')[0]+'月', 'max': data1['value'].max(), 'min': data1['value'].min()} for row in data1.values]

    sales1 = list(data1['value'])
    return df,sales1


def leida_zhejiang(name,value):
    t = Timeline()
    for i in range(2021, 2024):
        df,sales1 = lei_zhejiang(name=name,value=value,y=i)
        sales1 = sales1
        # print(sales1)

        data = [{"value": sales1, "name": value}]
        c_schema = df
        # print(c_schema)

        c = (
            Radar()
                .set_colors([" #FF6600 "])
                .add_schema(
                schema=c_schema,
                shape="circle",
                center=["50%", "50%"],
                radius="80%",
                angleaxis_opts=opts.AngleAxisOpts(
                    min_=0,
                    max_=360,
                    is_clockwise=True,
                    interval=1,
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    axislabel_opts=opts.LabelOpts(is_show=False),
                    axisline_opts=opts.AxisLineOpts(is_show=False),
                    splitline_opts=opts.SplitLineOpts(is_show=False),
                ),
                radiusaxis_opts=opts.RadiusAxisOpts(
                    min_=0,
                    max_=10,
                    interval=1,
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                ),
                polar_opts=opts.PolarOpts(),
                splitarea_opt=opts.SplitAreaOpts(is_show=True),
                splitline_opt=opts.SplitLineOpts(is_show=False),
            )
                .add(
                series_name="总销售额",
                data=data,
                areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
                linestyle_opts=opts.LineStyleOpts(width=1),
            )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
                .set_global_opts(title_opts=opts.TitleOpts("{} 年{}销售额".format(i,value),title_textstyle_opts=opts.TextStyleOpts(font_size=20, color="#99CC00")),
                                 legend_opts=opts.LegendOpts(is_show=True, pos_right='10px', orient='vertical',
                                                             textstyle_opts=opts.TextStyleOpts(font_size=15,
                                                                                               color="#99CC00")),
                                 )
        )

        t.add(c, "{} 年".format(i))
        t.add_schema(height='30px',
                     pos_bottom='25px',
                     play_interval=2000,
                     is_auto_play=True,
                     # 是否循环播放。
                     is_loop_play=True, )
    # t.render("dada图.html")

    return t
# leida_zhejiang('绍兴市','商品1')