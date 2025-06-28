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
print("\t\ .::bienvenido a peliculas totalmente legales::.")

while opcion:
    print("eliga una opcion porfavor")
    print("1.- crear" \
    "\n 2.- borrar" \
    "\n 3.- mostrar" \
    "\n 4.- agregar caracteristica" \
    "\n 5.- modificar caracteristica" \
    "\n 6.- borrar caracteristicas" \
    "\n 7.- salir")
    eleccion  = input("Ingrese una opción: ")

    match eleccion:
        case"1":
            peliculass.crearpelicula()
            peliculass.esperartecla()

        case"2":
            peliculass.borrarpelicula()
            peliculass.esperartecla
        case"3":
            peliculass.mostrarpelicula()
            peliculass.esperartecla()
        case"4":
            peliculass.agregarcaracteristicaspeliculas() 
            peliculass.esperartecla()

        case"5":
            peliculass.modificarcaracteristicas2()
            peliculass.esperartecla()
        
        case"6":
            peliculass.borrarCaracteristicaPeliculas()
            peliculass.esperartecla()
        case"7":
            opcion=False    
            print("Terminaste la ejecucion del SW")
        case _:
            input("Opción invalida vuelva a intentarlo ... por favor")