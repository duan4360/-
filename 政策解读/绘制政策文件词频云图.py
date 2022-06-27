from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import PIL
import numpy as np

# 词云形状
image1 = PIL.Image.open('政策解读\中国地图.jpeg')
MASK = np.array(image1)

file1 = open("政策解读\词频统计高频词.txt", 'r',encoding='utf-8',errors='ignore')
text_cut = file1.read()

# 绘制词云
word_cloud = WordCloud(font_path="simsun.ttc",
                       background_color="white",
                       width=2500, height=3000,
                       mask=MASK,  # 指定词云的形状
                       )
word_cloud.generate(text_cut) #将词语导入

# 运用matplotlib展现结果
plt.subplots(figsize=(12, 8))
plt.imshow(word_cloud)
plt.axis("off")
plt.show()
