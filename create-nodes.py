nodesFile = open('nodes.csv', 'w')

def processData():
    for line in file('nodes-temp.csv', 'r'):
        if len(line) > 1:
            nodesFile.write(line)

processData()
nodesFile.close()


