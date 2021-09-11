#!/usr/bin/env python

from database import DataBase as DB
from wordcloud import WordCloud
import matplotlib.pyplot as plt

db = DB()

(pset, pwords, nset, nwords) = db.getWordList()
wc = WordCloud(width = 800, height = 800, margin = 0).generate(" ".join(pwords))


plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()


wc2 =  WordCloud(width = 800, height = 800, margin = 0).generate(" ".join(nwords))

plt.imshow(wc2, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()

df = db.getCurrentData()
dfp = df[df.est_positivity == 1]
dfn = df[df.est_positivity == -1]
presults = dfp.groupby("search_key").count()
nresults = dfn.groupby("search_key").count()


