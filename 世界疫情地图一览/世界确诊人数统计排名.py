#导入csv文件
import pandas as pd

df=pd.read_csv("全球新冠肺炎疫情量化数据.csv",sep=",",encoding="gbk")#编码格式使用记事本查看
df.head()
df_list = []

for i in range(3,13):
    df_time = df.loc[df.loc[:,"日期"]=='2020/'+str(i)+'/1']
    df2 = df_time.iloc[:, [2, 4]]
    df2['时间'] = '2020.'+str(i)+'.1'
    df2["确诊总数"] = df2["确诊总数"].fillna(0)  # 使用0填充缺测值
    df2.to_csv('实时疫情/世界确诊人数统计排名_2020.'+str(i)+'.1.csv', index=False, float_format='%.2f')

for i in range(1,13):
    df_time = df.loc[df.loc[:,"日期"]=='2021/'+str(i)+'/1']
    df2 = df_time.iloc[:, [2, 4]]
    df2['时间'] = '2021.'+str(i)+'.1'
    df2["确诊总数"] = df2["确诊总数"].fillna(0)  # 使用0填充缺测值
    df2.to_csv('实时疫情/世界确诊人数统计排名_2021.'+str(i)+'.1.csv', index=False, float_format='%.2f')

for i in range(1,4):
    df_time = df.loc[df.loc[:,"日期"]=='2022/'+str(i)+'/1']
    df2 = df_time.iloc[:, [2, 4]]
    df2['时间'] = '2022.'+str(i)+'.1'
    df2["确诊总数"] = df2["确诊总数"].fillna(0)  # 使用0填充缺测值
    df2.to_csv('实时疫情/世界确诊人数统计排名_2022.'+str(i)+'.1.csv', index=False, float_format='%.2f')



