import csv
import pandas as pd
class Local:
    def __init__(self,posX,posY,idArray):
        self.posX=posX
        self.posY=posX
        self.idArray=idArray

def graphMaker(listGrafico,graphTable):
    dictGraph={}
    #cria o dicionario que sera nosso grafo
    for x in range(1,len(graphTable)):
        dictGraph[graphTable[x][1]]=[]
    for x in range(0,len(listGrafico)):#remove as duplicatas do mesmo local
        formattedList=list(dict.fromkeys(listGrafico[x].idArray))
        for y in formattedList:
            insertGraph=formattedList
            insertGraph.remove(y)            
            dictGraph[y]=insertGraph
    return dictGraph


def readcsv(filePath):	
    ifile = open(filePath, "r")
    reader = csv.reader(ifile, delimiter=",")

    rownum = 0	
    a = []

    for row in reader:
        a.append (row)
        rownum += 1
    
    ifile.close()
    return a

def main():
    table=readcsv('OD_2017.csv')
    graphTable=readcsv('Ids_OD2017.csv')
    listValores=[]
    dictValores={}
    listObjectValores=[]
    listGrafico=[]
    #seleciona as colunas da tabela que nos interessam
    for x in range(1,len(table)):      
        listValores.append([table[x][88],table[x][89],table[x][43]])
    #organiza e agrupa os ids que frequentam os mesmos lugares
    for y in listValores:
        
        if y[0] in dictValores :
            dictValores[y[0]].append(y[2])
        else:
            dictValores[y[0]]=[y[1]]
    #coloca os valores do dicionario em um lista contendo os objetos
    for w in dictValores.keys():
        listObjectValores.append(Local(int(w),int(dictValores[w][0]),dictValores[w][1:]))
    graphFinal=graphMaker(listObjectValores,graphTable)
    for w in graphFinal.keys():
        listGrafico.append(len(graphFinal[w]))
    orderGrafico=pd.DataFrame(listGrafico,columns=["Quantidade"])
    orderGrafico.to_csv("hist2.csv")
if __name__ == "__main__":
    main()