import string
import re
relsFile = open('rels.csv', 'w')
     
def createRels():
    relsFile.write("start\tend\ttype\n")

    for line in file('everything2.tsv', 'r'):
        linearray = line.split('\t')
        directorid =  linearray[1]
        actorid =  linearray[3]
        filmid =  linearray[5][:-1]

        relsFile.write(directorid+"\t"+filmid+"\tDIRECTED\n")
        relsFile.write(actorid+"\t"+filmid+"\tACTED_IN\n")


createRels()
relsFile.close()


