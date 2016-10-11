from urllib.parse import urlparse,urlsplit
import urllib.request
import urllib
import random
import time
from datetime import datetime, timedelta
import socket
from selenium import webdriver
from disk_cache import DiskCache
import requests

DEFAULT_AGENT = 'al'
DEFAULT_DELAY = 5
DEFAULT_RETRIES = 1
DEFAULT_TIMEOUT = 60
cacheplace=DiskCache()
# dynamic:downloader parameter
#proxy is not implemented
class Downloader:
    def __init__(self, delay=DEFAULT_DELAY, user_agent=DEFAULT_AGENT, proxies=None, num_retries=DEFAULT_RETRIES,
                 timeout=DEFAULT_TIMEOUT, opener=None, cache=cacheplace,dynamic=None):
        socket.setdefaulttimeout(timeout)
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies
        self.num_retries = num_retries
        self.opener = opener
        self.cache = cache
        self.dynamic=dynamic

    def __call__(self, url):
        dynamic=self.dynamic
        result = None
        if self.cache:
            try:
                result = self.cache[url]
            except KeyError:
                # url is not available in cache
                print("not in cache")
                pass
            else:
                print("in cache")
                # proble, here
                if result['code']==None:
                    result = None
                elif self.num_retries > 0 and 500 <= result['code'] < 600:
                    # server error so ignore result from cache and re-download
                    result = None
        if result is None:
            print("is none")
            # result was not loaded from cache so still need to download
            self.throttle.wait(url)
            proxy = random.choice(self.proxies) if self.proxies else None
            headers = {'User-agent': self.user_agent}
            if dynamic==1:
                result =self.dynamic_download(url,num_retries=self.num_retries)
            else:
                result = self.download(url, headers, proxy=proxy, num_retries=self.num_retries)
            if self.cache:
                # save result to cache
                self.cache[url] = result
        return result
    def dynamic_download(self,url,num_retries):
        print('Dynamic Downloading:', url)
        driver1 = webdriver.PhantomJS()
        driver1.get(url)
        response2=requests.get(url)
        try:
            html = driver1.page_source

            code = response2.status_code
        except Exception as e:
            print('Download error:', str(e))
            html = ''
            if hasattr(e, 'code'):
                code = e.code
                if num_retries > 0 and 500 <= code < 600:
                    # retry 5XX HTTP errors
                    return self.dynamic_download(url, num_retries - 1)
            else:
                code = None
        return {'html': html, 'code': code}

    def download(self,url, headers, proxy, num_retries, data=None):
        print('Downloading:', url)
        request = urllib.request.Request(url, data, headers or {})
        opener = self.opener or urllib.request.build_opener()

        if proxy:
            proxy_params = {urlparse(url).scheme: proxy}
            opener.add_handler(urllib.request.ProxyHandler(proxy_params))
        try:
            response = opener.open(request)

            html = response.read()

            code = response.code
        except Exception as e:
            print('Download error:', str(e))
            html = ''
            if hasattr(e, 'code'):
                code = e.code
                if num_retries > 0 and 500 <= code < 600:
                    # retry 5XX HTTP errors
                    return self.download(url, headers, proxy, num_retries - 1, data)
            else:
                code = None
        return {'html': html, 'code': code}


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
