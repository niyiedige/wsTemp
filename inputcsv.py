import csv



def inputfromexcel(inputfile_str):
    with open(inputfile_str, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        listofdic = []
        count=0
        for row in spamreader:
            count+=1

            datastructure = {}

            xpathlist = [row[3], row[4], row[5],
                         row[6], row[7], ]
            datastructure.update({'link': row[0]})
            datastructure.update({'company': row[1]})
            datastructure.update({'career_level': row[2]})
            datastructure.update({'interlinkregex': row[8]})
            datastructure.update({'finallinkregex': row[9]})
            datastructure.update({'xpathlist': xpathlist})
            listofdic.append(datastructure)

        return (listofdic)

