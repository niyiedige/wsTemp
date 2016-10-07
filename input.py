import time
import openpyxl
from openpyxl import load_workbook
start_time = time.time()


#1,2,3,4,5,6
def inputfromexcel(inputfile_str,worksheetname_str):
    #dic operation :default_data['item3'] = 3 or default_data.update({'item3': 3},......)
    listofdic = []
    try :
        wb=load_workbook(filename=inputfile_str)
        worksheet=wb[worksheetname_str]
    except FileNotFoundError:
        print("input wrong")
    except KeyError:
        print("input wrong")
    else:
        pass
    count=0
    while True:

        num=count+2
        numstr=str(num)
        if worksheet["C"+numstr].value==None:
            count=0
            break
        datastructure = {}
        xpathlist = [worksheet["C"+numstr].value,worksheet["D"+numstr].value,worksheet["E"+numstr].value,worksheet["F"+numstr].value,worksheet["G"+numstr].value,worksheet["H"+numstr].value,]
        datastructure.update({'link': worksheet["A"+numstr].value})
        datastructure.update({'company': worksheet["B"+numstr].value})
        datastructure.update({'interlinkregex': worksheet["I" + numstr].value})
        datastructure.update({'finallinkregex': worksheet["J" + numstr].value})
        datastructure.update({'xpathlist': xpathlist})
        count += 1
        listofdic.append(datastructure)

    return(listofdic)
    #it's a list of dic

#print("--- %s seconds ---" % (time.time() - start_time))
#print(inputfromexcel('input.xlsx','info'))

#still need parameters for different website