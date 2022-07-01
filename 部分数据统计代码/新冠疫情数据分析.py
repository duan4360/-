import pandas
import pandas as pd
import os
from matplotlib import pyplot as plt
from sympy.physics.quantum.circuitplot import matplotlib
############################################################################################################

#主要国家
main_country=['China','United States','Russia','India','Japan','England','Canada','Brazil','South Korea','United Kingdom','France','Germany'
              ,'Australia','Italy','Mexico','Turkey','South Africa','Indonesia','Saudi Arabia','Singapore']
"""
purpose:按照excel某列字段将一个文件拆分成多个文件。
"""
# 按照文件所包含的专业新建不同专业的工作表
def creatfilebymajor(filepath, filename):
    scoresinfo = pd.read_csv("D:\综合课程设计Ⅲ\数据\全球新冠肺炎疫情量化数据.csv",encoding="gbk")#编码格式使用记事本查看

    # 获取专业列所有数值，包括重复的
    majors = scoresinfo[property]

    # 获取去重后的专业并转化为list方便读取数据,set函数是一个无序不重复的元素集，list为[],set为{}
    nmajors = list(set(majors))

    # 获取专业的个数，即需要创建工作表的个数
    filenums = len(nmajors)

    # 根据专业数量，创建对应个数的工作表，工作表的名称以专业命名
    for i in range(0, filenums, 1):
        majorpath = filepath.replace(filename, "") + list(nmajors)[i] + ".xlsx"
        df = pd.DataFrame()
        df.to_excel(majorpath)


def splitbymajor(filepath,filename):  # filepath="C:\\Users\\lenovo\\Desktop\\test\\scores.xlsx"这里必须双斜杠 ,filename="scores.xlsx"
    # 1、创建各专业文件
    creatfilebymajor(filepath, filename)
    scores = pd.read_csv("D:\综合课程设计Ⅲ\数据\全球新冠肺炎疫情量化数据.csv",encoding="gbk")#编码格式使用记事本查看
    grouped = scores.groupby(property)  # 按照专业分组
    majors = scores[property]  # 获取专业列所有数值，包括重复的
    nmajors = list(set(majors))  # 获取去重后的专业并转化为list方便读取数据,set函数是一个无序不重复的元素集，list为[],set为{}
    # 2、分别将各专业从分组后的集合中取出.get_group("专业名称")，然后专业名称与文件名称比对，配对后写入对应专业文件
    dir = filepath.replace("\\" + filename, "")  # 获取文件所在的根目录，即文件夹目录
    for i in range(0, len(nmajors), 1):
        major = grouped.get_group(nmajors[i])
        # 遍历文件夹下面的所有文件
        for root_dir, sub_dir, files in os.walk(r'' + dir):  # 遍历目录下的根目录，子目录，所有文件
            # 对文件列表中的每一个文件进行处理，如果文件名字是以‘xlxs’结尾就
            # 认定为是一个excel文件，当然这里还可以用其他手段判断，比如你的excel
            # 文件名中均包含‘res’，那么if条件可以改写为
            # if file.endswith('xlsx') and 'res' in file:
            for file in files:
                if file == nmajors[i] + '.xlsx':
                    major.to_excel(filepath.replace(filename, "") + nmajors[i] + ".xlsx", index=False)


def state_disease_num():  #大洲疾病数目统计
    df = pd.read_csv("D:\综合课程设计Ⅲ\各组织的新冠数据.csv", encoding='GBK', error_bad_lines=False)  # 编码格式使用记事本查看
    df = df.drop(df.index.to_list()[10034:], axis=0)

    temp = df.loc[df.loc[:, "日期"] == '2022/3/11', ['国家', '日期', '确诊总数']]
    print(temp)
    x = temp['国家'].tolist()  # 直接建立列表，设置
    y = temp['确诊总数'].tolist()
    # 绘制图形
    matplotlib.rcParams["font.family"] = "SimHei"
    plt.figure(figsize=(12, 6))
    x_width = range(0, len(x))
    color = ['yellow', 'red', 'green', 'blue', 'pink', 'black', 'orange', 'purple', 'peru', 'gray', 'tan', 'bisque',
             'skyblue']
    for i in x_width:
        plt.bar(i, y[i], lw=0.5, fc=color[i], width=0.4, label=x[i])
    # plt.plot(x, y, linewidth=1, color="orange", marker="*")
    plt.xlabel("各大洲或组织")
    plt.ylabel("确诊总数(亿人)")
    plt.xticks(range(len(x)), range(1, len(x) + 1))
    plt.title("各大洲或组织截至2022-3-11的确诊总数")
    plt.legend()
    plt.show()

def get_data_to_csv():#获取数据
    df = pd.read_csv("D:\综合课程设计Ⅲ\全球新冠肺炎疫情量化数据.csv", encoding='GBK', error_bad_lines=False)
    temp=df.loc[(df.loc[:,"日期"]=='2022/3/11')&(df.loc[:,"所属洲"].isna()==False)&(df.loc[:,"人类发展指数"].isna()==False)
                , ['国家', '日期', '人类发展指数']]
    print(temp.loc[temp.loc[:,'国家']=='China',['国家','人类发展指数']])

def GDP_and_humanity_num():  #人均GDP与人类发展指数
    df = pd.read_csv("D:\综合课程设计Ⅲ\全球新冠肺炎疫情量化数据.csv", encoding='GBK', error_bad_lines=False)
    temp = df.loc[(df.loc[:, "日期"] == '2022/3/11') & ((df.loc[:, "所属洲"].isna() == False)) & (
    (df.loc[:, "国家"]))
    , ['国家', '日期','GDP（购买力平价计算）','人类发展指数']]
    l=pandas.DataFrame(columns=['国家', '日期','GDP（购买力平价计算）','人类发展指数'])
    for i in main_country:
        tdf=temp.loc[temp.loc[:,"国家"]==i,['国家', '日期','GDP（购买力平价计算）','人类发展指数']]
        l=l.append(tdf)
    tl=l[['国家','GDP（购买力平价计算）']]
    tl=tl.sort_values(by='GDP（购买力平价计算）', ascending=False)
    print(tl)
    pie_chart(tl['GDP（购买力平价计算）'].tolist(),tl['国家'].tolist(),title='主要国家人均GDP对比')

    tl=l[['国家','人类发展指数']]
    print(tl)
    x=tl['国家'].tolist()
    y=[float(i) for i in tl['人类发展指数'].tolist()]
    bar_char(y, x, '主要国家人类发展指数', xl='国家', yl='发展指数')
    '''matplotlib.rcParams["font.family"] = "SimHei"
    plt.figure(figsize=(12, 6))
    x_width = range(0, len(x))
    color = ['red', 'yellow', 'green', 'blue', 'pink', 'black', 'orange', 'purple', 'peru', 'gray', 'tan', 'bisque',
             'skyblue', 'gold', 'maroon', 'silver', 'yellowgreen', 'mediumorchid', 'khaki', 'darkred']
    for i in x_width:
        plt.bar(i, y[i], lw=0.5, fc=color[i], width=0.4)
    # plt.plot(x, y, linewidth=1, color="orange", marker="*")
    plt.xlabel("国家")
    plt.ylabel("人类发展指数")
    plt.xticks(range(len(x)), range(1, len(x) + 1))
    plt.title("主要国家人类发展指数对比")
    plt.legend()
    plt.show()'''


def government_response():  #政府响应严格指数
    df = pd.read_csv("D:\综合课程设计Ⅲ\全球新冠肺炎疫情量化数据.csv", encoding='GBK', error_bad_lines=False)
    temp = df.loc[(df.loc[:, "日期"] == '2022/3/11') & ((df.loc[:, "所属洲"].isna() == False)), ['国家', '政府响应严格指数']]
    temp=temp.fillna('null')
    #print(temp)
    l = pandas.DataFrame(columns=['国家', '政府响应严格指数'])
    for i in main_country:
        tdf = temp.loc[temp.loc[:, "国家"] == i, ['国家', '政府响应严格指数']]
        if 'null' not in tdf['政府响应严格指数'].tolist():
            l=l.append(tdf)
        else:
            t= df.loc[((df.loc[:, "所属洲"].isna() == False)) & (
            df.loc[:, "国家"]==i), ['国家','政府响应严格指数']]
            print(t['政府响应严格指数'].mean())
            tdf['政府响应严格指数']=t['政府响应严格指数'].mean()  # 每列的平均填充缺失值
            l=l.append(tdf)
    l.sort_values(by='政府响应严格指数', ascending=False)
    #pie_chart(l['政府响应严格指数'].tolist(),l['国家'].tolist())
    bar_char(l['政府响应严格指数'].tolist(),l['国家'].tolist(),title="主要国家新冠期间政府响应严格指数",xl='国家',yl="政府响应指数")
    print(l)

def the_main_countries_GDP_changes(): #主要国家2013-2020年GDP变化
    column=['Country']
    column.extend([str(i) for i in range(2013,2021)])
    df = pd.read_csv("D:\综合课程设计Ⅲ\WEOOct2021all.csv", encoding='GBK', error_bad_lines=False)
    df=df.loc[(df.loc[:, "Country"].isin(main_country)) & ((df.loc[:, "WEO Subject Code"]=='NGDPD')),
                  column]
    for i in [j for j in range(2013,2021)]:
        df.loc[:,str(i)]=[float(j.replace(',','')) for j in df[str(i)].tolist()]
    print(df)
    y,country=[],[]
    for i in main_country:
        temp=df.loc[df.loc[:, "Country"]==i,[str(i) for i in range(2013,2021)]]
        temp=temp.values.tolist()
        if len(temp)>0:
            country.append(i)
            y.append(temp[0])
    print(y)
    broken_line_chart(x=[i for i in range(2013,2021)], y=y, label=country, title='2013-2020各国GDP变化图', xl='年份（年）', yl='GDP（亿美元）')

def unemployment_rate():   #主要国家近几年失业率
        column = ['Country']
        column.extend([str(i) for i in range(2016, 2023)])
        df = pd.read_csv("D:\综合课程设计Ⅲ\WEOOct2021all.csv", encoding='GBK', error_bad_lines=False)
        df = df.loc[(df.loc[:, "Country"].isin(main_country)) & (df.loc[:, "Subject Descriptor"] == 'Unemployment rate')
        &(df.loc[:, "2022"].isna()==False),column]
        for i in [j for j in range(2016, 2023)]:
            df.loc[:, str(i)] = [float(j) for j in df[str(i)].tolist()]
        print(df)
        heatmap(x_ticks=[str(i) for i in range(2016, 2023)], y_ticks=df['Country'], df=df[[str(i) for i in range(2016, 2023)]], title='2016-2022各国失业率变化图', xl='年份（年）',
                          yl='失业率（%）')

def china_importandexport():  #中国近几年进出口
    from dateutil.parser import parse as ps
    bt = ps("2019-1-1")
    et = ps("2022-1-1")
    df = pd.read_csv("D:\综合课程设计Ⅲ\Import_Export.csv", encoding='GBK', error_bad_lines=False)
    df['Month']=pd.to_datetime(df['Month'], format="%Y年%m月")
    df = df.loc[(df.loc[:, "Month"]<=et)&(df.loc[:, "Month"]>=bt), ['Month','Total_Export','Total_Export_YOY','Total_Import','Total_Import_YOY']]
    '''for i in [j for j in range(2016, 2023)]:
        df.loc[:, str(i)] = [float(j) for j in df[str(i)].tolist()]'''
    df=df.sort_values(by='Month', ascending=True)
    print(df)
    x=[ str(i)[2:7] for i in df['Month'].tolist()]
    y1=[int(i) for i in df['Total_Export'].tolist()]
    y2=[ float(i[:-1]) for i in df['Total_Export_YOY'].tolist()]
    y3=[int(i) for i in df['Total_Import'].tolist()]
    y4=[ float(i[:-1]) for i in df['Total_Import_YOY'].tolist()]

    plt.rcParams['font.sans-serif']=['Microsoft YaHei']
    plt.figure(figsize=(14, 9))
    ax1 = plt.subplot2grid((2, 1), (0, 0), colspan=1, rowspan=1)
    # 第一个括号的（2,2）表示将画布分割成2*2，（0,0）表示该子图从位置（0,0）开始，
    # colspan和rowspan分别表示子图占用的行长度和列长度
    ax1.plot(x, y1)
    ax1.set_ylabel("总出口额（亿元）")
    ax1.set_title("2019到2022每月出口额")
    ax1.grid()
    plt.xticks(rotation=45, fontsize=9)

    ax2 = plt.subplot2grid((2, 1), (1, 0), colspan=1, rowspan=1)
    ax2.plot(x, y2)
    ax2.set_ylabel("总出口额增长率（%）")
    ax2.set_title("2019到2022每月出口额与同期相比增长率")
    ax2.grid()
    plt.xticks(rotation=45, fontsize=9)
    plt.show()

    plt.figure(figsize=(14, 9))
    ax3 = plt.subplot2grid((2, 1), (0, 0), colspan=2, rowspan=1)
    ax3.plot(x, y3)
    print('ok')
    ax3.set_ylabel("总进口额（亿元）")
    ax3.set_title("2019到2022每月进口额")
    ax3.grid()
    plt.xticks(rotation=45, fontsize=9)

    ax4 = plt.subplot2grid((2, 1), (1, 0), colspan=2, rowspan=1)
    ax4.plot(x, y4)
    ax4.set_ylabel("总进口额增长率（%）")
    ax4.set_title("2019到2022每月进口额与同期相比增长率")
    ax4.grid()
    plt.xticks(rotation=45, fontsize=9)
    plt.show()
    #broken_line_chart()

def china_industrial_add_value():  #中国近两年工业增加值变化率
    from dateutil.parser import parse as ps
    bt = ps("2019-1-1")
    et = ps("2021-12-1")
    df = pd.read_csv("D:\综合课程设计Ⅲ\Industrial_Added_Value.csv", encoding='GBK', error_bad_lines=False)
    df['Month'] = pd.to_datetime(df['Month'], format="%Y年%m月")
    df = df.loc[(df.loc[:, "Month"] <= et) & (df.loc[:, "Month"] >= bt), ['Month', 'Cumulative_Growth']]
    df = df.sort_values(by='Month', ascending=True)
    print(df)
    x = [str(i)[2:7] for i in df['Month'].tolist()]
    y = [float(i[:-1]) for i in df['Cumulative_Growth'].tolist()]
    broken_line_chart(x=x, y=[y], label=[], title='2019到2022每月工业产值增长率', xl='年月', yl='增长率（%）')

def export_of_medical_device(): #用雷达图展示中国对各州医疗产品出口额
    import numpy as np

    # 某学生的课程与成绩
    state = ['亚洲', '欧洲', '南美洲', '非洲', '大洋洲', '北美洲']
    export = [297.04, 445.09, 42.5,40.5,21.09, 390.08]
    dataLength = len(export)  # 数据长度
    # angles数组把圆周等分为dataLength份
    angles = np.linspace(0, 2 * np.pi, dataLength, endpoint=False)
    export.append(export[0])
    angless = np.append(angles, angles[0])  # 闭合
    # 绘制雷达图
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.polar(angless,  # 设置角度
              export,  # 设置各个角度上的数据
              'rv--',  # 设置颜色、线型和端点符号
              linewidth=2)  # 设置线宽
    # 设置角度网络标签
    plt.thetagrids(angles * 180 / np.pi, state, fontproperties='simhei', fontsize=10, color='k')
    # 填充雷达图内部
    plt.fill(angless, export, facecolor='g', alpha=0.2)
    plt.title("中国2020年对各洲医疗设备出口额（亿美元）")
    plt.show()

def heatmap(x_ticks,y_ticks,df,title,xl,yl):  #热力图
    import seaborn as sns
    pd.set_option('expand_frame_repr', False)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 可以正常显示中文
    plt.figure(figsize=(9, 6))
    ax = sns.heatmap(df, annot=True, fmt='.3f', cmap="OrRd", vmax=35, vmin=0, xticklabels=x_ticks,
                     yticklabels=y_ticks)
    #  annot=True表示每一个格子显示数字;fmt='.0f'表示保留0位小数，同理fmt='.1f'表示保留一位小数
    #  camp表示颜色，在另一个博主的文章中讲解的很清晰
    #  vmax=350, vmin=20表示右侧颜色条的最大最小值，在最大最小值外的颜色将直接以最大或最小值的颜色显示，
    #  通过此设置就可以解决少数值过大从而使得大部分色块区别不明显的问题
    #  xticklabels=x_ticks, yticklabels=y_ticks，横纵轴标签
    ax.set_title(title)  # 图标题
    ax.set_xlabel(xl)  # x轴标题
    ax.set_ylabel(yl)  # y轴标题
    plt.show()

def pie_chart(x,labels,title): #饼图
    matplotlib.rcParams["font.family"] = "SimHei"
    plt.figure(figsize=(8, 6))
    # 建立轴的大小
    explode = [0.05 for i in range(len(x))]
    # 这个是控制分离的距离的，默认饼图不分离
    plt.pie(x, labels=labels, explode=explode, startangle=60, autopct='%1.1f%%')
    # autopct在图中显示比例值，注意值的格式
    plt.title(title)
    plt.show()

def bar_char(y,label,title,xl,yl): #带平均值的柱状图
    import numpy as np
    matplotlib.rcParams["font.family"] = "SimHei"
    plt.figure(figsize=(12, 8))
    x_width = range(0, len(y))
    color = [ 'red','yellow','green', 'blue', 'pink', 'black', 'orange', 'purple', 'peru', 'gray', 'tan', 'bisque',
             'skyblue','gold','maroon','silver','yellowgreen','mediumorchid','khaki','darkred']
    c = np.mean(y)
    for i in x_width:
        rects=plt.bar(i, y[i], lw=0.5, fc=color[i],width=0.4, label=label[i]) #hatch="/",
        for rect in rects:
            plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height(), round(y[i],2), size=10, ha='center', va='bottom')
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.xticks(range(len(label)), label,rotation=30, fontsize=8)
    plt.title(title)
    plt.axhline(y=c, color="red",linestyle='--')
    #plt.legend()
    plt.show()

def broken_line_chart(x,y,label,title,xl,yl): #折线图
    plt.rcParams['font.sans-serif']=['Microsoft YaHei']
    plt.figure(figsize=(9, 8))
    color = ['red', 'yellow', 'green', 'blue', 'pink', 'black', 'orange', 'purple', 'peru', 'gray', 'tan', 'bisque',
             'skyblue', 'gold', 'maroon', 'silver', 'yellowgreen', 'mediumorchid', 'khaki', 'darkred']

    for i in range(len(y)):
        plt.plot(x, y[i], marker='*',linewidth=1, linestyle='--', color=color[i])
    #plt.legend(label,loc="upper left")
    if len(label)!=0:
        plt.legend(label,bbox_to_anchor=(0.96, 0.45), loc=3, borderaxespad=0)
    plt.title(title)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.xticks(rotation=45, fontsize=8)
    plt.show()

##################################################################################################
if __name__=='__main__':
    pass
    #get_data_to_csv()
    state_disease_num()
    GDP_and_humanity_num()
    government_response()
    the_main_countries_GDP_changes()
    unemployment_rate()
    china_importandexport()
    china_industrial_add_value()
    export_of_medical_device()




