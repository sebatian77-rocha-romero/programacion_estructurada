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
print(varios)

#recorrer una lista e imprimir el contenido

#1er forma
for i in paises:
    print(i)

lista=''
for i in paises:
    lista=lista+f"[{i}]"
print (lista+"]")

#2da forma
for i in range(0,4):
    print(paises[i])

lista="["
for i in range(0, len):
    lista+=f"{paises[i]},"
print(lista+"[")


#
os.system("cls")
print(paises)
print(numeros)
print(varios)

paises.sort()
print(paises)
numeros.sort()
print(numeros)

#dar vueltas a las listas
varios.reverse()
print(varios)
paises.revers()
print(paises)
numeros.reverse()
print(numeros)

#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
paises.append("Honduras")
print(paises)

#2da forma
paises.insert(1,"Honduras")
print(paises)

paises.sort()
print(paises)

#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
paises.pop(4)
print(paises)

#2da forma 
paises.remove("Honduras")
print(paises)

#Buscar un elemento dentro de la lista
print(paises)

print("Brasil" in paises)

#Contar el numeros de veces que aparece un elemento dentro de una lista

print(numeros)

cuantos=numeros.count(23)
print(cuantos)

numeros.append(23)
cuantos=numeros.count(23)
print(cuantos)

#Conocer la posicion o indice en el que se encuentra un elemento de la lista
paises.reverse()
print(paises)

posicion=paises.index("Canada")
print(f"El valor de Canada lo encontro en la posicion: {posicion}")

#Unir el contenido de una lista dentro de otra lista
os.system("clear")
print(numeros)
numeros2=[100,200]

print(numeros2)

#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente


numeros.extend(numeros2)
print(numeros)

numeros.sort()
print(numeros)

numeros.reverse()
print(numeros)

#buscar un elemento dentro de una lista
r="españa" in paises
print(r)

#insertar, añadir, agregar un elemento a una lsita
os.system("cls")
print(paises)

#1er forma
paises.append ("mexico")
print(paises)

#2sa forma
paises.inser(1, "mexico")
print(paises)

#norrar, eliminar
paises.pop(0)
print(paises)
 
#unir el contenido
os.system("cls")
print(numeros)

numeros2=(100, 200)
print(numeros2)