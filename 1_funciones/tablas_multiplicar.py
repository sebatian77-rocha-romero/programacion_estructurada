'''
  crear un programa que calcule e imprima la tabla de multiplicar del 2

  resticciones:
  1.-sin estructuras de control
  2.-sin funciones
'''
num=int(input("inserta el numero de la tabla de multiplicar"))

uno=num*1
dos=num*2
tres=num*3
cuatro=num*4
cinco=num*5
seis=num*6
siete=num*7
ocho=num*8
nueve=num*9
diez=num*10

print(f"1 x 2={uno}")
print(f"2 x 2={dos}")
print(f"3 x 2={tres}")
print(f"4 x 2={cuatro}")
print(f"5 x 2={cinco}")
print(f"6 x 2={seis}")
print(f"7 x 2={siete}")
print(f"8 x 2={ocho}")
print(f"9 x 2={nueve}")
print(f"10 x 2={diez}")



'''
crear un programa que calcula e imprimir cualquier tabla de multiplicar
restricciones
1.-con estructuras de control
2.-sin 
'''
num2=int(input("inserta el numero de la tabla de multiplicar"))
for i in range (1,11):
    mult=num2+i
    print(f"{num2} x {i}= {mult} ")


#version 3
'''
crear un programa que calcula e imprimir cualquier tabla de multiplicar
restricciones
1.-con estructuras de control
2.-con funciones
'''

def tabla(numero):
    num3=numero
    respuesta=""
    for i in range (1,11):
        multi=num3+i
        respuesta+=f"\t{num3} x {i} = {multi}\n"
    return=respuesta

num3=int(input("inserta el numero de la tabla de multiplicar"))

    