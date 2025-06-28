'''
proyecto 1: crear un proyecto que permita gestionar y administraer peliculas, colocar un menu de opciones para agregar
eliminar, modificar, consultar, buscar y colsultar peliculas

notas: 1.-utilizar funciones y mandar a llamar de otro archivo
2.- utilizar listas para almacenar los nombres de las peliculas

'''
import peliculas

opcion=True
while opcion:
    print("\t\ .::bienvenido a peliculas totalmente legales::.")

    print("eliga una opcion porfavor")
    print("1.- agregar" \
    "\n 2.- elimnar" \
    "\n 3.- actualizar" \
    "\n 4.- consultar" \
    "\n 5.- buscar" \
    "\n 6.- vaciar" \
    "\n 7.- salir")
    eleccion  = input("Ingrese una opción: ")

    match eleccion:
        case"1":
            peliculas.agregarpeliculas()
            peliculas.esperartecla()

        case"2":
            peliculas.eliminarpeliculas()
            peliculas.esperartecla
        case"3":
            peliculas.modificarpeliculas()
            peliculas.esperartecla()
        case"4":
            peliculas.consultarpelicula() 
            peliculas.esperartecla()

        case"5":
            peliculas.buscarpeliculas()
            peliculas.esperartecla()
        
        case"6":
            peliculas.vaciarpeliculas()
            peliculas.esperartecla()
        case"7":
            opcion=False    
            print("Terminaste la ejecucion del SW")
        case _:
            input("Opción invalida vuelva a intentarlo ... por favor")