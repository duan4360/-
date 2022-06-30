import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df=pd.read_csv("世界卫生情况统计.csv",sep=",",encoding="utf-8")#编码格式使用记事本查看
df.head()
x = df["国家"].values.tolist()
y1 = df['医生数/万人'].values.tolist()
y2 = df['病床数/千人'].values.tolist()
y3 = df['每百万人确诊人数'].values.tolist()
for i in range(len(y3)):
    y3[i] = float(y3[i])/10000

x1_width = range(0, len(x))
x2_width = [i + 0.2 for i in x1_width]
x3_width = [i + 0.2 for i in x2_width]

#定义函数来显示柱子上的数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.-0.08, 1.02*height, '%.2f'% height, size=10, family="Times new roman")

plt.figure(figsize=(14, 6))
cm = plt.bar(x1_width, y1, lw=0.5, fc="#ADD8E6", width=0.2, label="医生数/万人")
autolabel(cm)   #添加数值
cm = plt.bar(x2_width, y2, lw=0.5, fc="#808080", width=0.2, label="病床数/千人")
autolabel(cm)
cm = plt.bar(x3_width, y3, lw=0.5, fc="#A52A2A", width=0.2, label="每百人确诊人数")
autolabel(cm)


plt.xticks(range(0, 10), x)
plt.legend(loc='upper left')
plt.title("世界卫生情况统计")

#设置字体为楷体
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
plt.show()
