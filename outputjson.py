import json
import os
import re
from urllib.parse import urlsplit

def url_to_path(url):
    """Create file system path for this URL
    """
    components = urlsplit(url)
    # when empty path set to /index.html
    path = components.path
    if not path:
        path = '/index.html'
    elif path.endswith('/'):
        path += 'index.html'
    filename = components.netloc + path + components.query
    # replace invalid characters
    filename = re.sub('[^/0-9a-zA-Z\-.,;_ ]', '_', filename)
    # restrict maximum number of characters
    filename = "/".join(segment[0:250] for segment in filename.split("/"))
    seg=filename.split("/")
  #  dir = os.path.dirname(__file__)
    dir='C:\python\wetemp\wsTemp-niyiedige-patch-3'
    temp = os.path.join(dir,"cache",*seg)
    return temp

def outputprep(output):
    result1=[]
    for output1 in output:
        d = {}
        d["link"] = output1[0]
        d["company"] = output1[1]
        d["career_level"] = output1[2]
        d["title"] = output1[3]
        d["department"] = output1[4]
        d["location"] = output1[5]
        d["date"] = output1[6]
        d["time_type"] = output1[7]
        d["job_type"] = output1[8]
        path=url_to_path(output1[0])
        if os.path.exists(path):
            pass
        else:
            result1.append(d)
    return result1


