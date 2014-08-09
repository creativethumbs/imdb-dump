import string
import re
nodesFile = open('nodes.csv', 'w')
relsFile = open('rels.csv', 'w')
#everythingFile = open('everything2.tsv', 'w')

nodesArray = list('b')*300000

def processData():
    start = True

    global nodesArray

    for line in file('actor-rels.tsv', 'r'):
        if start:
            nodesFile.write("name\tnumber:string:nodeid\tl:label\n")
            relsFile.write("number:string:nodeid\tnumber:string:nodeid\ttype\n")
            start = False
        else:
            linearray = line.split('\t')
            actorname = re.findall(r"['\"](.*?)['\"]", linearray[0])[0].strip()
            actorid =  re.findall(r"['\"](.*?)['\"]", linearray[1])[0]
            actorid = int(actorid) + 200000
            film = re.findall(r"['\"](.*?)['\"]", linearray[2])[0]
            filmid =  re.findall(r"['\"](.*?)['\"]", linearray[3])[0]
            filmid = int(filmid)
            
            if nodesArray[actorid] == 'b':
                nodesArray[actorid] = actorname+'\t'+str(actorid)+"\tactor\n"

            if nodesArray[filmid] == 'b':
                nodesArray[filmid] = film+'\t'+str(filmid)+"\tmovie\n"

            relsFile.write(str(actorid)+"\t"+str(filmid)+"\tACTED_IN\n")

    start = True

    for line in file('director-rels.tsv', 'r'):
        if start:
            start = False
        else:
            linearray = line.split('\t')
            directorname = re.findall(r"['\"](.*?)['\"]", linearray[0])[0].strip()
            directorid =  re.findall(r"['\"](.*?)['\"]", linearray[1])[0]
            directorid = int(directorid) + 100000
            film = re.findall(r"['\"](.*?)['\"]", linearray[2])[0]
            filmid =  re.findall(r"['\"](.*?)['\"]", linearray[3])[0]
            filmid = int(filmid)
            
            if nodesArray[directorid] == 'b':
                nodesArray[directorid] = directorname+'\t'+str(directorid)+"\tdirector\n"

            if nodesArray[filmid] == 'b':
                nodesArray[filmid] = film+'\t'+str(filmid)+"\tmovie\n"

            relsFile.write(str(directorid)+"\t"+str(filmid)+"\tDIRECTED\n")

def createNodes():
    global nodesArray
    for i, item in enumerate(nodesArray):
        if item != 'b':
            nodesFile.write(item)


processData()
createNodes()
nodesFile.close()
relsFile.close()


