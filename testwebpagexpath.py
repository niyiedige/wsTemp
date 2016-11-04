from bs4 import BeautifulSoup
import requests
from lxml import html
#need selenimum
from selenium import webdriver
from clearstr import clearstr
driver1=webdriver.PhantomJS()

link='http://egfbank.zhiye.com/zpdetail/310063745?p=3%5E4'
driver1.get(link)
page=requests.get(link)
code=page.status_code
soup=BeautifulSoup(page.content, "lxml")
#print(soup.prettify())
print(code)
scarpeinfo=[]
web=driver1.page_source
tree = html.fromstring(web)
xpath='/html/body/div[5]/div[2]/div/div/div[1]/span/text()'
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