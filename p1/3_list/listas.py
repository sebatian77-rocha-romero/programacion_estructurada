import os
#ejemplo1 crear una lista de numeros e imprimir el contenido

os.system("cls")

num=[1,2,3,4,5,6,7,8,9,10]
variable=""
print(num)

for i in num:
    variable+=f"{i},"
print(f"{variable}]")

variable="["
for i in range(0, len(num)):

    variable+=f"{num[i]},"

lista="["
for i in num:
  lista+=f"{i},"
print(f"{lista}]")

lista="["
for i in range(0,len(num)):
  lista+=f"{num[i]},"
print(f"{lista}]")

lista="["
i=0
while i<len(num):
  lista+=f"{num[i]},"
  i+=1
print(f"{lista}]")

#ejemplo2 crear una lista de palabras y posteriormente buscar la coincidencia de una palbra 
os.system("cls")
pal=["casa", "manzana", "auto","computadora","lapiz"]
print(pal)
palabra_buscar=input("dame la palabra a buscar en la lista: ")


#1er forma
if palabra_buscar in pal:
    print("si encontro la palabra en la lista")
else:
    print("no se encontro la palabra en la lista")

#2da forma

encontro=False
for i in pal:
    if palabra_buscar in pal:
        print("si encontro la palabra en la lista")
    else:
        print("no se encontro la palabra en la lista")

#3ra. forma
encontro=False
for i in range(0,len(pal)):
 if pal[i]==palabra_buscar:
    encontro=True 
    
if encontro:
   print("SI se encontro la palabra en la lista")

else:
     print("NO se encontro la palabra en la lista")  



#enemplo3 añadir elementos a la lista
pal.append("videojuego")
print(pal)

opc="si"
while opc=="si":
    num.append(float(input("Dame un numero entero o decimal: ")))
    opc=input("¿Desear agregar otro numero a las lista (si/no)? ").lower()

print(num)   



#3er.
encontro=False
cuentas=0
posiciones=[]

for i in pal:
    if pal=={i}==palabra_buscar:
        encontro=True
        cuentas+=1
        posiciones=pal.append(pal.index(i))

for i in pal:
    if palabra_buscar in pal:
        print("si encontro la palabra en la lista")
    else:
        print("no se encontro la palabra en la lista")


#ejemplo4 crear una lista multimensional para almacenar los nombres y telefonos de unos contactos"agenda"
nom=["jose", "maria","erick", "judy"]
tel = ["618 123 4567", "618 987 6543", "618 555 5320", "618 760 4321"]
agenda=[]

for i in range(len(nom)):
    contacto = [nom[i], tel[i]]
    agenda.append(contacto)
print(agenda)


agenda = [
    ["carlos", "6184536734"],
    ["carlos v", "6186438146"],
    ["carlosvk", "6188352758"]
]


print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])

cadena=""
for r in range(0,3):
    for c in range(0,2):
      cadena+=f"{agenda[r][c]}, "
    cadena+="\n"     
print(cadena) 