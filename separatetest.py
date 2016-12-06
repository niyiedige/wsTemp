from linkcrawler1 import link_crawler
from getinfo import getinfo
from input import inputfromexcel
from output import output

raws=inputfromexcel('input.xlsx','info')
outputlist=[]

for raw in raws:
    data1=link_crawler(raw['link'],raw['interlinkregex'],raw['finallinkregex'])
    print(data1)