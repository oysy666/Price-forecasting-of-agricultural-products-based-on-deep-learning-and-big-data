# -*- coding: UTF-8 -*-
'''
@Project ：Course Design 
@File    ：pie_zhejiang.py
@IDE     ：PyCharm 
@Author  ：2022的山大王
@Date    ：2022/5/5 14:41 
'''
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline

import experiment

def pie_zhejiang(name,value) -> Pie:
    c = Timeline()
    for i in range(2021, 2024):
        data = experiment.experiment0(name=name,value=value,y=i)
        pie = (
            Pie()
                .add(
                value,
                [list(z) for z in zip(data[0],data[1])],
                rosetype="radius",
                radius=["30%", "55%"],
                label_opts=opts.LabelOpts(is_show=True,font_size=15),
            )
                .set_global_opts(title_opts=opts.TitleOpts("{} 年{}销售额比例".format(i,value),title_textstyle_opts=opts.TextStyleOpts(font_size=20, color="#99CC00")),
                                 legend_opts=opts.LegendOpts(is_show=True,
                                                             pos_right='10px', orient='vertical',
                                                             textstyle_opts=opts.TextStyleOpts(font_size=15,
                                                                                               color="#99CC00")
                                                             ), )
        )
        c.add(pie, "{} 年".format(i))
        c.add_schema(height='30px',
                     pos_bottom='25px',
                     play_interval=2500,
                     is_auto_play=True,
                    # 是否循环播放。
                    is_loop_play=True,)
    # c.render("冰冰图.html")

    return c
# pie_zhejiang('绍兴市','商品1')