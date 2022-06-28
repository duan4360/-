#导入csv文件
import pandas as pd
import numpy as np

df=pd.read_csv("全球新冠肺炎疫情量化数据.csv",sep=",",encoding="gbk")#编码格式使用记事本查看
df.head()
df1 = df.loc[df.loc[:,"日期"]=='2022/3/11']   #先筛选
df2 = df1.iloc[:,[2,4,10]]
df3 = df2.sort_values(by="每百万人确诊人数",ascending=False)#默认升序排列
print(df3)
df3.to_csv("世界确诊人数统计排名.csv",index=False,float_format="%.2f")
