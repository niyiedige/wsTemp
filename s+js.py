from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import html
#need to include phantomjs in the PATH

link = 'https://l3com.taleo.net/careersection/l3_ext_us/jobsearch.ftl'

driver1 = webdriver.PhantomJS()
driver1.get('http://job.icbc.com.cn/ICBC/%E4%BA%BA%E6%89%8D%E6%8B%9B%E8%81%98/default.htm')
b=html.fromstring(driver1.page_source)
for a in b.xpath('//*[@href]'):
    print(a.get('href'))




driver1.quit()



