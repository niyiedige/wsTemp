from lxml import html
from linkcrawler1 import link_crawler
from getinfo import getinfo
from input import inputfromexcel
from output import output
import re


raws=inputfromexcel('input.xlsx','info')
outputlist=[]
for raw in raws:
    print(raw['link'])
    print(raw['interlinkregex'])
    print(raw['finallinkregex'])
    data1=link_crawler(raw['link'],raw['interlinkregex'],raw['finallinkregex'])
    print(data1)
    print(1111)
    z=getinfo(raw,data1)
    outputlist+=z

output(outputlist)