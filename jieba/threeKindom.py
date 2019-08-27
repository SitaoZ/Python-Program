#-*- coding:utf-8-*-
import jieba
import wordcloud
from scipy.misc import imread

f = open('/Users/zhusitao/Downloads/TheThreeKindom.txt','r',encoding='utf-8')
t = f.read()
f.close()

ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="Hiragino Sans GB.ttc",width=1000,height=700,background_color='white',max_words=15)
w.generate(txt)
w.to_file('wordcloud.png')


{
"max_depth":15,
"min_sample_count":3,
"use_surrogates":TRUE,
"max_categories":10,
"cal_var_importance":TRUE,
"nactive_vars":20,
"max_num_of_tree_in_the_forest":500,
"forest_accuracy":0.0005,
"Training_Percentage":0.7
}


