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
    Techjobkeyword=['工程','技术','网络','运','维','系统','计算机','开发']
    Otherjobkeyword=['代表','秘','司机','柜员','法','绩效','人力']
    if any(ext in string for ext in Techjobkeyword):
        return("tech")
    elif any(ext in string for ext in Otherjobkeyword):
        return("other")
    else:
        return("Finance")