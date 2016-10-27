from bs4 import BeautifulSoup
import requests
from lxml import html
#need selenimum
from clearstr import clearstr
link='http://career.cmbchina.com/Social/Position.aspx?id=8508'
page=requests.get(link)
soup=BeautifulSoup(page.content)
print(soup.prettify())
scarpeinfo=[]

tree = html.fromstring(page.text)
xpath='//*[@id="rightdiv"]/div[1]/div[1]/text()'
if xpath != None:
    # z is constantly changing, can be empty some time
    z = tree.xpath(xpath)
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