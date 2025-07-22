'''
proyecto 3:

notas: 1.-utilizar funciones y mandar a llamar de otro archivo
2.- utilizar listas para almacenar el nombre y 3 clasificaciones de los alumnos

'''
import calificaciones

def main():
    opcion=True
    datos=[]

    while opcion:
        calificaciones.borrarpantalla()
        opcion=calificaciones.menu_principal()

        match opcion:
            case"1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperartecla()
            case"2":
                calificaciones.mostrar_calificaciones()
                calificaciones.esperartecla()
            case"3":
                calificaciones.calcular_promedios()
                calificaciones.esperartecla()
            case"4":
                calificaciones.buscar_calificaciones(datos)
                calificaciones.esperartecla()
            case"5":
                opcion=False  
                calificaciones.borrarpantalla()  
                print("Terminaste la ejecucion del SW")
            case _:
                input("Opción invalida vuelva a intentarlo ... por favor")
                calificaciones.esperartecla()

if __name__ == "__main__":
    main()