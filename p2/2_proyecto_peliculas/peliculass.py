peliculas=[ "john wick",
    "john wick: capítulo 2",
    "john wick: capítulo 3",
    "john wick: capítulo 4",
    "el origen",
    "el caballero de la noche",
    "transformers",
    "matrix",
    "gladiador",
    "interestelar",
    "el padrino",
    "el club de la pelea",
    "star war",
    "al filo del mañana",
    "spiderman"]

#dict u objeto los atributos (nombre/categoria/clasificacion/genero/idioma)

'''
pelicula={
        "nombre":","
        "categoria""peliculas"
}
'''

pelicula={}

def borrarpantalla():
    import os
    os.system("cls")

def esperartecla():
    input("\n\toprima cualquier tecla para continuar... ")


def crearpelicula():
    borrarpantalla()
    print("\n\t\t .:: crear peliculas::. \n")
    pelicula.update({"nombre": input("\ningresa el nombre: ").upper().strip()})
    #pelicula["nombre"]=input("\ningrese el nombre").upper().strip()
    pelicula.update({"categoria": input("\ningresa la categoria: ").upper().strip()})
    pelicula.update({"clasificacion": input("\ningresa la clasificacion: ").upper().strip()})
    pelicula.update({"genero": input("\ningresa el genero: ").upper().strip()})
    pelicula.update({"idioma": input("\ningresa el idioma: ").upper().strip()})
    print("\n\t :::LA OPERACION SE REALIZO CON EXITO!:::")


def borrarpelicula():
    borrarpantalla()
    print("\n\t .::Borrar o quitar todas las peliculas::. \n")
    resp=input("deseas quitar o borrar las peliculas del sistema? (si/no)")
    if resp=="si":
        pelicula.clear()
        input("\n\t\t :::. LA OPERACION SE REALIZO CON EXITO :::")

def mostrarpelicula():
    borrarpantalla()
    print("\n\t\t .::mostrar peliculas::. \n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"\t{(i)} : {pelicula[i]}")
    else:
        print("\t ..::no hay peliculas en el sistema::..")

def agregarcaracteristicaspeliculas():
    borrarpantalla()
    print("\n\t.:: Agregar Características a las Películas ::.\n")
    atributo = input("Ingresa la nueva característica de la película: ").lower().strip()
    valor_atributo=input("ingresa el valor de la nueva caracteristica: ").upper().strip()
    #pelicula.update({atributo:valor_atributo})
    pelicula[atributo]=valor_atributo
    print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")


def modificarcaracteristicas2():
    print("\n\t ::modificar las caracteristicas de la peliculas ::\n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"\t{(i)} : {pelicula[i]}")
            resp=input("desea modificar esta carACTERISTICA de: {i}? (si/no)").lower().strip()
            if resp=="si":
                pelicula[i]=input(f"\n\t ingrese el nuevo valor de la caracteristica {i}").upper().strip()
                print("\n\t ::: La operacion se realizo con exito :::")
    else:
        print("\n\t .::No hay peliculas en el sistema::.")  

def borrarCaracteristicaPeliculas():
    borrarpantalla()
    print("\n\t.:: Borrar Característica de Películas ::.\n")
    resp=input("¿deseas quitar o borrar caracteristicas de las peliculas del sistema? (si/no)")
    if resp=="si":
        if len(pelicula) > 0:
            for valor in pelicula:
                print(f"\t{valor}: {pelicula[valor]}")
            carac = input("\nIngresa el nombre de la característica que deseas borrar: ").lower().strip()

            if carac in pelicula:
                del pelicula[carac]
                print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
            else:
                print("\n\t\t::: La característica no existe :::")
        else:
            print("\t..:: No hay películas en el sistema ::..")

'''
def modificarcaracteristicas():
    borrarpantalla()
    print("\n\t ::modificar las caracteristicas de la peliculas ::\n")
    caracterristica_cambiar=input("ingresa la caracteristica de la pelicula a buscar: ").lower().strip()


    if caracterristica_cambiar in pelicula:
        nuevo_valor=input("Ingresa el nuevo valor: ").lower().strip()
        pelicula[caracterristica_cambiar]=nuevo_valor
        print(f"el atributo dentro de la caracteristica que busco: {caracterristica_cambiar} se cambio por: {nuevo_valor}")

    else:
        print("\n\t .::No hay ninguna caracteristica con este nombre::.")  
'''


















'''
def agregarpeliculas():
    borrarpantalla()
    print("\n\t\t ..::agregar peliculas::.  ")
    peliculas.append(input("ingresa el nombre : ").upper().strip())
    print("\n\t .::LA OPERACION SE REALIZO CON EXITO::.")

def consultarpelicula():
    borrarpantalla()
    print("\n\t\t ..::consultar o mostrar todas las  peliculas::.  ")

    if len(peliculas) > 0:
        for i in range(len(peliculas)):
            print(f"\t{i+1} : {peliculas[i]}")

def vaciarpeliculas():
    borrarpantalla()
    print("\n\\t limpira o borrar todas las peliculas")
    resp=input("deseas vorrar todas la peliculas (si\no)").lower()
    if resp == "si":
        peliculas.clear()
        print("\n\t ::: LA OPERACION SE REALIZO CON EXITO")

def buscarpeliculas():
    borrarpantalla()
    print("\n\t\t .::buscar una pelicula::. \n")
    peliculas_buscar=input("ingresa el nombre de la pelicula a buscar: ").upper().strip()
    encontro=0

    for i in range(0, len(peliculas)):
        if peliculas_buscar==peliculas[i]:
            print(f"la pelicula {peliculas[i]} si la tenemos esta en el casillero: {i+1}")
            encontro+=1

    if encontro == 0: 
        print("\n\t .::No hay ninguna pelicula con este nombre::.")
    else:
        print(f"\n\t Tenemos {encontro} película(s) con ese título.")


def modificarpeliculas():
    borrarpantalla()
    print("\n\t\t .::modificar una pelicula::. \n")
    peliculas_buscar=input("ingresa el nombre de la pelicula a buscar: ").upper().strip()
    if peliculas_buscar not in peliculas:
        print("\n\t .::No hay ninguna pelicula con este nombre::.")

    else:  
        encontro=0
        for i in range(0, len(peliculas)):
            if peliculas_buscar==peliculas[i]:
                resp=input("deseas modificar la pelicula? (si/no)").lower().strip()
                if resp=="si":
                    nuevo_nombre = input("\n\t Introduce el nuevo nombre de la película: ").upper().strip()
                    peliculas[i] = nuevo_nombre
                    print(f"\n\t la pelicula ahora se llama: {peliculas[i]} y la tenemos en el casillero: {1+i}")
                encontro+= 1
        print(f"\n\t se actualizaron  {encontro} peliculas con este titulo")

def eliminarpeliculas():
    borrarpantalla()
    print("\n\t\t .::Eliminar una pelicula::. \n")
    peliculas_buscar=input("ingresa el nombre de la pelicula a buscar: ").upper().strip()
    encontro=0

    if not(peliculas_buscar in peliculas):
        print("\n\t\t No se encuentra la pelicula")
    
    else:
        resp="si"
        while peliculas_buscar in peliculas and resp=="si":
            resp=input("desea quitar o borrar la pelicula del sistema (si/no)?").lower()
            if resp=="si":
                posicion=peliculas.index(peliculas_buscar)
                print(f"\n la pelicula que se borro fue: {peliculas_buscar} y estabaen la casila {posicion+1}")
                peliculas.remove(peliculas_buscar)
                encontro+=1
                print("\n\t\t .::la operacion se realizo con exito::.")
        print(f"se borro {encontro} pelicula(s) con este titulo")

'''