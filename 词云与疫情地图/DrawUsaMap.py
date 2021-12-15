#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Target  ：
@Author  ：jackyliu
@Date    ：2021/12/15 19:16
Reference:
    https://pyecharts.org/#/zh-cn/intro
    https://gallery.pyecharts.org/#/README

'''
from typing import List
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Bar, Map, Pie, Line
from pyecharts.datasets import register_url
import json

register_url("https://echarts-maps.github.io/echarts-countries-js/")

with open('Data(2).json', 'r') as fp:
    json_data = fp.read()
    Data = json.loads(json_data)
    # print(Data)

# print(json_data)

time_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# 全世界确诊增量
minNum = maxNum = 0
total_confirmed_list = []
for month_dict in Data:
    month_confirmed_list = 0
    for province_dict in month_dict['Data']:
        month_confirmed_list += province_dict['Confirmed']
        if province_dict['Confirmed'] > maxNum:
            maxNum = province_dict['Confirmed']
    total_confirmed_list.append(month_confirmed_list)
# print(total_confirmed_list)
print(minNum, maxNum)


def get_year_chart(year: str):
    global maxNum, minNum, total_confirmed_list
    map_data = [
        [[x["Province"], x["Confirmed"]] for x in d["Data"]] for d in Data if d["time"] == year][0]
    min_data, max_data = (minNum, maxNum)
    data_mark: List = []
    i = 0
    for x in time_list:
        if x == year:
            data_mark.append(total_confirmed_list[i])
        else:
            data_mark.append("")
        i = i + 1

    map_chart = (
        Map()
            .add(
            series_name="",
            data_pair=map_data,
            zoom=1,
            maptype='美国',
            is_roam=False,
            center=[-96.3, 35.1],
            is_map_symbol_show=False,
            itemstyle_opts={
                "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                "emphasis": {
                    "label": {"show": Timeline},
                    "areaColor": "rgba(255,255,255, 0.5)",
                },
            },
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="" + str(year) + "美国确诊人数变动图",
                subtitle="",
                pos_left="center",
                pos_top="top",
                title_textstyle_opts=opts.TextStyleOpts(
                    font_size=25, color="rgba(255,255,255, 0.9)"
                ),
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                formatter=JsCode(
                    """function(params) {
                    if ('value' in params.data) {
                        return params.data.value[2] + ': ' + params.data.value[0];
                    }
                }"""
                ),
            ),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="30",
                pos_top="center",
                range_text=["High", "Low"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
        )
    )
    data = sorted(map_data, key=(lambda x: x[1]), reverse=True)
    bar_x_data = [x[0] for x in data]  # 分类名称
    bar_y_data = [x[1] for x in data]  # value
    bar = (
        Bar()
            .add_xaxis(xaxis_data=bar_x_data)
            .add_yaxis(
            series_name="",
            yaxis_data=bar_y_data,
            label_opts=opts.LabelOpts(
                is_show=True, position="right", formatter="{b} : {c}"
            ),
        )
            .reversal_axis()
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                max_=maxNum, axislabel_opts=opts.LabelOpts(is_show=False)
            ),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="10",
                pos_top="top",
                range_text=["High", "Low"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
        )
    )

    pie_data = [[x[0], x[1]] for x in map_data]
    pie = (
        Pie()
            .add(
            series_name="",
            data_pair=pie_data,
            radius=["5%", "25%"],
            center=["80%", "82%"],
            itemstyle_opts=opts.ItemStyleOpts(
                border_width=1, border_color="rgba(0,0,0,0.3)"
            ),
        )
            .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{b} {d}%"),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )

    grid_chart = (
        Grid()
            .add(
            bar,
            grid_opts=opts.GridOpts(
                pos_left="10", pos_right="45%", pos_top="30%", pos_bottom="5"
            ),
        )
            .add(pie, grid_opts=opts.GridOpts(pos_left="65%", pos_top="60%"))
            .add(map_chart, grid_opts=opts.GridOpts())
    )

    return grid_chart


if __name__ == "__main__":
    timeline = Timeline(
        init_opts=opts.InitOpts(width="2160px", height="1080px", theme=ThemeType.DARK)
    )
    for y in time_list:
        g = get_year_chart(year=y)
        timeline.add(g, time_point=str(y))

    timeline.add_schema(
        orient="vertical",
        is_auto_play=True,
        is_inverse=True,
        play_interval=2000,
        pos_left="null",
        pos_right="5",
        pos_top="20",
        pos_bottom="20",
        width="60",
        label_opts=opts.LabelOpts(is_show=True, color="#fff"),
    )

    timeline.render("美国疫情地图Test.html")
