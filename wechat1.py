# -*- coding:utf-8 -*-
import itchat
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import os
import numpy as np
import PIL.Image as Image
import jieba
# 登录
itchat.auto_login()
# 获取好友列表
friends = itchat.get_contract(update=True)[0:]
# 初始化计数器，有男有女，当然，有些人是不填的
'''
male = female = other = 0

# 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
# 1表示男性，2女性
sig=[]
for i in friends[1:]:
	sig.append(i["Signature"])
	sex=i["Sex"]
	if sex == 1:
		male += 1
	elif sex == 2:
		female += 1
	else:
		other+=1
	# 总数算上，好计算比例啊～
	total = len(friends[1:])

##好了，打印结果
print (u"男性好友：%.2f%%" % (float(male) / total * 100))
print (u"女性好友：%.2f%%" % (float(female) / total * 100))
print (u"其他：%.2f%%" % (float(other) / total * 100))
print(sig)
'''
tList=[]
for i in friends:
    signature = i["Signature"].replace(" ","").replace("span","").replace("class","").replace("emoji","")
    rep=re.compile("1f\d.+")
    signature=rep.sub("",signature)
    tList.append(signature)

text="".join(tList)
wordlist_jieba=jieba.cut(text,cut_all=True)
wl_space_split=" ".join(wordlist_jieba)
d = os.path.dirname(__file__)
alice_coloring = np.array(Image.open(os.path.join(d,"wechat_cloud.png").replace('\\','/')))
my_wordcloud = WordCloud(background_color="white", max_words=20000, mask=alice_coloring,
                         stopwords=STOPWORDS.add("said"),
                         max_font_size=300, random_state=50).generate(wl_space_split)
image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
#plt.imshow(alice_coloring,cmap=plt.cm.gray)
plt.axis("off")
plt.show()
