#导入csv文件
import pandas as pd
import numpy as np

main_country=['China','America','Russia','India','Japan','England','Canada','Brazil'
    ,'South Korea','United Kingdom','France','Germany'
    ,'Australia','Italy','Mexico','Turkey','South Africa','Indonesia','Saudi Arabia','Singapore'] #主要国家列表


df_doc=pd.read_csv("-\medicalDoctors.csv",sep=",",encoding="utf-8")#编码格式使用记事本查看
df_doc.head()
df_doc = df_doc.iloc[:,[0,3]]   #取国家名 和 每万人拥有医生数
df_doc.rename(columns={'Location':'国家','First Tooltip':'医生数/万人'},inplace=True)  #修改列名
country_list = df_doc["国家"].values.tolist() # 求出所有国家列表
s = set(country_list)
country_list = list(s)

df_list = []
for i in country_list:
    df_country = df_doc.loc[df_doc.loc[:,"国家"]==i]
    df_country = df_country.fillna(df_country.mean())   #每列的平均填充缺失值
    df_country = df_country.iloc[[0], :]   #取最新的数据
    df_list.append(df_country)

df_final = pd.concat(df_list)   #将各个国家的数据整合在一起
df_final = df_final.dropna()    #删除缺失值


df=pd.read_csv("全球新冠肺炎疫情量化数据.csv",sep=",",encoding="gbk")#编码格式使用记事本查看
df.head()
df1 = df.loc[df.loc[:,"日期"]=='2022/3/11']   #先筛选
df2 = df1.iloc[:,[1,2,10,60]]
df2 = df2.dropna()    #删除缺失值

#合并两个 df
df_final = pd.merge(df_final,df2,on="国家")


#筛选10个主要国家作对比
main_list = []
num = 0

for i in main_country:
    if num >= 10:
        break
    if (df_final["国家"]==i).any():
        main_list.append( df_final.loc[df_final.loc[:,"国家"]==i] )
        num = num+1

df_final = pd.concat(main_list)   #将各个国家的数据整合在一起
df_final = df_final.sort_values(by="每百万人确诊人数",ascending=True)#升序排列

df_final.to_csv("世界卫生情况统计.csv",index=False,float_format="%.2f")
