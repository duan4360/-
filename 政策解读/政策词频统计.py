# 导入相应的库
import pandas as pd
import  os
import jieba
import sys
sys.path.append('E:\python-graph-core-1.8.2')

all_words = []  #分词得到的单词列表
file1 = open("政策解读\停用词.txt", 'r',encoding='utf-8',errors='ignore')
stop_words = file1.readlines()   #停用词列表
for i in range(len(stop_words)):
    stop_words[i] = stop_words[i][:-1]
stop_words.append('\n')
stop_words.append('\t')
stop_words.append('2020')
stop_words.append(' ')
stop_words.append(' ')

def fenci(path,filename):
    file1 = open(path, 'r',encoding='utf-8',errors='ignore')
    str1 = file1.readlines()
    article = ""
    for i in str1:
        article += i
    seg_list = jieba.lcut(article, cut_all=False)  # 返回列表类型，使用jieba.cut返回的是
    count=0
    while(count<len(seg_list)):
        if seg_list[count] in stop_words:
            seg_list.remove(seg_list[count])
        else:
            count+=1
    file1.close()
    return seg_list

#主函数执行开始
file_abs_path = '政策解读\china_policy'

for dirpath,dirnames,filenames in os.walk(file_abs_path):
    for i in filenames:
        t = fenci(dirpath+"\\"+i,i)
        for j in t:
            all_words.append(j)


show_words = pd.Series(all_words).value_counts().head(50).keys()  #将打印的词语转为列表以供wordcloud使用
text_cut = " ".join(show_words) #将词语连接成字符串
f_context = open("政策解读\词频统计高频词.txt", 'w',encoding='UTF-8')
f_context.write(text_cut)



