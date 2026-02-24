# -*- coding: UTF-8 -*-
'''
@Project ：Course Design 
@File    ：zhejiagn_map.py
@IDE     ：PyCharm 
@Author  ：2022的山大王
@Date    ：2022/5/5 12:07 
'''

from pyecharts import options as opts
from pyecharts.charts import Map
def map_zhejian(name, good) -> Map:
    c = (
        Map()
            .add(good, [list(z) for z in zip([name], [100])], "浙江", label_opts=opts.LabelOpts(is_show=True, font_size=18, position='right',color=" #99CC00 "))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="浙江省地图", title_textstyle_opts=opts.TextStyleOpts(font_size=30, color="#99CC00")),
            visualmap_opts=opts.VisualMapOpts(max_=100, is_piecewise=True, is_show=False),
            legend_opts=opts.LegendOpts(is_show=True, textstyle_opts=opts.TextStyleOpts(font_size=16, color="#99CC00"), pos_right='10px'),
        )
    )
    return c
# map_zhejian()