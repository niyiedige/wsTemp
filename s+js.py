from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import html
#need to include phantomjs in the PATH

link = 'https://l3com.taleo.net/careersection/l3_ext_us/jobsearch.ftl'

driver1 = webdriver.PhantomJS()
driver1.get('http://career.cmbchina.com/Campus/Position.aspx?id=10231')
print(driver1.page_source)
driver1.set_window_size(1120, 550)
s = BeautifulSoup(driver1.page_source,"lxml")
b=html.fromstring(driver1.page_source)
print(b.xpath('//*[@id="rightdiv"]/div/div[1]/text()'))



driver1.quit()



