from ConexionBD import *

def agregar_empleado(nombre, telefono, correo, cargo, fecha_ingreso):
    try:
        cursor.execute("""
            INSERT INTO empleados (Nombre, Telefono, Correo, Cargo, FechaIngreso)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, telefono, correo, cargo, fecha_ingreso))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al agregar empleado: {e}")
        return False

def mostrar_empleados():
    try:
        cursor.execute("SELECT * FROM empleados")
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al mostrar empleados: {e}")
        return []

def actualizar_empleado(id, nombre, telefono, correo, cargo, fecha_ingreso):
    try:
        cursor.execute("""
            UPDATE empleados 
            SET Nombre=%s, Telefono=%s, Correo=%s, Cargo=%s, FechaIngreso=%s
            WHERE id=%s
        """, (nombre, telefono, correo, cargo, fecha_ingreso, id))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al actualizar empleado: {e}")
        return False

def eliminar_empleado(id):
    try:
        cursor.execute("DELETE FROM empleados WHERE id=%s", (id,))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar empleado: {e}")
        return False
