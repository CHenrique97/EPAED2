import csv
import pandas as pd
class Local:
    def __init__(self,posX,posY,idArray):
        self.posX=posX
        self.posY=posX
        self.idArray=idArray

def graphMaker(graphTable):
    dictGraph={}
    #cria o dicionario que sera nosso grafo
    for x in range(3,len(graphTable)):
        try :
            dictGraph[graphTable[x][1]].append(graphTable[x][0])
        except: 
            dictGraph[graphTable[x][1]]=[graphTable[x][0]]
    return dictGraph





def readcsv(filePath):	
    ifile = open(filePath, "r")
    reader = csv.reader(ifile, delimiter=" ")

    rownum = 0	
    a = []

    for row in reader:

        a.append (row)
        if (len(row)>1):
            a.append([row[1],row[0]])
        rownum += 1
    
    ifile.close()
    #print(a)
    return a


def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
    connectedNeighbours=[]
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
            print(neighbours)
            connectedNeighbours.append(len(neighbours))
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return connectedNeighbours

 # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']
def main():
    g = { "a" : ["d"],
        "b" : ["c"],
        "c" : ["b", "d", "e"],
        "d" : ["a", "c","f"],
        "e" : ["c"],
        "f" : ["d"]

    }


    table=readcsv('traducao1.txt')

    listGrafico=[]

    graphFinal=graphMaker(table)
    listGraficoAppended=[]
    listGrafico=bfs_connected_component(graphFinal, '0')
    
    orderGrafico=pd.DataFrame(listGrafico)
    orderGrafico.to_csv("grafo4.csv")
if __name__ == "__main__":
    main()