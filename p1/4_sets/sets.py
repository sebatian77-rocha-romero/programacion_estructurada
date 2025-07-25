"""
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
"""import os
os.system("cls")

varios={True, "cadena", 23,3.1416}
print(varios)

paises={"mexico", "españa", "brasil", "canada", "canada"}
print(paises)

paises.add("mexicoo")
print(paises)

varios.pop
print(varios)

varios.remove("cadena")"""

#ejemplo crear un programa que solicite los email de los alumnos de la utd. almacenar en una lista y 
# posteriormente mostrar los email sin duplicarlos

email=[]
resp="si"

while resp== "si":
    email.append(input("escribe un email: "))
    resp=input("deseas agregar otro email?" ).lower()

print(email)
email_set=set(email)
print(email_set)
email=list(email_set)
print(email)
