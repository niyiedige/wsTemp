import json


def outputprep(output):
    result1=[]
    for output1 in output:
        d = {}
        d["Link"] = output1[0]
        d["Company"] = output1[1]
        d["CM"] = output1[2]
        d["Title"] = output1[3]
        d["Department"] = output1[4]
        d["Location"] = output1[5]
        d["date"] = output1[6]
        d["Time Type"] = output1[7]
        d["Job Type"] = output1[8]
        result1.append(d)
    return result1


