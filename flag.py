from rlineal import *
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import sys
import math as mt

def F_generadora(mayor, menor, intervalos):

    pos= menor
    Largo_intervalo= (mayor-menor)/intervalos
    lista_aa=[]
    while pos<maxxx:
        lista_aa.append(pos)
        pos=pos+Largo_intervalo
    return lista_aa
    
def open_file(filename=""):
    if filename=="":
        filename = raw_input("Entre el nombre del archivo: ")
    try:
        myfile = open(filename)
    except:
        print ("Archivo %s no encontrado." % filename)
        myfile = open_file()
    return myfile


lista_tuplas = []

arch = open_file(str('datos.txt'))

for linea in arch:

    lista= linea.strip().split(' ')
    tupla_ql= (2*mt.sin(7/120)*float(lista[0]), float(lista[1])*float(lista[1]))
    lista_tuplas.append(tupla_ql)

lista_x=[]
lista_y=[]
    
for i in range(len(lista_tuplas)):
    lista_x.append(lista_tuplas[i][0])
    lista_y.append(lista_tuplas[i][1])


    
R=Regresion(lista_tuplas)
print(R)
tangente= R.pendiente()
interrr= R.intercepto()
maxxx= R.maximo_x()
minnn=R.minimo_x()
ancho=maxxx-minnn
Largo_intervalo=ancho/100

valores_y=[]
valores_x=F_generadora(maxxx, minnn, 100)
for i in range(len(valores_x)):
    new_x= valores_x[i]
    new_y= (tangente*new_x)+interrr
    valores_y.append(new_y)
    



titulo= "Regresion lineal"
fig, ax = plt.subplots()
plt.suptitle(str(titulo))
#plt.margins(x=minnn,x=maxxx)
ax.plot(valores_x, valores_y, 'r-')
plt.xlabel('Datos x', fontsize=16)
plt.ylabel('Datos y',fontsize=16)

plt.plot(lista_x, lista_y, 'bo')
plt.legend(('Regresion lineal', 'Datos entregados'))

tangente=str(tangente)
interrr=str(interrr)
ax.annotate('$y(x) =$'+ tangente[:5]+'$x$'+ '$+($' + interrr[:5] + '$)$',
            xy=(1, 0), xycoords='axes fraction',
            xytext=(-150, 30), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='top', fontsize=15)

plt.savefig("figura2.png")

plt.show()
    




