import os
path='D:/log/'
saida=path+'ArquivoConsolidado.csv'
lista = os.listdir(path)

fileSaida = open(saida, 'w')

for f in lista:
    if f[len(f)-4:]=='.txt':
        f = path+f
        file = open(f,'r')
        for line in file:
            fileSaida.write(line.replace('|',' , '))
        fileSaida.write('\n')
        file.close()

fileSaida.close()
