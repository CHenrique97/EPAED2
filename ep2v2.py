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
        rownum += 1
    
    ifile.close()
    #print(a)
    return a

def main():
    table=readcsv('cenario1.txt')

    listGrafico=[]

    graphFinal=graphMaker(table)
    for w in graphFinal.keys():
        listGrafico.append(len(graphFinal[w])+1)
    orderGrafico=pd.DataFrame(listGrafico,columns=["Quantidade"])
    orderGrafico.to_csv("grafo.csv")
if __name__ == "__main__":
    main()