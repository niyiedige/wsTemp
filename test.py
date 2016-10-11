import datetime as DT
import urllib.request
import requests
from lxml import html
from bs4 import BeautifulSoup
from disk_cache import DiskCache
today = DT.date.today()
week_ago = today - DT.timedelta(days=7)
print(week_ago)
cache = DiskCache()
page=requests.get('http://career.cmbchina.com/Campus/Position.aspx?id=10297')
#request = urllib.request.Request('http://career.cmbchina.com/Campus/Position.aspx?id=10297')
#opener =  urllib.request.build_opener()
#response = opener.open(request)
#htl = response.read()
#tree=html.fromstring(htl)

soup=BeautifulSoup(page.content,"lxml")
print(soup.prettify)
#z=tree.xpath('//*[@id="rightdiv"]/div/div[1]/text()')
#print(z)