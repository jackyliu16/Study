#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Target  ：
@Author  ：jackyliu
@Date    ：2021/12/10 10:41
@Reference:
    https://github.com/pyecharts/pyecharts/issues/1372
'''
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Collector, Faker
from pyecharts.datasets import register_url

# 如果出现 ssl 异常再加下面这两行
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context


register_url("https://echarts-maps.github.io/echarts-countries-js/")

def tp_map_china(area,variate):
    pieces = [
        {'max':100000,'min':50000,'label1':'>1000000','color':'#8A0808'},
        {'max': 50000, 'min': 10000, 'label1': '>10000', 'color': '#B40404'},
        {'max': 10000, 'min': 100, 'label1': '>100', 'color': '#DF0101'},
        {'max': 1000, 'min': 0, 'label1': '>0', 'color': '#F5A9A9'},
    ]
    c = (
        Map(init_opts=opts.InitOpts(width="1960px",height="1080px"))
            .add("累计确诊人数", [list(z) for z in zip(area, variate)], "美国")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="中国疫情地图分布",subtitle="本图表的数据截止日期为{}".format(0)),
            visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True,pieces=pieces),
        )
            .render("中国疫情地121图.html")
    )

tp_map_china(['北京'],['100'])


