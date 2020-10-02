from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

with open("kaptnpeng.txt","rb") as f:
    text = f.read().decode("utf-8")

wordcould = WordCloud(width=1920, height=1200)

STOPWORDS.add('und')
STOPWORDS.add('Und')
STOPWORDS.add('oder')
STOPWORDS.add('du')
STOPWORDS.add('Du')
STOPWORDS.add('Doch')
STOPWORDS.add('dich')
STOPWORDS.add('bist')
STOPWORDS.add('der')
STOPWORDS.add('das')
STOPWORDS.add('zu')
STOPWORDS.add('die')
STOPWORDS.add('doch')
STOPWORDS.add('ein')
STOPWORDS.add('Und')
STOPWORDS.add('dir')
STOPWORDS.add('es')
STOPWORDS.add('DOCH')

wordcould.generate(text)
plt.imshow(wordcould, interpolation='bilinear')
plt.axis('off')
plt.show()
# 