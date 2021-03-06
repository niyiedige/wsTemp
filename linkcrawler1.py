import re
import urllib.parse
import urllib.request
import time
import threading
from lxml import html
from downloader import Downloader
from urllib.parse import urlparse
import socket
import gc


def link_crawler(seedurllist,interlinkregex,finallinkregex):
  #  result=crawlqueue(seedurllist,interlinkregex,finallinkregex,maxdepth)
    SLEEP_TIME=2
    max_threads=10
    threads = []
    crawlqueue = [seedurllist]
    inputdepth=3
    D=Downloader()
    targetqueue = []

    done=[]
    seen = {seedurllist: 0}
    def crawler():
        counttt=0
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
                try:
                    page=D(url)

##need to change utf-8 to header.charset
                    html = page['html']
                    depth = seen[url]
                    if depth != inputdepth:
                        for link in get_links(html):
                            if re.search(finallinkregex, link):
                                link = urllib.parse.urljoin(seedurllist, link)

                                try:
                                    c=urlparse(link).netloc
                                    d=urlparse(link).path
                                    truelink=urllib.parse.urljoin(urlparse(link).netloc, urlparse(link).path)
                                    if truelink not in done or "id" in urlparse(link).query:
                                        done.append(truelink)
                                        if link not in seen:
                                            seen[link] = depth + 1
                                            targetqueue.append(link)
                                    # there should be a optional loop
                                        #for interregex in inter...
                                    else:
                                        counttt += 1
                                        print("dup")
                                        pass
                                except AttributeError:

                                    print(counttt)
                                    if link not in seen:
                                        seen[link] = depth + 1
                                        targetqueue.append(link)

                            elif interlinkregex:
                                if re.search(interlinkregex, link):

                                    link = urllib.parse.urljoin(seedurllist, link)
                                    try:
                                        truelink = urllib.parse.urljoin(urlparse(link).netloc, urlparse(link).path)
                                        if truelink not in done or "branch" in urlparse(link).query or "jlt" in urlparse(link).query:
                                            done.append(truelink)
                                            if link not in seen:
                                                seen[link] = depth + 1
                                                crawlqueue.append(link)
                                                # there should be a optional loop
                                                # for interregex in inter...
                                        else:
                                            counttt += 1
                                            print("dup")
                                            pass
                                    except AttributeError:

                                        print(counttt)
                                        if link not in seen:
                                            seen[link] = depth + 1
                                            crawlqueue.append(link)

                except socket.error:
                    print("AAAAAAAAAAAAAAAAAAAAAAAAAAA")

                    pass


    while threads or crawlqueue :
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
    #return requested links from html by re
#   regex=re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    if type(html)!=str :
        html=html.decode('utf-8')
    regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    a=regex.findall(html)
    # to spot javescript
    b=[]

    for link in a:
        if re.search("/",link):
            b.append(link)
        elif re.search('=',link):
            b.append(link)
   # print(regex.findall(html))
   # print(b)

    return b