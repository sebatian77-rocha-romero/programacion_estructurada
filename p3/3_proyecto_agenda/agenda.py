import mysql.connector
from mysql.connector import Error
import os

agenda={}

def borrarpantalla():
    os.system("cls")

def esperartecla():
    input("presione una tecla para continuar")

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_agenda"

        )
        return conexion
    except Error as e:
        print(f"el error que se presento es: {e}")
        return None

def mostrar_menu():
    print("\t\t 📄..::: Sistema de gestion de agenda de contactos :::..📄 \n\t")
    print("\n\t 1️⃣ AGREGAR CONTACTO" \
    "\n\t 2️⃣ MOSTRAR TODOS LOS CONTACTOS" \
    "\n\t 3️⃣ BUSCAR CONTACTO POR SU NOMBRE" \
    "\n\t 4️⃣ MODIFICAR CONTACTO" \
    "\n\t 5️⃣ ELIMINAR CONTACTO" \
    "\n\t 6️⃣ SALIr\t")

    opcion=input(("\n\tElige una opcion (1-6):\t")).upper()
    return opcion

def agregar_contacto(agenda):
    rep = True
    conexionBD=conectar()

    while rep:
        borrarpantalla()
        print("\n\t.::AGREGAR CONTACTO::.\t")

        nombre = input("\nIngrese el nombre: ").upper().strip()

        if nombre in agenda:
            print("\nYa existe este contacto...")
            rep = input("¿Quiere intentar con otro nombre (si/no)? ").lower().strip()
            if rep == "no":
                break
        else:
            tel = input("Ingrese el número de teléfono: ").strip()
            email = input("Ingrese el email: ").strip()
            agenda[nombre] = {"telefono": tel, "email": email}
            try:
                ##### Sql para BD
                cursor=conexionBD.cursor()
                sql="insert into agenda (nombre, tel, email) values ( %s, %s, %s)"
                val=(nombre, tel, email)
                cursor.execute(sql,val)
                conexionBD.commit()
            except Exception as e:
                print(f"\nError al guardar en la base de datos: {str(e)}")
                conexionBD.rollback()
        rep = input("¿Quiere agregar otro contacto (si/no)? ").lower().strip()
        if rep == "no":
            rep = False


def mostrar_contactos(agenda):
    borrarpantalla()
    print("\n\t..:::Mostrar agenda de contactos:::..\t")
    conexionBD= conectar()
    if not conexionBD:
        esperartecla()
        return
    
    try:
        cursor = conexionBD.cursor(dictionary=True)
        cursor.execute("SELECT nombre, tel, email FROM agenda ORDER BY nombre")
        registros = cursor.fetchall()

        if registros:
            print("\n{:<20} {:<15} {:<25}".format("NOMBRE", "TELÉFONO", "EMAIL"))
            print("-"*60)
            for contacto in registros:
                print("{:<20} {:<15} {:<25}".format(
                    contacto['nombre'],
                    contacto['tel'],
                    contacto['email']))

        else:
            print("\t ..::no hay contactos guardados::..")

    except Error as e:
        print(f"no fue posible conectarse...{e}")



def buscar_contacto(agenda):
    borrarpantalla()
    print("\n\t\t .::buscar un contacto::. \n")
    conexionBD=conectar()
    if conexionBD is not None:
        
        try:
            nombre = input("Ingrese el nombre que quiere buscar: ").upper().strip()
            cursor=conexionBD.cursor(dictionary=True)
            sql="select nombre, tel, email from agenda where nombre=%s"
            cursor.execute(sql, (nombre,))
            registro = cursor.fetchone()
            if registro:
                print(f"Nombre: {registro['nombre']} \nTelefono: {registro['tel']}\n Email: {registro['email']}")
                print("-"*50)

            else:
                print("\nEl contacto no fue encontrado en la base de datos... ")
        except Error as e:
            print(f"\nError al buscar contacto: {e}")

def modificar_contacto(agenda):
    borrarpantalla()
    print("\n\t..::: MODIFICAR CONTACTO :::..\t")
    print("="*50)
    conexionBD=conectar()
    if conexionBD is not None:
        nombre=input("Ingresa el nombre del contacto a modificar: ").upper().strip()
        cursor=conexionBD.cursor()
        sql="select * from agenda where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
    if registros:
      print("Mostrar la agenda")
      print(f"{'ID':<10}{'Nombre':<15}{'tel':<15}{'email':<15}")
      print(f"-"*60)
      for agenda in registros:
            print(f"{agenda[0]:<10}{agenda[1]:<15}{agenda[2]:<15}{agenda[3]:<15}")
            print(f"-"*80) 
            resp=input(f"¿Deseas borrar la agenda {nombre}? (Si/No): ").lower().strip()
            if resp == "si":
              # Obtener nuevos datos
                try:
                    nuevos_datos = {
                    "nombre": input("\nNuevo nombre: ").upper().strip(),
                    "tel": input("Nueva telefona: ").upper().strip(),
                    "email": input("Nuevo email: ").upper().strip()
                    }
                
                    # Actualizar en la base de datos
                    sql_update = """
                    UPDATE agenda 
                    SET nombre = %s, tel = %s, email = %s
                    WHERE id = %s
                    """
                    val_update = (
                        nuevos_datos["nombre"],
                        nuevos_datos["tel"],
                        nuevos_datos["email"],
                        agenda[0]  # ID de la película
                    ) 
                
                    cursor.execute(sql_update, val_update)
                    conexionBD.commit()
                    print("\n¡Contacto actualizado correctamente!")

                except Exception as e:
                    print(f"\nError al actualizar el contacto: {e}")
                
            else:
                print("\nOperación cancelada")
    else:
        print("\nError: La película no existe en el sistema")
        

def eliminar_contacto(agenda):
    borrarpantalla()
    print("\n\t..::: ELIMINAR CONTACTO :::..\t")
    print("="*50)
    
    conexionBD = conectar()
    if not conexionBD:
        print("Error al conectar a la base de datos")
        esperartecla()
        return

    try:
        if not conexionBD or not conexionBD.is_connected():
            print("Error: Conexión no disponible")
            return
        
        nombre = input("\nIngrese el nombre del contacto a eliminar: ").upper().strip()
        encontrado = False
        
        #base de datos
        with conexionBD.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM agenda WHERE nombre = %s", (nombre,))
            registro = cursor.fetchone()
            
            if registro:
                print("Mostrar el Contacto")
                print(f"{'ID':<10}{'Nombre':<15}{'Teléfono':<15}{'Email':<15}")
                print(f"-"*80)
                print(f"{registro['id']:<10}{registro['nombre']:<15}{registro['tel']:<15}{registro['email']:<15}")
                print(f"-"*80)

                print("-"*50)
                
                resp = input("\n¿Desea eliminar este contacto de la base de datos? (si/no): ").lower().strip()
                if resp == "si":
                    cursor.execute("DELETE FROM agenda WHERE nombre = %s", (nombre,))
                    conexionBD.commit()
                    print("\nContacto eliminado de la base de datos")
                    encontrado = True
        
        if not encontrado:
            print("\nEl contacto no fue encontrado en la base de datos")

    except Error as e:
        print(f"\nError al eliminar contacto: {e}")