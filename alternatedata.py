from lxml import html
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import requests
import datetime
import openpyxl

targetlist={"YiYangZhi":'http://appstore.huawei.com/app/C10401368','TongHuaShun':'http://appstore.huawei.com/app/C2861','DaZhiHui':'http://appstore.huawei.com/app/C10148748'}
scarpeinfo = []
names=["YiYangZhi",'TongHuaShun','DaZhiHui']
#http://blog.csdn.net/u014595019/article/details/48445223

for name in names:
    driver1 = webdriver.PhantomJS()
    driver1.get(targetlist[name])
    tree = html.fromstring(driver1.page_source)
    xpath='//*[@id="bodyonline"]/div[2]/div[4]/div[1]/div/div/div[1]/ul[1]/li[2]/p[1]/span[2]/text()'
    a=tree.xpath(xpath)
    c=re.sub("[^0-9]", "", a[0])
    print(c)
    b=name
    scarpeinfo.append(c)

now=datetime.datetime.now()
enddate=str(now.year)+str(now.month)+str(now.day+1)
startdate=str(now.year)+str(now.month)+str(now.day)
url='http://quotes.money.163.com/service/chddata.html?code=0000001&start='+startdate+'&end='+enddate+'&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;VOTURNOVER;VATURNOVER '
z=requests.get(url)
quote=z.text.split('\r\n')[1]
market=quote.split(',')
marketdata=[]
scarpeinfo.append(market[0])
scarpeinfo.append(market[4])
scarpeinfo.append(market[5])
scarpeinfo.append(market[8])
scarpeinfo.append(market[9])

now=datetime.datetime.now()
enddate=str(now.year)+str(now.month)+str(now.day+1)
wb = openpyxl.load_workbook('result.xlsx')
ws=wb.active
dd=int(enddate)
for col in ws.iter_cols(min_row=dd-20161018, max_col=8, max_row=dd-20161018):
    for cell in col:
        cell.value=scarpeinfo.pop()
wb.save('result.xlsx')
print(scarpeinfo)
