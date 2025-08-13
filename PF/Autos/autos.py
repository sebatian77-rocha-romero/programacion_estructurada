from ConexionBD import *

def agregar_auto(marca, modelo, año, potencia, transmision, motor, neumaticos, rines, combustible, precio):
    try:
        cursor.execute("""
            INSERT INTO autos (Marca, Modelo, Año, Potencia, Transmision, Motor, Neumaticos, Rines, `Tipo de combustible`, Precio)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (marca, modelo, año, potencia, transmision, motor, neumaticos, rines, combustible, precio))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al agregar auto: {e}")
        return False

def mostrar_autos():
    try:
        cursor.execute("SELECT * FROM autos")
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al mostrar autos: {e}")
        return []

def actualizar_auto(id, marca, modelo, año, potencia, transmision, motor, neumaticos, rines, combustible, precio):
    try:
        cursor.execute("""
            UPDATE autos 
            SET Marca=%s, Modelo=%s, Año=%s, Potencia=%s, Transmision=%s, Motor=%s, Neumaticos=%s, 
                Rines=%s, `Tipo de combustible`=%s, Precio=%s
            WHERE id=%s
        """, (marca, modelo, año, potencia, transmision, motor, neumaticos, rines, combustible, precio, id))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al actualizar auto: {e}")
        return False

def eliminar_auto(id):
    try:
        cursor.execute("DELETE FROM autos WHERE id=%s", (id,))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar auto: {e}")
        return False
