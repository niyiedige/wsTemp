from disk_cache import DiskCache
from downloader import Downloader
from lxml import html
from clearstr import clearstr
from fliter import fliter1
from urllib.parse import urlparse
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
        cache[link]=D(link)
        page = cache[link]["html"]
        tree = html.fromstring(page)

        scarpeinfo=[link,input['company'],input['CM'],urlparse(link).path]
        for xpath in targetxpath:
            if xpath!=None:
                #z is constantly changing, can be empty some time
                z=tree.xpath(xpath)
                if z:
                    print(z)
                    t=clearstr(z[0])
                    if t=="":
                        try:
                            t=clearstr(z[1])
                            scarpeinfo.append(t)
                        except IndexError:
                            scarpeinfo.append('Destination empty')

                    else:
                        scarpeinfo.append(t)
                else:
                    scarpeinfo.append('xpath empty')

            else:
                scarpeinfo.append('Not available')
        if fliter1(scarpeinfo)==1:
            joblist.append(scarpeinfo)
        else:
            pass
    return joblist
#print(getinfo(sss))

    #4.generate a new out put datacollection
    #returm it
