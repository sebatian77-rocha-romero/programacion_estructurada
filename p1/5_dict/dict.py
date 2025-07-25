"""
 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos. Es decir es algo parecido como los Objetos 

  Tambien se conoce como un arreglo asosiativo u Objeto JSON

  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""
import os
os.system("cls")

paises=["Mexico", "Brasil", "España", "Canada"]

pais1={
          "nombre":"Mexico", 
          "capital":"CDMX",
          "poblacion":1200000,
          "idioma":"español",
          "sttus":True
          
        }

pais2={
          "nombre":"Brasil", 
          "capital":"Brasilia",
          "poblacion":1400000,
          "idioma":"portugues",
          "sttus":True
        }

pais3={
          "nombre":"Canada", 
          "capital":"Otawa",
          "poblacion":1000000,
          "idioma":["ingles", "frances"],
          "sttus":True
        }

#funciones u operaciones con los dict u objetos
print(pais1)

for i in pais1:
    print(f"{i}={pais1[i]}")

#agregar un atributo
pais1["altitud"]=3000

for i in pais1:
    print(f"{i}={pais1[i]}")

