import os

agenda={}

def borrarpantalla():
    os.system("cls")

def esperartecla():
    input("presione una tecla para continuar")

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

        rep = input("¿Quiere agregar otro contacto (si/no)? ").lower().strip()
        if rep == "no":
            rep = False


def mostrar_contactos(agenda):
    borrarpantalla()
    print("\n\t..:::Mostrar agenda de contactos:::..\t")

    if len(agenda)>0:
        for i in agenda:
            print(f"\tEl contacto: {(i)} : {(agenda[i])}")
    else:
        print("\t ..::no hay contactos guardados::..")


def buscar_contacto(agenda):
    borrarpantalla()
    print("\n\t\t .::buscar un contacto::. \n")
    borrarpantalla()
    print("\n\t..:::BUSCAR CONTACTO:::..\t")

    if not agenda:
        print("NO HAY CONTACTOS")  
    else:
        nombre = input("Ingrese el nombre que quiere buscar: ").upper().strip()
        if nombre in agenda:
            print(f"el contacto: {agenda[nombre]} ")

            
            
            
            

'''
def buscar_contacto(agenda):
    borrarpantalla()
    print("BUSCAR CONTACTO")

    if not agenda:
        print("NO HAY CONTACTOS")  
    else:
        nombre = input("Ingrese el nombre que quiere buscar: ").upper().strip()
        if nombre in agenda:
            print(f"\n{'NOMBRE':<15}{'TELEFONO':<15}{'EMAIL':<15}")  
            print("-"*60)
            print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<15}") 
            print("-"*60)
        else:
            print(f"\nNO HAY CONTACTO CON ESE NOMBRE")
'''
            


def modificar_contacto(agenda):
    borrarpantalla()
    print("\n\t..::: Modificar Contacto :::..\n")
    buscar = input("Ingrese el nombre del contacto a modificar: ").upper().strip()

    if buscar in agenda:
        contacto = agenda[buscar]
        print(f"\nDatos actuales de {buscar}:")
        print(f"Teléfono: {contacto['telefono']}")
        print(f"Email: {contacto['email']}")


        nuevo_valor = input("Ingrese el nuevo número telefónico: ").strip()
        contacto['telefono'] = nuevo_valor
        print("Modificación realizada con éxito.")

        nuevo_valor = input("Ingrese el nuevo email: ").strip()
        contacto['email'] = nuevo_valor
        print("Modificación realizada con éxito.")
     

'''
def modificar_contacto(agenda):
    borrarpantalla()
    print ("Modificar Contactos")
    if not agenda:
        print("No hay contactos en la Agenda")
    else:
        nombre=input("Nombre.del.contacto.a-buscar:.").upper().strip()
        if nombre in agenda:
            print("Valores actuales")
            print(f"Nombre: {nombre} \nTeléfono: {agenda[nombre][0]}\nE-mail:{agenda[nombre][1]}")
            resp=input
            if resp=="si":
                tel=input ("Teléfono:.").upper().strip()
                email=input("E-mail: ").lower().strip()
                agenda [nombre]=[tel,email]
                print ("Acción Realizada con éxito...")

        else:
            print("Este contacot no exite")
'''

def eliminar_contacto(agenda):
    borrarpantalla()
    print("Eliminar contacto")
    if not agenda:
        print("No hay contactos en la agenda")
    else:
        nombre=input("Nombre del contacto a buscar").upper().strip()
        if nombre in agenda:
            print("valores actuales")
            print(f"Nombre: {nombre}\nTelefono: {agenda[nombre]([0])}\nE-mail: {agenda[nombre]([1])}")
            resp=input("¿desea eliminar los valores? (si/no)").lower().strip()
            if resp =="si":
                agenda.pop(nombre)
                print("accion realizada con exito")

        else:
            print("Este contacto no existe")

################################################################################################

'''
def borrar_contacto(agenda):
    borrarpantalla()
    print("\n\t..::: Eliminar Contacto :::..\n")
    buscar = input("Ingrese el nombre del contacto a eliminar: ").upper().strip()

    if buscar in agenda:
        confirmar = input(f"¿Está seguro que desea eliminar a {buscar}? (S/N): ").upper().strip()
        if confirmar == "S":
            del agenda[buscar]
            print("Contacto eliminado exitosamente.")
        else:
            print("Operación cancelada.")
    else:
        print("El contacto no existe.")
        esperartecla()
'''