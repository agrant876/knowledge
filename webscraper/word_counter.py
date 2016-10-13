import sys

sys.path.append('/Users/andrewgrant/anaconda3/lib/python3.5/site-packages')

from lxml import html
import requests

page = requests.get('https://en.wikipedia.org/wiki/Kingston,_Jamaica')
#tree = html.fromstring(page.content)


if population in page.text:
    print('yes')

#wordcount = {}
#for word in page.text.split():
 #   if word not in wordcount:
  #      wordcount[word] = 1
   # else:
    #    wordcount[word] += 1

#for word, value in wordcount.items():
 #   if value >= 25:
  #      print(word,value)





