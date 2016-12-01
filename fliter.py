import datetime as DT
import re
#need a fliter for dup
#a fliter for uncessay jobs
def fliter1(info):
    datetemp = re.sub("[^0-9,-]", "", info[6])
    if info[4]=="xpath empty":
            return 0
    if datetemp=='':
        return 1
    else:
        date1 =datetemp[0:10]
        today = DT.datetime.today()
        line=DT.datetime(2016,1,1)

        date=DT.datetime.strptime(date1,'%Y-%m-%d')
        if date>=today:
            info[7]="Deadline"
            return 1
        elif date <= line :
            return 0
        else:
            info[7] = "Post date"
            return 1
def fliter2(string):
    Techjobkeyword=[]
    Otherjobkeyword=[]
    if any(ext in string for ext in Techjobkeyword):
        return("tech")
    elif any(ext in string for ext in Otherjobkeyword):
        return("other")
    else:
        return("Finance")