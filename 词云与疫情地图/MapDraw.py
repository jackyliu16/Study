"""
Author： 刘逸珑
Time：   2021/12/8 22:29
https://pyecharts.org/#/zh-cn/intro
https://gallery.pyecharts.org/#/README
"""
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker


class Draw_map():
    def to_map_city(self):
        pass
    def tp_map_china(self,area,variate,updateTime):
        pieces = [
            {'max':100000,'min':50000,'label1':'>1000000','color':'#8A0808'},
            {'max': 50000, 'min': 10000, 'label1': '>10000', 'color': '#B40404'},
            {'max': 10000, 'min': 100, 'label1': '>100', 'color': '#DF0101'},
            {'max': 1000, 'min': 0, 'label1': '>0', 'color': '#F5A9A9'},
        ]
        c = (
            Map(init_opts=opts.InitOpts(width="1960px",height="1080px"))
                .add("累计确诊人数", [list(z) for z in zip(area, variate)], "china")
                .set_global_opts(
                title_opts=opts.TitleOpts(title="中国疫情地图分布",subtitle="本图表的数据截止日期为{}".format(updateTime)),
                visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True,pieces=pieces),
            )
                .render("中国疫情地图.html")
        )
