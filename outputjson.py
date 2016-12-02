import json


def outputprep(output):
    result1=[]
    for output1 in output:
        d = {}
        d["link"] = output1[0]
        d["company"] = output1[1]
        d["cm"] = output1[2]
        d["title"] = output1[3]
        d["department"] = output1[4]
        d["location"] = output1[5]
        d["date"] = output1[6]
        d["time_type"] = output1[7]
        d["job_type"] = output1[8]
        result1.append(d)
    return result1


