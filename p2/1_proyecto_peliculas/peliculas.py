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

peliculas = [p.upper() for p in peliculas]


def borrarpantalla():
    import os
    os.system("cls")

def esperartecla():
    input("\n\toprima cualquier tecla para continuar... ")

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
