from linkcrawler1 import link_crawler
from getinfo import getinfo

import requests
from outputjson import outputprep
import json
from inputcsv import inputfromexcel
from output import output

#to run on server/pc change the line on scrape and downloader, delete output ,change cache expire time
def scrape():
    raws=inputfromexcel('C:\python\wetemp\wsTemp-niyiedige-patch-3/input11.csv')
#    raws=inputfromexcel('/home/ubuntu/crawler/jobcrawler/input11.csv')
    outputlist=[]

    resulttemp=[]
    try:
        for raw in raws:
            data1=link_crawler(raw['link'],raw['interlinkregex'],raw['finallinkregex'])
            z=getinfo(raw,data1)
            resulttemp +=z
    finally:
        result=outputprep(resulttemp)
        payload = {"data":{"query":{"results":result}}}
        headers = {'content-type': 'application/json'}
        resp = requests.post('http://47.90.61.239:8000/api/v1/jobposts/', data=json.dumps(payload), headers=headers)
        output(resulttemp)
scrape()

    #add another getinfo,add a loop function or crawling funciton
    # to change output ,you should change input like company
    #use different method for list of job
    #output needed to be updated
