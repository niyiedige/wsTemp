from linkcrawler1 import link_crawler
from getinfo import getinfo
from input import inputfromexcel
from output import output
from outputjson import outputprep
import json

def scarpe():
    raws=inputfromexcel('input.xlsx','info')
    outputlist=[]

    resulttemp=[]
    for raw in raws:
        data1=link_crawler(raw['link'],raw['interlinkregex'],raw['finallinkregex'])
        z=getinfo(raw,data1)
        resulttemp +=z
    result=outputprep(resulttemp)
    j=json.dumps(result,indent=4)
    return j
print(scarpe())

    #add another getinfo,add a loop function or crawling funciton
    # to change output ,you should change input like company
    #use different method for list of job
    #output needed to be updated