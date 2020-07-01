import csv
import pandas as pd
import random
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

def contGen(graphFinal):
    contGen={}
    for k in graphFinal.keys():
        contGen[k]=random.uniform(0, 1)
    return contGen
def resGen(graphFinal):
    recProb={}
    for k in graphFinal.keys():
        recProb[k]=random.uniform(0, 1)
    return recProb
def bfs_connected_component(graph, start,y,r):

    explored = []

    queue = [start]
    connectedNeighbours=[]
    succep=[]
    infec=[]
    rem=[]
    contProb={}
    recProb={}
    removed=[]
    infected=[]
    succeptible=list(graph.keys())
    timeLine=[]
    while queue:

        
        node = queue.pop(0)
        if node not in explored:
         
            explored.append(node)
            infected.append(node)
            try:
                succeptible.remove(node) 
            except:
                print('derp')
            neighbours = graph[node]

            for neighbour in neighbours:
                queue.append(neighbour)

            if (random.uniform(0, 1)>=float(r)):
                if (node in infected):
                    infected.remove(node)
                    removed.append(node)
            else:
                listProbInfected=graph[node]
                for i in listProbInfected:
                    #print(listProbInfected)
                    if (random.uniform(0, 1)<=float(y) and i not in removed and i in succeptible):
                        if (node not in infected and node not in removed):
                            infected.append(i)
                            succeptible.remove(i)   
            timeLine.append([len(succeptible),len(infected),len(removed)])
            print([len(succeptible),len(infected),len(removed),(len(removed)+len(infected)+len(succeptible))])
    orderGrafico=pd.DataFrame(timeLine)
    orderGrafico.to_csv("grafo5_20707.csv")

 # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']
def main():
    g = { "a" : ["d"],
        "b" : ["c"],
        "c" : ["b", "d", "e"],
        "d" : ["a", "c","f"],
        "e" : ["c"],
        "f" : ["d"]

    }
    table=readcsv('traducao2.txt')

    listGrafico=[]

    graphFinal=graphMaker(table)



    orderGrafico=pd.DataFrame(listGrafico)
    listGrafico=bfs_connected_component(graphFinal, '5431',0.7,0.8)

        #print(len(infected))
        #print("-------")
        #print(len(removed))



if __name__ == "__main__":
    main()