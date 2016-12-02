from linkcrawler1 import link_crawler
from getinfo import getinfo

import requests
from outputjson import outputprep
import json
from inputcsv import inputfromexcel

def scrape():
    raws=inputfromexcel('/home/ubuntu/crawler/jobcrawler/input11.csv')
    outputlist=[]

    resulttemp=[]
    for raw in raws:
        data1=link_crawler(raw['link'],raw['interlinkregex'],raw['finallinkregex'])
        z=getinfo(raw,data1)
        resulttemp +=z
    result=outputprep(resulttemp)
    payload = {"data":{"query":{"results":result}}}
    headers = {'content-type': 'application/json'}
    resp = requests.post('http://47.90.61.239:8000/api/v1/jobpost/', data=json.dumps(payload), headers=headers)

scrape()

    #add another getinfo,add a loop function or crawling funciton
    # to change output ,you should change input like company
    #use different method for list of job
    #output needed to be updated
