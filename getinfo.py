from disk_cache import DiskCache
from downloader import Downloader
from lxml import html
from clearstr import clearstr
#from input import inputfromexcel

sss={"targeturls":["http://job.ccb.com/ccbjob/cn/job/notice_info.jsp?infoId=87571875&planCode=20150410&bankName=%B0%B2%BB%D5%CA%A1%B7%D6%D0%D0"],"xpathlist":['//*[@id="data"]/table/tr[2]/td/p[8]/font'],'company':'123'}

def getinfo(datestructure_dic,targeturls):
    #1.download,cache page
    #2.get xpathlist
    #3.get the infomation needed
    D=Downloader()
    cache=DiskCache()
    input=datestructure_dic
    targetlist=targeturls
    targetxpath=input["xpathlist"]
    joblist=[]
    outputdata={input['company']:joblist}

    #can use pop here for multithread
    for link in targetlist:
        scarpeinfo = []
        cache[link]=D(link)
        page = cache[link]["html"]
        tree = html.fromstring(page)
        tempinfo=[]
        scarpeinfo=[link,input['company']]
        for xpath in targetxpath:
            if xpath!=None:
                #z is constantly changing, can be empty some time
                z=tree.xpath(xpath)
                try:
                    if z:
                        t=clearstr(z[0])
                        if t=="":
                            t=clearstr(z[1])
                    scarpeinfo.append(t)
                except UnboundLocalError:
                    print('t is empty,somthing wrong with xpath or link')
                    break

            else:
                scarpeinfo.append('Not available')
    # data structure something wrong,change the dictionary with company into a list
        joblist.append(scarpeinfo)
    #info with a company tag
    return joblist
#print(getinfo(sss))

    #4.generate a new out put datacollection
    #returm it
