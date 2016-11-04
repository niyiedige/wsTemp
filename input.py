from openpyxl import load_workbook

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
        #test for the end of the file
        if worksheet["C"+numstr].value==None:
            count=0
            break
        datastructure = {}
        xpathlist = [worksheet["D"+numstr].value,worksheet["E"+numstr].value,worksheet["F"+numstr].value,worksheet["G"+numstr].value,worksheet["H"+numstr].value,]
        datastructure.update({'link': worksheet["A"+numstr].value})
        datastructure.update({'company': worksheet["B"+numstr].value})
        datastructure.update({'CM': worksheet["C" + numstr].value})
        datastructure.update({'interlinkregex': worksheet["I" + numstr].value})
        datastructure.update({'finallinkregex': worksheet["J" + numstr].value})
        datastructure.update({'xpathlist': xpathlist})
        count += 1
        listofdic.append(datastructure)

    return(listofdic)
    #it's a list of dic

#print(inputfromexcel('input.xlsx','info'))

#still need parameters for different website