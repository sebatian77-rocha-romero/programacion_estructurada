import agenda



def main():
    agenda_contactos={}
    iniciar=True

    while iniciar:
        agenda.borrarpantalla()
        opcion = agenda.mostrar_menu()

        if opcion =="1":
            agenda.agregar_contacto(agenda_contactos)
            agenda.esperartecla()
        
        if opcion =="2":
            agenda.mostrar_contactos(agenda_contactos)
            agenda.esperartecla()
        
        if opcion =="3":
            agenda.buscar_contacto(agenda_contactos)
            agenda.esperartecla()
        
        if opcion =="4":
            agenda.modificar_contacto(agenda_contactos)
            agenda.esperartecla()

        if opcion =="5":
            agenda.eliminar_contacto(agenda_contactos)
            agenda.esperartecla()

        if opcion =="6":
            agenda.borrarpantalla()
            print("programa finalizado")
            iniciar=False

if __name__ == "__main__":
    main()


