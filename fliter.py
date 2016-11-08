import datetime as DT
import re
info=['http://career.cmbchina.com/Campus/Position.aspx?id=10297', 'cmbchina', 'C', '管理培训生（海外专场--公司金融方向）', '总行', '深圳（轮岗地：深圳、北京、上海、广州、武汉、苏州、南京、天津、重庆）', '2016-12-04', 'Not available']


def fliter1(info):
    datetemp = re.sub("[^0-9,-]", "", info[6])

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
