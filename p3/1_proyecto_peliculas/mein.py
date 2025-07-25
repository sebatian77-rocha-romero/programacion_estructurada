'''
proyecto 1: crear un proyecto que permita gestionar y administraer peliculas, colocar un menu de opciones para 
agregar eliminar, modificar, consultar, buscar y colsultar peliculas

notas: 1.-utilizar funciones y mandar a llamar de otro archivo
2.- utilizar una dict para almacenar los atributos o caracteristicas (nombre, categoria, clasificacion, genero
y idioma) de la pelicula
)

'''
import peliculass

opcion=True

while opcion:
    peliculass.borrarpantalla()
    print("\t\ .::bienvenido a peliculas totalmente legales::.")
    print("eliga una opcion porfavor")
    print("1.- crear" \
    "\n 2.- borrar" \
    "\n 3.- mostrar" \
    "\n 4.- buscar" \
    "\n 5.- modificar" \
    "\n 6.- salir")
    eleccion  = input("Ingrese una opción: ")

    match eleccion:
        case"1":
            peliculass.crearPeliculas()
            peliculass.esperartecla()

        case"2":
            peliculass.borrarPeliculas()
            peliculass.esperartecla
        case"3":
            peliculass.mostrarPeliculas()
            peliculass.esperartecla()
        case"4":
            peliculass.buscarPeliculas() 
            peliculass.esperartecla()
        case"5":
            peliculass.modificarPeliculas()
            peliculass.esperartecla()
        
        case"6":
            opcion=False    
            print("Terminaste la ejecucion del SW")
        case _:
            input("Opción invalida vuelva a intentarlo ... por favor")