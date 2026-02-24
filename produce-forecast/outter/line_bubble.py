# -*- coding: UTF-8 -*-
'''
@Project ：flask-pyecharts 
@File    ：line_bubble.py
@IDE     ：PyCharm 
@Author  ：2022的山大王
@Date    ：2022/5/13 10:20 
'''
from pyecharts import options as opts
from pyecharts.charts import Line, Scatter, Timeline
import pandas as pd

import experiment


def line_zehjiang11(name, value):
    dd = experiment.experiment1(name=name, value=value)
    x = dd[0]
    a = dd[1]
    b = dd[2]
    line1 = (
        Scatter(
            # init_opts=opts.InitOpts(bg_color='#003366')
        )
            .add_xaxis(x)
            .add_yaxis(value+'销量', b,markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]), yaxis_index=0)

            .extend_axis(yaxis=opts.AxisOpts(type_="value",
                                             name='价格',
                                             name_textstyle_opts=opts.TextStyleOpts(color='green',
                                                                                    font_size=20,
                                                                                    font_weight='bold'),
                                             axisline_opts=opts.AxisLineOpts(  # 坐标轴轴线相关设置
                                                 is_show=True,
                                                 symbol=[None, 'arrow'],  # 箭头
                                                 linestyle_opts=opts.LineStyleOpts(  # 坐标轴线风格配置项
                                                     is_show=True,
                                                     width=3,
                                                     opacity=0.5,  # 图形透明度。支持从 0 到 1 的数字，
                                                     color='green',
                                                 )),
                                             axistick_opts=opts.AxisTickOpts(is_show=True,
                                                          is_align_with_label=True,
                                                          length=10,
                                                          linestyle_opts=opts.LineStyleOpts(
                                                              width=5,
                                                              color='green',
                                                          )),
                                             axislabel_opts=opts.LabelOpts(  # 坐标轴刻度标签的相关设置
                                                 is_show=True,  # bool
                                                 # position="right",  # 标签的位置
                                                 color='green',  # Optional[str]
                                                 font_size=16,  # Optional[Numeric]
                                                 rotate=0,  # 斜率
                                                 margin=10,  # 刻度标签与轴线之间的距离。
                                             ),
                                             axispointer_opts=opts.AxisPointerOpts(  # 坐标轴指示器设置
                                                 is_show=True,
                                                 type_="line",
                                                 linestyle_opts=opts.LineStyleOpts(
                                                     is_show=True,
                                                     width=5,
                                                     opacity=0.5,
                                                     curve=0,
                                                     type_="solid",
                                                     color=' #FFCC00 ',
                                                 ),
                                             ),
                                             splitline_opts=opts.SplitLineOpts(is_show=True), ))  # 双坐标轴 这个必须添加,添加虚线
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=max(b), min_=min(b), is_show=False),

            title_opts=opts.TitleOpts(title=value+'销量、价格变化', title_textstyle_opts=opts.TextStyleOpts(font_size=20, color="#99CC00")),

            xaxis_opts=opts.AxisOpts(
                name='时间', name_rotate=0,
                name_textstyle_opts=opts.TextStyleOpts(color='green',
                                                       font_size=20,
                                                       font_weight='bold'),
                axisline_opts=opts.AxisLineOpts(  # 坐标轴轴线相关设置
                    is_show=True,
                    symbol=[None, 'arrow'],  # 箭头
                    linestyle_opts=opts.LineStyleOpts(  # 坐标轴线风格配置项
                        is_show=True,
                        width=3,
                        opacity=1,  # 图形透明度。支持从 0 到 1 的数字，
                        type_="solid",
                        color='green',
                    )),
                axistick_opts=opts.AxisTickOpts(  # 坐标轴刻度相关设置
                    is_show=True,
                    is_align_with_label=True,
                    length=8,
                    linestyle_opts=opts.LineStyleOpts(
                        is_show=True,
                        width=5,
                        opacity=1,
                        curve=0,
                        type_="solid",
                        color='green',
                    )
                ),
                axislabel_opts=opts.LabelOpts(  # 坐标轴刻度标签的相关设置
                    is_show=True,  # bool
                    position="top",  # 标签的位置
                    color=' #FF6600 ',  # Optional[str]
                    font_size=12,  # Optional[Numeric]
                    rotate=90,  # 斜率
                    margin=10,  # 刻度标签与轴线之间的距离。
                ),
            ),

                             yaxis_opts=opts.AxisOpts(name='销量',
                                                      name_textstyle_opts=opts.TextStyleOpts(color='green',
                                                                                             font_size=20,
                                                                                             font_weight='bold'),
                                                      axisline_opts=opts.AxisLineOpts(  # 坐标轴轴线相关设置
                                                          is_show=True,
                                                          symbol=[None, 'arrow'],  # 箭头
                                                          linestyle_opts=opts.LineStyleOpts(  # 坐标轴线风格配置项
                                                              is_show=True,
                                                              width=3,
                                                              opacity=0.5,  # 图形透明度。支持从 0 到 1 的数字，
                                                              type_="solid",
                                                              color='green',
                                                          )),
                                                      axistick_opts=opts.AxisTickOpts(  # 坐标轴刻度相关设置
                                                          is_show=True,
                                                          is_align_with_label=True,
                                                          length=10,
                                                          linestyle_opts=opts.LineStyleOpts(
                                                              is_show=True,
                                                              width=5,
                                                              opacity=1,
                                                              curve=0,
                                                              type_="solid",
                                                              color='green',
                                                          )
                                                      ),
                                                      axislabel_opts=opts.LabelOpts(  # 坐标轴刻度标签的相关设置
                                                          is_show=True,  # bool
                                                          # position="right",  # 标签的位置
                                                          color='green',  # Optional[str]
                                                          font_size=16,  # Optional[Numeric]
                                                          rotate=0,  # 斜率
                                                          margin=10,  # 刻度标签与轴线之间的距离。
                                                      ),
                                                      axispointer_opts=opts.AxisPointerOpts(  # 坐标轴指示器设置
                                                          is_show=True,
                                                          type_="line",
                                                          linestyle_opts=opts.LineStyleOpts(
                                                              is_show=True,
                                                              width=10,
                                                              opacity=0.5,
                                                              curve=0,
                                                              type_="solid",
                                                              color='green',
                                                          ),
                                                      ),
                                                      ),
            legend_opts=opts.LegendOpts(is_show=True, pos_top='10px', orient='vertical',
                                        textstyle_opts=opts.TextStyleOpts(font_size=15, color="#99CC00")),
                             )
            .set_series_opts(label_opts=opts.LabelOpts(position='right', color="green", font_size=15))
    )
    line2 = (
        Line()
            .add_xaxis(x)
            .add_yaxis(value+'价格', a, linestyle_opts=opts.LineStyleOpts(color="#7ca6f4", width=4),
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]), yaxis_index=1)
            .set_series_opts(label_opts=opts.LabelOpts(position='right', color=" #FF9900 ", font_size=15))
    )
    line1.overlap(line2)
    # line1.render("折线散点组合图.html")
    return line1

# line_zehjiang11('绍兴市', '商品1')