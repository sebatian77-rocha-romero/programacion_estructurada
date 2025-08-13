import getpass
from datetime import datetime
from Autos import autos
from usuario import usuario
from ventas import ventas
from Clientes import clientes
import funciones 
from ConexionBD import *

def main():
    while True:
        funciones.borrar_pantalla()
        print("\n\t🚗 Agencia de Autos - Sistema de Gestión")
        print("\t1. Registro de Usuario")
        print("\t2. Iniciar Sesión")
        print("\t3. Salir")
        opcion = input("\n\tSeleccione una opción: ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("\n👋 Hasta pronto.")
            break
        else:
            print("\n⚠️ Opción inválida.")
            funciones.esperar_tecla()

def registrar_usuario():
    funciones.borrar_pantalla()
    print("\n\t📝 Registro de Usuario y Empleado")

    username = input("Nombre de usuario: ").strip()
    email = input("Correo electrónico: ").strip().lower()
    password = getpass.getpass("Contraseña: ").strip()

    funciones.borrar_pantalla()
    print("\n\t📋 Datos del Empleado")

    nombre = input("Nombre(s): ").strip()
    apellido = input("Apellido(s): ").strip()
    puesto = input("Cargo o puesto: ").strip()
    telefono = input("Teléfono: ").strip()
    salario = input("Salario: ").strip()
    fecha_contratacion = input("Fecha de contratación (AAAA-MM-DD): ").strip()

    registrado = usuario.registrar_usuario_y_empleado(
        username, email, password,
        nombre, apellido, puesto, telefono, salario, fecha_contratacion
    )

    if registrado:
        print("\n✅ Usuario y empleado registrados correctamente.")
    else:
        print("\n❌ No se pudo registrar.")
    funciones.esperar_tecla()

def iniciar_sesion():
    funciones.borrar_pantalla()
    print("\n\t🔐 Iniciar Sesión")
    email = input("Correo electrónico: ").strip().lower()
    password = getpass.getpass("Contraseña: ").strip()
    sesion = usuario.iniciar_sesion(email, password)
    if sesion:
        print(f"\n✅ Bienvenido, {sesion[1]} ({sesion[3]})")
        funciones.esperar_tecla()
        menu_principal(sesion)
    else:
        print("\n❌ Usuario o contraseña incorrectos o cuenta inactiva.")
        funciones.esperar_tecla()

def menu_principal(usuario_actual):
    while True:
        funciones.borrar_pantalla()
        print(f"\n\t📂 Menú Principal - Usuario: {usuario_actual[1]}")
        print("\t1. Gestión de Autos")
        print("\t2. Gestión de Clientes")
        print("\t3. Vender Auto")
        print("\t4. Gestión de Ventas")
        print("\t5. Cerrar Sesión")
        opcion = input("\n\tSeleccione una opción: ").strip()

        if opcion == "1":
            menu_autos()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            vender_auto()
        elif opcion == "4":
            menu_ventas()
        elif opcion == "5":
            break
        else:
            print("\n⚠️ Opción inválida.")
            funciones.esperar_tecla()

def menu_autos():
    while True:
        funciones.borrar_pantalla()
        print("\n\t🚗 Gestión de Autos")
        print("\t1. Agregar Auto")
        print("\t2. Mostrar Autos")
        print("\t3. Actualizar Auto")
        print("\t4. Eliminar Auto")
        print("\t5. Volver")
        opcion = input("\n\tSeleccione una opción: ").strip()

        if opcion == "1":
            agregar_auto()
        elif opcion == "2":
            mostrar_autos()
        elif opcion == "3":
            actualizar_auto()
        elif opcion == "4":
            eliminar_auto()
        elif opcion == "5":
            break
        else:
            print("\n⚠️ Opción no válida.")
            funciones.esperar_tecla()

def agregar_auto():
    funciones.borrar_pantalla()
    print("\n\t➕ Agregar Auto")

    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()
    año = input("Año: ").strip()
    potencia = input("Potencia: ").strip()
    transmision = input("Transmisión: ").strip()
    motor = input("Motor: ").strip()
    neumaticos = input("Neumáticos: ").strip()
    rines = input("Rines: ").strip()
    combustible = input("Tipo de combustible: ").strip()
    precio = input("Precio: ").strip()

    if autos.agregar_auto(marca, modelo, año, potencia, transmision, motor, neumaticos, rines, combustible, precio):
        print("\n✅ Auto agregado exitosamente.")
    else:
        print("\n❌ Error al agregar auto.")
    funciones.esperar_tecla()

def mostrar_autos():
    funciones.borrar_pantalla()
    print("\n\t📋 Lista de Autos")
    lista = autos.mostrar_autos()
    if lista:
        print("\n{:<3} | {:<15} | {:<15} | {:<6} | {:>12} | {:<12}".format("ID", "Marca", "Modelo", "Año", "Precio", "Estado"))
        print("-" * 70)
        for a in lista:
            estado = a[11] if len(a) > 11 else 'N/A'
            print("{:<3} | {:<15} | {:<15} | {:<6} | ${:>11} | {:<12}".format(
                a[0], a[1], a[2], a[3], a[10], estado))
    else:
        print("❌ No hay autos registrados.")
    funciones.esperar_tecla()

def actualizar_auto():
    funciones.borrar_pantalla()
    print("\n\t✏️ Actualizar Auto")
    id = input("ID del auto a actualizar: ").strip()
    
    autos_existentes = autos.mostrar_autos()
    if not any(str(a[0]) == id for a in autos_existentes):
        print("\n❌ No existe un auto con ese ID.")
        funciones.esperar_tecla()
        return
    
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()
    año = input("Año: ").strip()
    potencia = input("Potencia: ").strip()
    transmision = input("Transmisión: ").strip()
    motor = input("Motor: ").strip()
    neumaticos = input("Neumáticos: ").strip()
    rines = input("Rines: ").strip()
    combustible = input("Tipo de combustible: ").strip()
    precio = input("Precio: ").strip()

    if autos.actualizar_auto(id, marca, modelo, año, potencia, transmision, motor, neumaticos, rines, combustible, precio):
        print("\n✅ Auto actualizado.")
    else:
        print("\n❌ Error al actualizar auto.")
    funciones.esperar_tecla()

def eliminar_auto():
    funciones.borrar_pantalla()
    print("\n\t🗑 Eliminar Auto")
    id = input("ID del auto a eliminar: ").strip()
    
    autos_existentes = autos.mostrar_autos()
    if not any(str(a[0]) == id for a in autos_existentes):
        print("\n❌ No existe un auto con ese ID.")
        funciones.esperar_tecla()
        return
        
    if autos.eliminar_auto(id):
        print("\n✅ Auto eliminado.")
    else:
        print("\n❌ Error al eliminar.")
    funciones.esperar_tecla()

def menu_clientes():
    while True:
        funciones.borrar_pantalla()
        print("\n\t👥 Gestión de Clientes")
        print("\t1. Agregar Cliente")
        print("\t2. Mostrar Clientes")
        print("\t3. Actualizar Cliente")
        print("\t4. Eliminar Cliente")
        print("\t5. Volver")
        opcion = input("\n\tSeleccione una opción: ").strip()

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            actualizar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            break
        else:
            print("\n⚠️ Opción no válida.")
            funciones.esperar_tecla()

def agregar_cliente():
    funciones.borrar_pantalla()
    print("\n\t➕ Agregar Cliente")
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    telefono = input("Teléfono: ").strip()
    direccion = input("Dirección: ").strip()
    correo = input("Correo: ").strip()

    if clientes.agregar_cliente(nombre, apellido, telefono, direccion, correo):
        print("\n✅ Cliente agregado exitosamente.")
    else:
        print("\n❌ Error al agregar cliente.")
    funciones.esperar_tecla()

def mostrar_clientes():
    funciones.borrar_pantalla()
    print("\n\t📋 Lista de Clientes")
    lista = clientes.mostrar_clientes()
    if lista:
        print("\n{:<3} | {:<25} | {:<15} | {:<25}".format("ID", "Nombre Completo", "Teléfono", "Correo"))
        print("-" * 80)
        for c in lista:
            nombre_completo = f"{c[1] or 'Sin nombre'} {c[2] or ''}".strip()
            telefono = c[3] or "Sin teléfono"
            correo = c[5] or "Sin correo"
            print("{:<3} | {:<25} | {:<15} | {:<25}".format(
                c[0], nombre_completo, telefono, correo))
    else:
        print("❌ No hay clientes registrados.")
    funciones.esperar_tecla()

def actualizar_cliente():
    funciones.borrar_pantalla()
    print("\n\t✏️ Actualizar Cliente")
    id = input("ID del cliente a actualizar: ").strip()
    
    clientes_existentes = clientes.mostrar_clientes()
    if not any(str(c[0]) == id for c in clientes_existentes):
        print("\n❌ No existe un cliente con ese ID.")
        funciones.esperar_tecla()
        return
        
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    telefono = input("Teléfono: ").strip()
    direccion = input("Dirección: ").strip()
    correo = input("Correo: ").strip()

    if clientes.actualizar_cliente(id, nombre, apellido, telefono, direccion, correo):
        print("\n✅ Cliente actualizado.")
    else:
        print("\n❌ Error al actualizar cliente.")
    funciones.esperar_tecla()

def eliminar_cliente():
    funciones.borrar_pantalla()
    print("\n\t🗑 Eliminar Cliente")
    id = input("ID del cliente a eliminar: ").strip()
    
    clientes_existentes = clientes.mostrar_clientes()
    if not any(str(c[0]) == id for c in clientes_existentes):
        print("\n❌ No existe un cliente con ese ID.")
        funciones.esperar_tecla()
        return
        
    if clientes.eliminar_cliente(id):
        print("\n✅ Cliente eliminado.")
    else:
        print("\n❌ Error al eliminar.")
    funciones.esperar_tecla()

def menu_ventas():
    while True:
        funciones.borrar_pantalla()
        print("\n\t💰 Gestión de Ventas")
        print("\t1. Mostrar Todas las Ventas")
        print("\t2. Buscar Venta por ID")
        print("\t3. Buscar Ventas por Cliente")
        print("\t4. Buscar Ventas por Fecha")
        print("\t5. Eliminar Venta")
        print("\t6. Generar reporte PDF de ventas")
        print("\t7. Volver")
        opcion = input("\n\tSeleccione una opción: ").strip()

        if opcion == "1":
            mostrar_ventas()
        elif opcion == "2":
            buscar_venta_por_id()
        elif opcion == "3":
            buscar_ventas_por_cliente()
        elif opcion == "4":
            buscar_ventas_por_fecha()
        elif opcion == "5":
            eliminar_venta()
        elif opcion == "6":
            generar_reporte_ventas()
        elif opcion == "7":
            break
        else:
            print("\n⚠️ Opción no válida.")
            funciones.esperar_tecla()

def mostrar_ventas():
    funciones.borrar_pantalla()
    print("\n\t📋 Lista de Ventas")
    lista = ventas.mostrar_ventas()
    if lista:
        print("\n{:<3} | {:>12} | {:<22} | {:<22} | {:>10} | {:<15}".format(
            "ID", "Fecha Venta", "Cliente", "Auto", "Precio", "Método Pago"))
        print("-" * 100)
        for v in lista:
            try:
                id_venta = v[0] or "N/A"
                fecha_venta = v[3] or "Sin fecha"
                cliente = (v[1] or "Cliente desconocido")[:22]
                auto = (v[2] or "Auto desconocido")[:22]
                precio = f"${v[4]}" if v[4] is not None else "$0"
                metodo_pago = v[5] or "No especificado"
                print("{:<3} | {:>12} | {:<22} | {:<22} | {:>10} | {:<15}".format(
                    str(id_venta), fecha_venta, cliente, auto, precio, metodo_pago))
            except Exception as e:
                print(f"❌ Error mostrando venta ID {v[0]}: {str(e)}")
                continue
    else:
        print("❌ No hay ventas registradas.")
    funciones.esperar_tecla()

def generar_reporte_ventas():
    funciones.borrar_pantalla()
    print("\n\t📄 Generar reporte PDF de ventas")
    ventas_lista = ventas.mostrar_ventas()
    if not ventas_lista:
        print("❌ No hay ventas registradas.")
        funciones.esperar_tecla()
        return

    contenido = []
    contenido.append("{:<3} | {:>12} | {:<22} | {:<22} | {:>10} | {:<15}".format(
        "ID", "Fecha Venta", "Cliente", "Auto", "Precio", "Método Pago"))
    contenido.append("-" * 100)
    for v in ventas_lista:
        id_venta = v[0] or "N/A"
        fecha_venta = v[3] or "Sin fecha"
        cliente = (v[1] or "Cliente desconocido")[:22]
        auto = (v[2] or "Auto desconocido")[:22]
        precio = f"${v[4]}" if v[4] is not None else "$0"
        metodo_pago = v[5] or "No especificado"
        contenido.append("{:<3} | {:>12} | {:<22} | {:<22} | {:>10} | {:<15}".format(
            str(id_venta), fecha_venta, cliente, auto, precio, metodo_pago))

    nombre_archivo = input("\nNombre del archivo PDF (ejemplo: ventas_reporte.pdf): ").strip()
    if not nombre_archivo.endswith(".pdf"):
        nombre_archivo += ".pdf"

    exito = funciones.generar_reporte_pdf("Reporte de Ventas", contenido, nombre_archivo)
    if exito:
        print(f"\n✅ Reporte generado: {nombre_archivo}")
    funciones.esperar_tecla()

def buscar_venta_por_id():
    funciones.borrar_pantalla()
    print("\n\t🔍 Buscar Venta por ID")
    id_venta = input("ID de la venta: ").strip()
    venta = ventas.obtener_venta_por_id(id_venta)
    if venta:
        print("\n📋 Detalles completos de la venta:")
        print(f"ID Venta: {venta.get('id', 'N/A')}")
        print(f"\n👤 Cliente:")
        print(f"  Nombre: {venta.get('cliente', {}).get('nombre', 'Desconocido')}")
        print(f"  Teléfono: {venta.get('cliente', {}).get('telefono', 'No disponible')}")
        print(f"\n🚗 Auto:")
        print(f"  Modelo: {venta.get('auto', {}).get('nombre', 'Desconocido')}")
        print(f"  Precio original: ${venta.get('auto', {}).get('precio_original', 0)}")
        print(f"\n💰 Transacción:")
        print(f"  Fecha: {venta.get('fecha', 'No registrada')}")
        print(f"  Precio venta: ${venta.get('precio_venta', 0)}")
        print(f"  Método pago: {venta.get('metodo_pago', 'No especificado')}")
        print(f"  Notas: {venta.get('notas', 'Ninguna')}")
    else:
        print("\n❌ Venta no encontrada.")
    funciones.esperar_tecla()

def buscar_ventas_por_cliente():
    funciones.borrar_pantalla()
    print("\n\t👥 Ventas por Cliente")
    id_cliente = input("ID del cliente: ").strip()
    
    clientes_existentes = clientes.mostrar_clientes()
    cliente = next((c for c in clientes_existentes if str(c[0]) == id_cliente), None)
    
    if not cliente:
        print("\n❌ No existe un cliente con ese ID.")
        funciones.esperar_tecla()
        return
        
    ventas_cliente = ventas.obtener_ventas_por_cliente(id_cliente)
    if ventas_cliente:
        print(f"\n📋 Ventas del cliente: {cliente[1] or ''} {cliente[2] or ''}".strip())
        print("\nID | Auto                  | Fecha       | Precio    | Método Pago")
        print("-" * 80)
        for v in ventas_cliente:
            try:
                id_venta = v[0] or "N/A"
                auto = (v[1] or "Auto desconocido")[:20]
                fecha = v[2] or "Sin fecha"
                precio = f"${v[3]}" if v[3] is not None else "$0"
                metodo_pago = v[4] or "No especificado"
                
                print(f"{str(id_venta):<3} | {auto:<22} | {fecha} | {precio:<9} | {metodo_pago}")
            except Exception as e:
                print(f"❌ Error mostrando venta ID {v[0]}: {str(e)}")
                continue
    else:
        print("\n❌ No se encontraron ventas para este cliente.")
    funciones.esperar_tecla()

def buscar_ventas_por_fecha():
    funciones.borrar_pantalla()
    print("\n\t📅 Ventas por Fecha")
    fecha_inicio = input("Fecha inicio (AAAA-MM-DD): ").strip()
    fecha_fin = input("Fecha fin (AAAA-MM-DD): ").strip()
    ventas_fecha = ventas.obtener_ventas_por_fecha(fecha_inicio, fecha_fin)
    if ventas_fecha:
        print(f"\n📋 Ventas entre {fecha_inicio} y {fecha_fin}")
        print("\nID | Cliente                | Auto                  | Fecha       | Precio")
        print("-" * 90)
        for v in ventas_fecha:
            try:
                id_venta = v[0] or "N/A"
                cliente = (v[1] or "Cliente desconocido")[:20]
                auto = (v[2] or "Auto desconocido")[:20]
                fecha = v[3] or "Sin fecha"
                precio = f"${v[4]}" if v[4] is not None else "$0"
                
                print(f"{str(id_venta):<3} | {cliente:<22} | {auto:<22} | {fecha} | {precio}")
            except Exception as e:
                print(f"❌ Error mostrando venta ID {v[0]}: {str(e)}")
                continue
    else:
        print("\n❌ No se encontraron ventas en este rango de fechas.")
    funciones.esperar_tecla()

def eliminar_venta():
    funciones.borrar_pantalla()
    print("\n\t🗑 Eliminar Venta")
    id_venta = input("ID de la venta a eliminar: ").strip()
    
    ventas_existentes = ventas.mostrar_ventas()
    if not any(str(v[0]) == id_venta for v in ventas_existentes if v[0] is not None):
        print("\n❌ No existe una venta con ese ID.")
        funciones.esperar_tecla()
        return
        
    if ventas.eliminar_venta(id_venta):
        print("\n✅ Venta eliminada correctamente.")
    else:
        print("\n❌ Error al eliminar la venta.")
    funciones.esperar_tecla()

def vender_auto():
    funciones.borrar_pantalla()
    print("\n\t💰 Venta de Auto")
    
    try:
        if not conexion or not conexion.is_connected():
            print("❌ No hay conexión a la base de datos")
            funciones.esperar_tecla()
            return

        autos_disponibles = [a for a in autos.mostrar_autos() if len(a) > 11 and a[11] == 'Disponible']

        if not autos_disponibles:
            print("\n⚠️ No hay autos disponibles para vender.")
            funciones.esperar_tecla()
            return

        print("\nAutos disponibles:")
        print("ID | Marca      | Modelo     | Año  | Precio    | Estado")
        print("-" * 60)
        for a in autos_disponibles:
            estado = a[11] if len(a) > 11 else 'N/A'
            print(f"{a[0]:<3} | {a[1]:<10} | {a[2]:<10} | {a[3]:<4} | ${a[10]:<8} | {estado}")

        id_auto = input("\nIngrese el ID del auto que desea vender: ").strip()
        seleccionado = [a for a in autos_disponibles if str(a[0]) == id_auto]

        if not seleccionado:
            print("❌ ID inválido o auto no disponible.")
            funciones.esperar_tecla()
            return

        cursor.execute("SELECT estado FROM autos WHERE id = %s", (id_auto,))
        estado_auto = cursor.fetchone()
        
        if not estado_auto:
            print("❌ El auto no existe en la base de datos.")
            funciones.esperar_tecla()
            return
            
        if estado_auto[0] != 'Disponible':
            print(f"❌ El auto seleccionado está en estado '{estado_auto[0]}'. No se puede vender.")
            funciones.esperar_tecla()
            return

        print("\n¿El cliente es existente o nuevo?")
        print("1. Cliente existente")
        print("2. Cliente nuevo")
        opcion_cliente = input("Seleccione una opción: ").strip()

        cliente_id = None
        if opcion_cliente == "1":
            lista_clientes = clientes.mostrar_clientes()
            if lista_clientes:
                print("\nClientes existentes:")
                print("ID | Nombre Completo | Teléfono")
                print("-" * 40)
                for c in lista_clientes:
                    nombre = c[1] if c[1] is not None else "Sin nombre"
                    apellido = c[2] if c[2] is not None else ""
                    telefono = c[3] if c[3] is not None else "Sin teléfono"
                    print(f"{c[0]:<3} | {nombre} {apellido:<12} | {telefono}")
                
                cliente_id = input("\nIngrese el ID del cliente: ").strip()
                if not any(str(c[0]) == cliente_id for c in lista_clientes):
                    print("❌ ID de cliente no válido.")
                    funciones.esperar_tecla()
                    return
            else:
                print("No hay clientes registrados. Se creará uno nuevo.")
                opcion_cliente = "2"

        if opcion_cliente == "2" or not cliente_id:
            print("\n🧾 Datos del Nuevo Cliente:")
            nombre = input("Nombre: ").strip()
            while not nombre:
                print("❌ El nombre es obligatorio.")
                nombre = input("Nombre: ").strip()
                
            apellido = input("Apellido: ").strip()
            while not apellido:
                print("❌ El apellido es obligatorio.")
                apellido = input("Apellido: ").strip()
                
            telefono = input("Teléfono: ").strip()
            while not telefono:
                print("❌ El teléfono es obligatorio.")
                telefono = input("Teléfono: ").strip()
                
            direccion = input("Dirección (opcional): ").strip()
            correo = input("Correo (opcional): ").strip()

            if clientes.agregar_cliente(nombre, apellido, telefono, direccion, correo):
                cliente_id = clientes.obtener_id_cliente_por_correo(correo) if correo else None
                if not cliente_id:
                    cursor.execute("SELECT LAST_INSERT_ID()")
                    cliente_id = cursor.fetchone()[0]
                print(f"\n✅ Cliente registrado con ID: {cliente_id}")
            else:
                print("❌ Error al registrar cliente.")
                funciones.esperar_tecla()
                return

        if not cliente_id:
            print("❌ No se pudo obtener el ID del cliente.")
            funciones.esperar_tecla()
            return

        # Validacion de metodo de pago para minusculas y mayusculas
        opciones_pago = {
            "efectivo": "Efectivo",
            "tarjeta": "Tarjeta",
            "transferencia": "Transferencia",
            "financiado": "Financiado"
        }

        metodo_pago = input("Método de pago (efectivo, tarjeta, transferencia, financiado): ").strip().lower()
        while metodo_pago not in opciones_pago:
            print("❌ Método de pago inválido.")
            metodo_pago = input("Método de pago (efectivo, tarjeta, transferencia, financiado): ").strip().lower()
        
        metodo_pago = opciones_pago[metodo_pago]  
        notas = input("Notas adicionales (opcional): ").strip()

        # Depurar
        print("DEBUG valor en índice 10:", seleccionado[0][10])

        # limpiar el precio de comas
        try:
            precio_str = seleccionado[0][10].replace(',', '')  # Quitar comas de miles
            precio_venta = float(precio_str)
        except (ValueError, TypeError) as e:
            print(f"❌ El precio no es numérico: {seleccionado[0][10]}")
            funciones.esperar_tecla()
            return

        auto_id = seleccionado[0][0]

        #registrar venta
        if ventas.agregar_venta(cliente_id, auto_id, metodo_pago, precio_venta, notas):
            print("\n✅ Venta registrada correctamente.")
        else:
            print("\n❌ No se pudo registrar la venta.")
        funciones.esperar_tecla()
        return

    except mysql.connector.Error as err:
        print(f"❌ Error de base de datos: {err}")
        funciones.esperar_tecla()
        return
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        funciones.esperar_tecla()
        return



if __name__ == "__main__":
    main()