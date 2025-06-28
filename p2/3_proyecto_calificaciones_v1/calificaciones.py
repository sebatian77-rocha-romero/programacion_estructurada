'''
listaa=[
        ["Ruben", 10.0, 8.9, 9.21]
        ["Andres", 10.0, 10.0, 10.01],
        ["Maria", 10.0, 10.0, 10.0]

        ]
'''


lista=[]

def borrarpantalla():
    import os
    os.system("cls")

def esperartecla():
    input("\n\toprima cualquier tecla para continuar... ")

def menu_principal():
    print("eliga una opcion porfavor")
    print("1.- Agregar" \
        "\n 2.- mostrar" \
        "\n 3.- calcular promedios" \
        "\n 4.- buscar calificaciones" \
        "\n 5.- salir"
        )
    opcion=input("Ingrese una opción(1-4): ")
    return opcion

def agregar_calificaciones(lista):
    borrarpantalla()
    print("\t\n Agregar calificaciones \n\t")
    nombre=input("Nombre del alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1, 4):
        continua=True
        while continua:
            try:
                #calificaciones.append=(float (input(f"calificacion {i}:")))
                cal=float(input(f"calificacion {i}: "))
                if cal>=0 and cal <=10:
                    continua=False
                    calificaciones.append(cal)
            except ValueError:
                print("ingrese un valor numerico")
    lista.append([nombre] + calificaciones)
    print("\t\n Accion realizada con exito\t\n")


def mostrar_calificaciones(lista):
    borrarpantalla()
    print("\t\n Mostrar calificaciones \n\t")
    if len(lista)>0:
        print("Nombre  calif1  calif2  calif3")
        print("---------------------------------------")
        print(f"{"Nombre":<15}{"calif1":<10}{"calif2":<10}{"calif3":<10}")
        for fila in lista:
            print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
        print("-"*30)
        print(f"Son {len(lista)} alumnos")

    else:
        print("No hay calificaciones en el sistema")


def calcular_calificaciones(lista):
    borrarpantalla()
    print("Promedios de Alumnos")
    promedio_clase=0
    alumnos=0
    if len(lista)>0:
        print(f"{"Nombre" :<15}{"Promedio":<10}")
        print("-"*30)
        for fila in lista:
            promedio=((fila[1])+(fila[2])+(fila[3]))/3
            print(f"{fila[0]:<15}{promedio:<10}")
            promedio_clase+=promedio
            alumnos+=1
        print("-"*30)
        print(f"Son {len(lista)} alumnos y tienen un promedio de {promedio_clase/alumnos}")
    else:
        print("No hay calificaiones en el sistema")


def buscar_calificaciones(lista):
    borrarpantalla()
    cal_encontradas=0
    print("\nbuscar calificaciones\n")
    nombre=input("ingresa el nombre a buscar: ").lower().strip()
    if len(lista)>0:
        print(f"{"::Nombre::":<15}{"::calif1::":<10}{"::calif2::":<10}{"::calif3::":<10}")
        print("-"*30)

        for fila in lista:
            if fila[0].lower() == nombre:
                print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
                print("-"*30)
                cal_encontradas+=1

        print(f"son {cal_encontradas} alumnos")
    else:
        print("no se encontro alumnos con este nombre")



         

'''
def calcular_promedios():
    borrarpantalla()
    print("\t\n Calcular calificaciones \n\t")
    if len(lista)>0:
        print("---------------------------------------")
        print(f"{"Nombre":<15}{"promedio":<10}")
        print("-"+30)
        for fila in lista:
            nombre=fila[0]
            promedio={fila{i}+fila{2}+fila{3}}/2
            
            
            pomedio_general=+promedio
            print(f"el promedio general del grupo es "({promedio_general}))
        print("-"+30)
        print(f"Son {len(lista)} alumnos")

    else:
        print("No hay calificaciones en el sistema")

'''

'''def agregar_calificaciones(calificaciones):
    borrarpantalla()
    print("\t\n Agregar calificaciones \n\t")
    calificaciones.append=({"nombre": input("\ningresa el nombre de la persona").upper().strip()})
    calificaciones.append=({"caloificacion 1": input("\ningresa la calificacion 1").upper().strip()})
    calificaciones.append=({"calificacion 2": input("\ningresa la calificacion 2").upper().strip()})
    calificaciones.append=({"calificacion 3": input("\ningresa la calificacion 3").upper().strip()})
    print("\t\n .:: LA OPERACION SE REALIZO CON EXITO ::. ")

'''
'''
def mostrar_calificaciones():
    print("\t\n Agregar calificaciones \n\t")
    if len(mostrar_calificaciones) >0:

        float
'''    