import csv
import pandas as pd
class Local:
    def __init__(self,posX,posY,idArray):
        self.posX=posX
        self.posY=posX
        self.idArray=idArray

def graphMaker(listGrafico):
    orderGrafico=pd.DataFrame(listGrafico,columns=["Quantidade","No Repeticoes"])
    orderGrafico.sort_values("Quantidade",inplace=True)
    orderGrafico=orderGrafico.groupby("Quantidade").sum()
    orderGrafico.to_csv("hist.csv")
def readcsv():	
    ifile = open("OD_2017.csv", "r")
    reader = csv.reader(ifile, delimiter=",")

    rownum = 0	
    a = []

    for row in reader:
        a.append (row)
        rownum += 1
    
    ifile.close()
    return a

def main():
    table=readcsv()
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
        if (len(dictValores[w][1:])>0):
            listGrafico.append([len(dictValores[w][1:]),1])
    graphMaker(listGrafico)
if __name__ == "__main__":
    main()