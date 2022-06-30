from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.charts import Timeline
import pandas as pd

file_name_list = ['世界确诊人数统计排名_2020.3.1.csv','世界确诊人数统计排名_2020.4.1.csv','世界确诊人数统计排名_2020.5.1.csv',
                  '世界确诊人数统计排名_2020.6.1.csv','世界确诊人数统计排名_2020.7.1.csv','世界确诊人数统计排名_2020.8.1.csv',
                  '世界确诊人数统计排名_2020.9.1.csv','世界确诊人数统计排名_2020.10.1.csv','世界确诊人数统计排名_2020.11.1.csv',
                  '世界确诊人数统计排名_2020.12.1.csv','世界确诊人数统计排名_2021.1.1.csv','世界确诊人数统计排名_2021.2.1.csv',
                  '世界确诊人数统计排名_2021.3.1.csv','世界确诊人数统计排名_2021.4.1.csv','世界确诊人数统计排名_2021.5.1.csv',
                  '世界确诊人数统计排名_2021.6.1.csv','世界确诊人数统计排名_2021.7.1.csv','世界确诊人数统计排名_2021.8.1.csv',
                  '世界确诊人数统计排名_2021.9.1.csv','世界确诊人数统计排名_2021.10.1.csv','世界确诊人数统计排名_2021.11.1.csv',
                  '世界确诊人数统计排名_2021.12.1.csv','世界确诊人数统计排名_2022.1.1.csv','世界确诊人数统计排名_2022.2.1.csv',
                  '世界确诊人数统计排名_2022.3.1.csv']
file_abs_path = '-\世界疫情地图一览\实时疫情'

#定义每日地图绘制函数
def map_visualmap(sequence, date) -> Map:
    return Map( init_opts=opts.InitOpts(page_title="世界疫情动态地图")).add(date, sequence,is_map_symbol_show=False,
        maptype="world",label_opts=opts.LabelOpts(is_show=False),).set_global_opts(title_opts=opts.TitleOpts(title="世界疫情动态地图"),
    visualmap_opts=opts.VisualMapOpts(max_=10000000),)


#创建时间轴对象
timeline = Timeline()
for i in file_name_list:
    #读取每月数据
    df1 = pd.read_csv(file_abs_path+'/'+i, sep=",", encoding="utf-8")  # 编码格式使用记事本查看
    df1.head()

    #取每月数据
    row = list(df1['确诊总数'])
    # 取出省份列表
    attr = list(df1['国家'])
    #将数据转换为二元的列表
    sequence_temp = list(zip(attr,row))
    #对日期格式化以便显示
    time = df1['时间'].tolist()[0]
    #创建地图
    map_temp = map_visualmap(sequence_temp,time)
    #将地图加入时间轴对象
    timeline.add(map_temp,time).add_schema(play_interval=360)
    # 地图创建完成后，通过render()方法可以将地图渲染为html
    timeline.render('世界疫情动态地图.html')


