import string
import re
nodesFile = open('nodes-temp.csv', 'w')
everythingFile = open('everything2.tsv', 'w')

nodesArray = list('b')*300000

def processData():
    start = True
    prevActor = ""

    global nodesArray

    for line in file('everything.tsv', 'r'):
        if start:
            nodesFile.write("name\tnumber:string:nodeid\tl:label\n")
            start = False
        else:
            linearray = line.split('\t')
            directorname = re.findall(r"['\"](.*?)['\"]", linearray[0])[0].strip()
            directorid =  re.findall(r"['\"](.*?)['\"]", linearray[1])[0]
            directorid = int(directorid) + 100000
            actorname = re.findall(r"['\"](.*?)['\"]", linearray[2])[0].strip()
            actorid =  re.findall(r"['\"](.*?)['\"]", linearray[3])[0]
            actorid = int(actorid) + 200000
            film = re.findall(r"['\"](.*?)['\"]", linearray[4])[0]
            filmid =  re.findall(r"['\"](.*?)['\"]", linearray[5])[0]
            filmid = int(filmid)
            
            if nodesArray[directorid] == 'b':
                #nodesArray[directorid] = directorname+"\tdirector\t"+str(directorid-100000)
                nodesArray[directorid] = directorname+'\t'+str(directorid)+"\tdirector"

            if nodesArray[actorid] == 'b':
                #nodesArray[actorid] = actorname+"\tactor\t"+str(actorid-200000)
                nodesArray[actorid] = actorname+'\t'+str(actorid)+"\tactor"

            if nodesArray[filmid] == 'b':
                #nodesArray[filmid] = film+"\tmovie\t"+str(filmid)
                nodesArray[filmid] = film+'\t'+str(filmid)+"\tmovie"

            everythingFile.write(directorname+"\t"+str(directorid)+"\t"+actorname+"\t"+str(actorid)+"\t"+film+"\t"+str(filmid)+"\n")

def createNodes():
    global nodesArray
    for i, item in enumerate(nodesArray):
        if item != 'b':
            nodesFile.write(item+'\n')
        else:
            nodesFile.write('\n')


processData()
createNodes()
nodesFile.close()
everythingFile.close()


