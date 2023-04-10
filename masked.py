#!/usr/bin/env python
"""
Minimal Example
===============

Generating a square wordcloud from the US constitution using default arguments.
"""

import os

from os import path
from wordcloud import WordCloud
import jieba
import jieba.analyse
import re

def keep_chinese(text):
    chinese_pattern = re.compile(r'[^\u4e00-\u9fa5]')
    return chinese_pattern.sub('', text)


from collections import Counter
import matplotlib.pyplot as plt

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'chat.txt'),encoding='utf-8').read()

text = keep_chinese(text)


words = jieba.cut(text)
top_k = 3000
tags = jieba.analyse.extract_tags(text, topK=top_k)

text_high = ' '.join(tags)

# Generate a word cloud image
# wordcloud = WordCloud().generate(text_high)

stopwords = ["的","是","了","如何",'什么','一个','一篇','哪些','口吻','引用','关于','怎么','哪里','消息',
             '怎么','数组','用颜','可以','中午','起来','休息','进行','想要','不是'
             ,'然后','中文','每个','两个','早点','一下','可爱','群友','一路平安'] # 去掉不需要显示的词

wc = WordCloud(font_path="msyh.ttc",
                         width = 4200,
                         height = 4200,
                         background_color='white',
                         font_step=2,
                         min_font_size=6,
                         max_words=300,
                         stopwords=stopwords).generate(text_high)



# plt.imshow(wc, interpolation='bilinear')# 用plt显示图片
# plt.axis("off")  # 不显示坐标轴
# plt.show() # 显示图片
# The pil way (if you don't have matplotlib)
image = wc.to_image()
image.show()
image.save("wordcloud.png")