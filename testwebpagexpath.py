from bs4 import BeautifulSoup
import requests
from lxml import html
#need selenimum
from selenium import webdriver
from clearstr import clearstr
driver1=webdriver.PhantomJS()

link='http://job.htsc.com.cn/recruitment/job/detail/h/2/jt/3/id/143'
ss=driver1.get(link)
page=requests.get(link)
code=page.status_code
soup=BeautifulSoup(page.content, "lxml")
#print(soup.prettify())
print(code)
scarpeinfo=[]
web=driver1.page_source
tree = html.fromstring(web)

xpath='//*[@id="Nav2"]/div[6]/div[1]/div[2]/text()'
if xpath != None:
    # z is constantly changing, can be empty some time
    z = tree.xpath(xpath)
    print(z)
    if z:
        t = clearstr(z[0])
        if t == "":
            t = clearstr(z[1])

        scarpeinfo.append(t)
    else:
        scarpeinfo.append('xpath empty')

else:
    scarpeinfo.append('Not available')
print(scarpeinfo)
