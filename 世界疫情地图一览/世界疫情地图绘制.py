from pyecharts.charts import Map
from pyecharts import options as opts
import pandas as pd

df=pd.read_csv("世界确诊人数统计排名.csv",sep=",",encoding="utf-8")#编码格式使用记事本查看
df.head()
country_names = list(df['国家'])
total_nums = list(df['确诊总数'])

map = Map( init_opts=opts.InitOpts(width="1900px", height="900px", bg_color="#ADD8E6",
	page_title="3.10全球疫情确诊人数",theme="white"))

map.add("确诊人数",[list(z) for z in zip(country_names, total_nums)],is_map_symbol_show=False,
    maptype="world",label_opts=opts.LabelOpts(is_show=False),
    itemstyle_opts=opts.ItemStyleOpts(color="rgb(49,60,72)"))

map.set_global_opts(title_opts = opts.TitleOpts(title='3.10 全球疫情确诊人数'),
	legend_opts=opts.LegendOpts(is_show=False),
    visualmap_opts = opts.VisualMapOpts(max_=10000000))
map.render('world_map.html')

