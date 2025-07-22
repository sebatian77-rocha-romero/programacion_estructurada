import mysql.connector
from mysql.connector import Error

lista=[]

def borrarpantalla():
    import os
    os.system("cls")

def esperartecla():
    input("\n\toprima cualquier tecla para continuar... ")

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_calificaciones"

        )
        return conexion
    except Error as e:
        print(f"el error que se presento es: {e}")
        return None

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
    conexionBD=conectar()
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
    ##### Sql para BD
    cursor=conexionBD.cursor()
    sql="insert into calificaciones (nombre, cal_1, cal_2, cal_3) values ( %s, %s, %s, %s)"
    val = (nombre, calificaciones[0], calificaciones[1], calificaciones[2])

    cursor.execute(sql, val)
    conexionBD.commit()
    lista.append([nombre] + calificaciones)
    print("\n\t::: ¡LA OPERACIÓN SE REALIZÓ CON EXÍTO! :::")



def mostrar_calificaciones():
    borrarpantalla()
    print("\nLISTADO DE CALIFICACIONES\n")
    conexionBD= conectar()
    if not conexionBD:
        esperartecla()
        return
    
    try:
        cursor = conexionBD.cursor(dictionary=True)
        cursor.execute("SELECT * FROM calificaciones ORDER BY nombre")
        registros = cursor.fetchall()
        
        if registros:
            print(f"{'Nombre':<20}{'C1':<6}{'C2':<6}{'C3':<6}")
            print("-"*40)
            for reg in registros:
                print(f"{reg['nombre']:<20}{reg['cal_1']:<6}{reg['cal_2']:<6}{reg['cal_3']:<6}")
            print(f"\nTotal registros: {len(registros)}")
        else:
            print("No hay calificaciones registradas")
            
    except Error as e:
        print(f"Error al consultar: {e}")
    finally:
        if conexionBD.is_connected():
            cursor.close()
            conexionBD.close()
    


def calcular_promedios():
    borrarpantalla()
    print("\t...:CÁLCULO Y REGISTRO DE PROMEDIOS:...")
    print("="*60)
    
    conexionBD = conectar()
    if not conexionBD:
        esperartecla()
        return

    try:
        cursor = conexionBD.cursor(dictionary=True)
        
        cursor.execute("SELECT id, nombre, cal_1, cal_2, cal_3 FROM calificaciones ORDER BY nombre")
        alumnos = cursor.fetchall()
        
        if not alumnos:
            print("\nNo hay alumnos registrados en el sistema")
            esperartecla()
            return
        
        print("\n{:<15} {:<8} {:<8} {:<8} {:<10}".format(
            "ALUMNO", "CAL_1", "CAL_2", "CAL_3", "PROMEDIO"))
        print("-"*70)
        
        for alumno in alumnos:
            try:
                cal1 = float(alumno['cal_1'])
                cal2 = float(alumno['cal_2'])
                cal3 = float(alumno['cal_3'])
                promedio = round((cal1 + cal2 + cal3) / 3, 2)
                
                print("{:<15} {:<8.1f} {:<8.1f} {:<8.1f} {:<10.2f}".format(
                    alumno['nombre'], cal1, cal2, cal3, promedio))
                
                update_sql = "UPDATE calificaciones SET promedio = %s WHERE id = %s"
                cursor.execute(update_sql, (promedio, alumno['id']))
                
            except (ValueError, TypeError):
                print("{:<15} {:<8} {:<8} {:<8} {:<10}".format(
                    alumno['nombre'], "Inválido", "Inválido", "Inválido", "Error"))
                continue
        
        conexionBD.commit()
        print("-"*50)
        print("\n\t.::Promedios calculados y guardados exitosamente::. \t")
        
    except Exception as e:
        print(f"\nError general: {str(e)}")
        conexionBD.rollback()
    finally:
        if conexionBD and conexionBD.is_connected():
            cursor.close()
            conexionBD.close()
    
    esperartecla()




def buscar_calificaciones(lista):
    borrarpantalla()
    cal_encontradas=0
    print("\nbuscar calificaciones\n")
    conexionBD=conectar()
    if conexionBD!=None:
        try:
            nombre=input("ingresa el nombre a buscar: ").lower().strip()
            cursor=conexionBD.cursor()
            sql="select * from calificaciones where LOWER(nombre) LIKE %s"  # Cambiado a LIKE y LOWER
            val=(f"%{nombre}%",)
            cursor.execute(sql,val)
            registros=cursor.fetchall()
            if registros:
                print(f"{'Nombre':<15}{'Calif1':<10}{'Calif2':<10}{'Calif3':<10}")  # Simplificado encabezado
                print("-"*45)

                for registro in registros:
                    print(f"{registro[1]:<15}{registro[2]:<10}{registro[3]:<10}{registro[4]:<10}")  # Índices corregidos
                    print("-"*45)
                    cal_encontradas+=1

                print(f"\nTotal encontrados: {cal_encontradas} alumnos")  # Mensaje más claro
        except Error as e:
            print(f"Error en la búsqueda: {e}")
        finally:
            cursor.close()  # Cierre de cursor
            conexionBD.close()  # Cierre de conexión
    else:
        print("Error de conexión a la base de datos")  # Mensaje más preciso

         

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