import datetime as DT
import re
#need a fliter for dup
#a fliter for uncessay jobs
def fliter1(info):
    datetemp = re.sub("[^0-9,-]", "", info[7])

    if datetemp=='':
        return 1
    else:
        date1 =datetemp[0:10]
        today = DT.datetime.today()
        line=DT.datetime(2016,1,1)

        date=DT.datetime.strptime(date1,'%Y-%m-%d')
        if date>=today:
            info[8]="Deadline"
            return 1
        elif date <= line :
            return 0
        else:
            info[8] = "Post date"
            return 1
