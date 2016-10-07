import re
import urllib.parse
import urllib.request
import requests
import time
import threading
from lxml import html
from downloader import Downloader

start_time = time.time()

def link_crawler(seedurllist,interlinkregex,finallinkregex,maxdepth):
    max_depth=maxdepth
    #why list list?
    targetqueue=[]
    crawlqueue=[seedurllist]
    seen = {seedurllist: 0}

    while crawlqueue:
        url=crawlqueue.pop()
      #  D=Downloader()
       # result=D(url)
      #  htmltemp=result["html"]
       # html1=html.fromstring(htmltemp)
        page=requests.get(url)
        html = page.text
        depth = seen[url]
        count=0
        if depth != max_depth:
            for link in get_links(html):
                count+=1
                print(count)
                if re.search(finallinkregex,link):
                    link = urllib.parse.urljoin(seedurllist, link)
                    if link not in seen:
                        seen[link] = depth + 1
                        targetqueue.append(link)
                #there should be a optional loop
                elif re.search(interlinkregex,link):
                    link=urllib.parse.urljoin(seedurllist,link)
                    if link not in seen:
                        seen[link] = depth + 1
                        crawlqueue.append(link)

    return targetqueue




def get_links(html):
    #return requested links from html by re
    regex=re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    print(regex.findall(html))
    return regex.findall(html)


print(link_crawler("http://career.cmbchina.com/Campus/Campus.aspx","branch=","Position.aspx",2))
print("--- %s seconds ---" % (time.time() - start_time))