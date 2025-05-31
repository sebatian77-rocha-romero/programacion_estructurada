'''
lista(Array)
son colecciones o conjunto de datos / valores bajo
un mismo nombre, para acceder a los valores se hace con un indice numerico

Nota; sus valores si son modificables

la lista es una coleccion ordenada y modificable. permite miembros duplicados
'''

import os
os.system("cls")
#funciones mas comunes en las listaas

paises={"mexico", "breasil", "españa", "canada"}
numeros=[23, 45, 8, 24,23, 56]
varios={"hola", 2, 1416, 33, True}

#imprimir el contenido de una lista 

print(paises)
print(numeros)

#recorrer una lista e imprimir el contenido

#1er forma
for i in paises:
    print(i)

#2da forma
for i in range(0,4):
    print(paises[i])