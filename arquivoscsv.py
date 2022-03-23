### Para manipular o arquivo csv ###
# importamos a biblioteca csv

import csv
from unittest import findTestCases

## Criar um arquivo csv com as funções writer e writerow

##  Gerenciador de contexto de arquivo

with open('arquivos/nomes.csv','w',newline="") as fcsv:
    escrever = csv.writer(fcsv,delimiter=',')
    escrever.writerow(("Nome","Sobrenome","Idade"))
    escrever.writerow(("João","Ricardo",36))
    escrever.writerow(("Pedro","Cunha",23))
    
## Ler o arquivo CSV

with open('arquivos/nomes.csv','r') as fcsv2:
    ler= csv.reader(fcsv2)
    
    ## Transformar en uma lista
    
    lista1= list(fcsv2)
    
    for c in lista1:
        print(c)
        
fcsv2.close()
    
    ## Transformar em dicionário
    
with open('arquivos/nomes.csv','r') as fcsv3:
    ler_dic= csv.DictReader(fcsv3)
    
    #for d in ler_dic:
        #print(d)
        
    #for d in ler_dic:
        #print(d["Nome"])
        
fcsv3.close()

with open('arquivos/arquivo1.csv','r') as fcsv4:
    ler= csv.reader(fcsv4)
    
    for i in ler:
        print(i)
        
        # Vamos converter os dados do csv para lista
        
    lista2= list(ler)

    print(lista2)
            