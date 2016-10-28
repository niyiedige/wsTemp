import re
import urllib.parse
import urllib.request
import requests

import threading
from lxml import html
from downloader import Downloader
from bs4 import BeautifulSoup,SoupStrainer
import time
start_time = time.time()

def link_crawler(seedurllist,interlinkregex,finallinkregex):
  #  result=crawlqueue(seedurllist,interlinkregex,finallinkregex,maxdepth)
    SLEEP_TIME=2
    max_threads=10
    threads = []
    crawlqueue = [seedurllist]
    inputdepth=3
    D=Downloader()
    targetqueue = []

    seen = {seedurllist: 0}
    def crawler():
        while True:
            print(threading.currentThread().getName(), 'Starting')
            try:
                url=crawlqueue.pop()
            except IndexError:
                print(threading.currentThread().getName(), 'Not Starting')
                break
            else:
                '''
                page = requests.get(url)
                if page.status_code!=200:
                    print(url,page.status_code)
                html = page.text
                '''
                page=D(url)
##need to change utf-8 to header.charset
                html = page['html']
                depth = seen[url]
                if depth != inputdepth:
                    for link in get_links(html):
                        if re.search(finallinkregex, link):
                            link = urllib.parse.urljoin(seedurllist, link)
                            if link not in seen:
                                seen[link] = depth + 1
                                targetqueue.append(link)
                                crawlqueue.append(link)
                            # there should be a optional loop
                                #for interregex in inter...
                        elif interlinkregex:
                            if re.search(interlinkregex, link):
                                link = urllib.parse.urljoin(seedurllist, link)
                                if link not in seen:
                                    seen[link] = depth + 1
                                    crawlqueue.append(link)


    while threads or crawlqueue:
        # the crawl is still active
        for thread in threads:
            if not thread.is_alive():
                # remove the stopped threads
                threads.remove(thread)
        while len(threads) < max_threads and crawlqueue:
            # can start some more threads
            thread = threading.Thread(target=crawler)
            thread.setDaemon(True)  # set daemon so main thread can exit when receives ctrl-c
            thread.start()
            threads.append(thread)
        # all threads have been processed
        # sleep temporarily so CPU can focus execution on other threads
        time.sleep(SLEEP_TIME)
    return(targetqueue)


def get_links(html):
    b = []
    try:
        soup=BeautifulSoup(html.decode('utf-8','ignore'),"lxml")
    except AttributeError:
        soup = BeautifulSoup(html, "lxml")
    for a in soup.find_all('a', href=True):
        b.append(a.get('href'))
    print(b)
    print("something")
    wait = input("PRESS ENTER TO CONTINUE.")
    #return requested links from html by re
#   regex=re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    '''
    regex = re.compile('<a[^>]+href=["\'](.*?)[>]', re.IGNORECASE)
    try:
        a=regex.findall(html)
    except TypeError:
        z=html.decode("utf-8")
        a = regex.findall(z)
    regex1=re.compile('[/](.*?)[,]', re.IGNORECASE)
    c=[]
    print(a)
    for A in a:
       b=regex1.findall(A)
       c+=b

    print(c)
    print("something")
    wait = input("PRESS ENTER TO CONTINUE.")
    #three line above for testing
    # to spot javescript


    for link in a:
        if re.search("/",link):
            b.append(link)
        elif re.search('=',link):
            b.append(link)
   # print(regex.findall(html))
   # print(b)
'''
    return b