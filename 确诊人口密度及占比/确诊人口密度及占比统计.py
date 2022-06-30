#导入csv文件
import pandas as pd
import numpy as np

main_country=['China','America','Russia','India','Japan','England','Canada','Brazil'
    ,'South Korea','United Kingdom','France','Germany'
    ,'Australia','Italy','Mexico','Turkey','South Africa','Indonesia','Saudi Arabia','Singapore'] #主要国家列表

df=pd.read_csv("全球新冠肺炎疫情量化数据.csv",sep=",",encoding="gbk")#编码格式使用记事本查看
df.head()

df1 = df.iloc[:,[1,2,4,10,48,49]]

df_time = df.loc[df.loc[:,"日期"]=='2022/3/11']   #先筛选
country_list = df_time["国家"].values.tolist() # 求出所有国家列表
#print(country_list)

df_list = []
for i in country_list:
    df_country = df1.loc[df1.loc[:,"国家"]==i]
    df_country = df_country.fillna(df_country.mean())#每列的最大值填充缺失值
    df_country = df_country.iloc[[-1], :]   #取最后一行 即最后一天的数据
    df_list.append(df_country)

df_final = pd.concat(df_list)   #将各个国家的数据整合在一起
df_final = df_final.dropna()    #删除缺失值

df_final['土地面积'] = df_final.apply(lambda x: x['人口'] /  x['人口：土地面积（人/平方公里）'], axis=1)  #计算各国的领土面积
df_final['每平方公里患病人数'] = df_final.apply(lambda x: x['确诊总数'] /  x['土地面积'], axis=1)  #计算各国的单位面积患病人数
df_final['确诊人数占国家总人口的比重(%)'] = df_final.apply(lambda x: x['确诊总数']*100 /  x['人口'], axis=1)  #确诊人数占国家总人口的比重

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
df_final = df_final.sort_values(by="每平方公里患病人数",ascending=True)#升序排列

df_final.to_csv("世界患病人口密度统计.csv",index=False,float_format="%.3f")
