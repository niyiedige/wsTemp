import datetime as DT
from lxml import html
import requests
from linkcrawler1 import link_crawler
'''
today = DT.date.today()
week_ago = today - DT.timedelta(days=7)
print(week_ago)

page=requests.get('http://job.icbc.com.cn/ICBC/%E4%BA%BA%E6%89%8D%E6%8B%9B%E8%81%98/default.htm')
html1=html.fromstring(page)
a=html1.xpath('//*[@id="ctl00_Content_Plan1_GVStudent_ctl03_HyperLink2"]')
print(a)
'''
z=link_crawler('http://job.abchina.com/rio/index.do?action=openHome','jobPublish.jsp','toPublish')
print(z)
