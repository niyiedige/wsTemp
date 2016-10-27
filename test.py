from linkcrawler1 import link_crawler
import urllib.parse
#link_crawler('http://job.abchina.com/htmlfile/29810jobPublish.jsp','jobPublish','jobDetails')
link = urllib.parse.urljoin('http://job.abchina.com/htmlfile/29810jobPublish.jsp', "htmlfile/262102jobDetails.jsp'")
print(link)