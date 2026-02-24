# -*- coding: UTF-8 -*-
'''
@Project ：flask-pyecharts 
@File    ：app.py.py
@IDE     ：PyCharm 
@Author  ：2022的山大王
@Date    ：2022/5/9 17:36 
'''

from flask import Flask, render_template, request
from outter import list_chart

app = Flask(__name__, static_folder="static")
urban = '绍兴市'
goods = '黄瓜'


@app.route("/", methods=['POST', 'GET'])
def index():
    global urban, goods
    if request.method == 'POST':
        urban = request.form.get('urban')
        goods = request.form.get('goods')
        if not urban:
            print('空值')
            urban = '绍兴市'
            ll = list_chart.list_(name=urban, value=goods)
            return render_template("index1.html", c_name='城市不能为空', ls=ll)
        else:
            print(urban, goods)
            ll = list_chart.list_(name=urban, value=goods)
            return render_template("index1.html", c_name=urban, ls=ll)
    else:
        ll = list_chart.list_(name=urban, value=goods)
    return render_template("index1.html", ls=ll)


from outter import bar_zhejiang


@app.route("/barChart")
def get_bar_chart():
    c = bar_zhejiang.timeline_bar(gs=urban, sp=goods)
    return c.dump_options_with_quotes()


from outter import line_bubble


@app.route("/line_zhe")
def get_line_chart1():
    c = line_bubble.line_zehjiang11(name=urban, value=goods)
    return c.dump_options_with_quotes()


from outter import zhejiagn_map


@app.route("/map_zhejiang")
def get_map_chart1():
    c = zhejiagn_map.map_zhejian(name=urban, good=goods)
    return c.dump_options_with_quotes()


from outter import pie_zhejiang


@app.route("/pie_zhe")
def get_pie_chart2():
    c = pie_zhejiang.pie_zhejiang(name=urban, value=goods)
    return c.dump_options_with_quotes()


from outter import wordclund


@app.route("/word_zhe")
def get_word_chart2():
    c = wordclund.ciyun_zhejiang(name=urban)
    return c.dump_options_with_quotes()


from outter import leida_zhejiang


@app.route("/radar_zhe")
def get_radar_chart2():
    c = leida_zhejiang.leida_zhejiang(name=urban, value=goods)
    return c.dump_options_with_quotes()


if __name__ == "__main__":
    app.run(debug=True)
