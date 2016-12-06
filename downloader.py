from urllib.parse import urlparse,urlsplit
import random
import time
from datetime import datetime, timedelta
import socket
from disk_cache import DiskCache
from selenium import webdriver
import requests
import gc
DEFAULT_AGENT = 'al'
DEFAULT_DELAY = 5
DEFAULT_RETRIES = 1
DEFAULT_TIMEOUT = 120
cacheplace=DiskCache()
global count
count=0

class Downloader:
    def __init__(self, delay=DEFAULT_DELAY, user_agent=DEFAULT_AGENT, proxies=None, num_retries=DEFAULT_RETRIES,
                 timeout=DEFAULT_TIMEOUT, opener=None, cache=cacheplace):
        socket.setdefaulttimeout(timeout)
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies
        self.num_retries = num_retries
        self.opener = opener
        self.cache = cache

    def __call__(self, url):
        result = None
        if self.cache:
            try:
                result = self.cache[url]
            except KeyError:
                # url is not available in cache
                pass
            else:
                if result['code']!=None:
                    if self.num_retries > 0 and 500 <= result['code'] < 600:
                        # server error so ignore result from cache and re-download
                        result = None
                else: result = None
        if result is None:
            # result was not loaded from cache so still need to download
            self.throttle.wait(url)
            proxy = random.choice(self.proxies) if self.proxies else None
            headers = {'User-agent': self.user_agent}
            result = self.download(url, headers, proxy=proxy, num_retries=self.num_retries)
            if self.cache:
                # save result to cache
                self.cache[url] = result
        return result

    def download(self, url, headers, proxy, num_retries, data=None):
        print('Downloading:', url)
        gc.collect()
        driver1 = webdriver.PhantomJS(
            executable_path='/home/ubuntu/crawler/env/bin/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
        #driver1 = webdriver.PhantomJS()
        try:

        #
            driver1.get(url)
            response = requests.get(url)
            html = driver1.page_source

            code = response.status_code
        except Exception as e:
            print('Download error:', str(e))
            global count
            count+=1
            if count>2:
                html='1'
                count=0
            else:
                html = ''
            code=None
        finally:
            driver1.close()
            driver1.quit()
        return {'html': html, 'code': code}


'''
    if hasattr(e, 'code'):
        code = e.code
        if num_retries > 0 and 500 <= code < 600:
            # retry 5XX HTTP errors
            return self.download(url, headers, proxy, num_retries - 1, data)
    else:
        code = None
'''

class Throttle:
    """Throttle downloading by sleeping between requests to same domain
    """

    def __init__(self, delay):
        # amount of delay between downloads for each domain
        self.delay = delay
        # timestamp of when a domain was last accessed
        self.domains = {}

    def wait(self, url):
        """Delay if have accessed this domain recently
        """
        domain = urlsplit(url).netloc
        last_accessed = self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.now()
