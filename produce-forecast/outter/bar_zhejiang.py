# -*- coding: UTF-8 -*-
'''
@Project ：Course Design 
@File    ：bar_zhejiang.py
@IDE     ：PyCharm 
@Author  ：2022的山大王
@Date    ：2022/5/5 15:18 
'''
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline

import experiment

def timeline_bar(gs, sp) -> Timeline:
    tl = Timeline()
    for i in range(2021, 2024):
        data = experiment.experiment0(name=gs, value=sp, y=i)
        bar = (
            Bar()
                .add_xaxis(data[0])
                .add_yaxis(sp, data[1], itemstyle_opts=opts.ItemStyleOpts(color="#99CC00"))
                .set_global_opts(title_opts=opts.TitleOpts('{}年{}不同时间点销量对比'.format(i, sp),
                                                           title_textstyle_opts=opts.TextStyleOpts(font_size=20, color="#99CC00")),
                                 legend_opts=opts.LegendOpts(is_show=True, pos_right='10px', orient='vertical',
                                                             textstyle_opts=opts.TextStyleOpts(font_size=15,
                                                                                               color="#99CC00")),

                                 xaxis_opts=opts.AxisOpts(
                                                          name='月份', name_rotate=0,
                                                          name_textstyle_opts=opts.TextStyleOpts(color='#7ca6f4',
                                                                                                 font_size=20,
                                                                                                 font_weight='bold'),
                                                          axisline_opts=opts.AxisLineOpts(  # 坐标轴轴线相关设置
                                                              is_show=True,
                                                              symbol=[None, 'arrow'],  # 箭头
                                                              linestyle_opts=opts.LineStyleOpts(  # 坐标轴线风格配置项
                                                                  is_show=True,
                                                                  width=8,
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
                                                              position="right",  # 标签的位置
                                                              color='green',  # Optional[str]
                                                              font_size=16,  # Optional[Numeric]
                                                              rotate=0,  # 斜率
                                                              margin=15,  # 刻度标签与轴线之间的距离。
                                                          ),
                                                          ),
                                 yaxis_opts=opts.AxisOpts(name='销量',
                                                          name_textstyle_opts=opts.TextStyleOpts(color='#7ca6f4',
                                                                                                 font_size=20,font_weight='bold'),
                                                          axisline_opts=opts.AxisLineOpts(  # 坐标轴轴线相关设置
                                                              is_show=True,
                                                              symbol=[None, 'arrow'],  # 箭头
                                                              linestyle_opts=opts.LineStyleOpts(  # 坐标轴线风格配置项
                                                                  is_show=True,
                                                                  width=8,
                                                                  opacity=1,  # 图形透明度。支持从 0 到 1 的数字，
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
                                                              position="right",  # 标签的位置
                                                              color='green',  # Optional[str]
                                                              font_size=16,  # Optional[Numeric]
                                                              rotate=10,  # 斜率
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
                                 )
        )
        tl.add(bar, "{}年".format(i))
        tl.add_schema(
            # axis_type="category",
            # # 时间轴的类型。可选:
            # # 'horizontal': 水平
            # # 'vertical': 垂直
            # orient="horizontal",
            # # timeline 标记的图形。
            # # ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle', 'diamond',
            # # 'pin', 'arrow', 'none'
            # # 可以通过 'image://url' 设置为图片，其中 URL 为图片的链接，或者 dataURI。
            # symbol='circle',
            # # timeline 标记的大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示宽和高，
            # # 例如 [20, 10] 表示标记宽为 20，高为 10。
            # symbol_size=None,
            # # 表示播放的速度（跳动的间隔），单位毫秒（ms）。
            # play_interval=2500,
            # # 表示播放按钮的位置。可选值：'left'、'right'。
            # control_position="left",
            # # 是否自动播放。
            # is_auto_play=True,
            # # 是否循环播放。
            # is_loop_play=True,
            # # 是否显示 timeline 组件。如果设置为 false，不会显示，但是功能还存在。
            # is_timeline_show=True,
            #
            # # Timeline 组件离容器左侧的距离。
            # # left 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，
            # # 也可以是 'left', 'center', 'right'。
            # # 如果 left 的值为'left', 'center', 'right'，组件会根据相应的位置自动对齐
            # pos_left=None,
            # pos_right=None,
            # pos_top=None,
            # pos_bottom=None,
            # # 时间轴区域的宽度, 影响垂直的时候时间轴的轴标签和轴之间的距离
            # width=None,
            # # 时间轴区域的高度
            # height='30px',
            # # 时间轴的坐标轴线配置，参考 `series_options.LineStyleOpts`
            # linestyle_opts=None,
            # # 时间轴的轴标签配置，参考 `series_options.LabelOpts`
            # label_opts=opts.LabelOpts(  # 坐标轴刻度标签的相关设置
            #     is_show=True,  # bool
            #     position="bottom",  # 标签的位置
            #     color='green',  # Optional[str]
            #     font_size=15,  # Optional[Numeric]
            #     rotate=0,  # 斜率
            #     margin=5,  # 刻度标签与轴线之间的距离。
            # ),
            # # 时间轴的图形样式，参考 `series_options.ItemStyleOpts`
            # itemstyle_opts=opts.ItemStyleOpts(
            #     color='green',
            # ),
            # # 控制按钮』的样式。『控制按钮』包括：『播放按钮』、『前进按钮』、『后退按钮』。
            # controlstyle_opts=opts.TimelineControlStyle(
            #     # 『控制按钮』的尺寸，单位为像素（px）。
            #     item_size=20,
            #     # 『控制按钮』的间隔，单位为像素（px）。
            #     item_gap=30,
            #     # 『控制按钮』的位置。
            #     position="left",
            #     color="#304654",
            #     # 按钮边框颜色。
            #     border_color="#304654",
            #     # 按钮边框线宽。
            #     border_width=2,
            height='30px',
            pos_bottom='5px',
            play_interval=2500,
            is_auto_play=True,
            # 是否循环播放。
            is_loop_play=True,
            ),

    return tl
