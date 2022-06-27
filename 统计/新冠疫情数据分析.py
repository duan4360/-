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
    temp=df.loc[(df.loc[:,"日期"]=='2022/3/11')&((df.loc[:,"所属洲"].isna()==False))&((df.loc[:,"人类发展指数"].isna()==False))
                , ['国家', '日期', '人类发展指数']]
    print(temp.loc[temp.loc[:,'国家']=='China',['国家','人类发展指数']])

def GDP_and_humanity_num():  #GDP与人类发展指数
    df = pd.read_csv("D:\综合课程设计Ⅲ\全球新冠肺炎疫情量化数据.csv", encoding='GBK', error_bad_lines=False)
    temp = df.loc[(df.loc[:, "日期"] == '2022/3/11') & ((df.loc[:, "所属洲"].isna() == False)) & (
    (df.loc[:, "国家"]))
    , ['国家', '日期','GDP（购买力平价计算）','人类发展指数']]
    l=pandas.DataFrame(columns=['国家', '日期','GDP（购买力平价计算）','人类发展指数'])
    for i in main_country:
        tdf=temp.loc[temp.loc[:,"国家"]==i,['国家', '日期','GDP（购买力平价计算）','人类发展指数']]
        l=l.append(tdf)
    print(l)

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
    print(l)

##################################################################################################
if __name__=='__main__':
    #state_disease_num()
    #get_data_to_csv()
    GDP_and_humanity_num()
    government_response()

