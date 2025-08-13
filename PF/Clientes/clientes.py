from ConexionBD import *

def validar_datos_cliente(nombre, apellido, telefono, direccion=None, correo=None):
    """Valida los datos básicos de un cliente"""
    if not nombre or not isinstance(nombre, str) or len(nombre.strip()) < 2:
        print("❌ El nombre debe tener al menos 2 caracteres")
        return False
    
    if not apellido or not isinstance(apellido, str) or len(apellido.strip()) < 2:
        print("❌ El apellido debe tener al menos 2 caracteres")
        return False
    
    if not telefono or not isinstance(telefono, str) or len(telefono.strip()) < 8:
        print("❌ El teléfono debe tener al menos 8 dígitos")
        return False
    
    return True

def agregar_cliente(nombre, apellido, telefono, direccion=None, correo=None):
    """
    Agrega un nuevo cliente a la base de datos con validaciones
    Devuelve: True si se agregó correctamente, False si hubo error
    """
    try:
        # Validar datos antes de insertar
        if not validar_datos_cliente(nombre, apellido, telefono, direccion, correo):
            return False

        # Verificar si el correo ya existe (si se proporcionó)
        if correo:
            cursor.execute("SELECT id FROM clientes WHERE correo = %s", (correo,))
            if cursor.fetchone():
                print("❌ Ya existe un cliente con este correo electrónico")
                return False

        cursor.execute("""
            INSERT INTO clientes (nombre, apellido, telefono, direccion, correo)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre.strip(), apellido.strip(), telefono.strip(), 
              direccion.strip() if direccion else None, 
              correo.strip().lower() if correo else None))
        
        conexion.commit()
        print("✅ Cliente agregado exitosamente")
        return True
        
    except mysql.connector.Error as err:
        print(f"❌ Error de MySQL al agregar cliente: {err}")
        conexion.rollback()
        return False
    except Exception as e:
        print(f"❌ Error inesperado al agregar cliente: {e}")
        conexion.rollback()
        return False
    
def obtener_id_cliente_por_correo(correo):
    """
    Obtiene el ID de un cliente por su correo electrónico
    Devuelve: ID del cliente o None si no existe o hay error
    """
    try:
        if not correo or not isinstance(correo, str):
            print("❌ Correo electrónico inválido")
            return None

        cursor.execute("SELECT id FROM clientes WHERE correo = %s", (correo.strip().lower(),))
        resultado = cursor.fetchone()
        return resultado[0] if resultado else None
        
    except mysql.connector.Error as err:
        print(f"❌ Error de MySQL al buscar cliente: {err}")
        return None
    except Exception as e:
        print(f"❌ Error inesperado al buscar cliente: {e}")
        return None

def mostrar_clientes():
    """
    Obtiene todos los clientes de la base de datos
    Devuelve: Lista de clientes o lista vacía si hay error
    """
    try:
        cursor.execute("""
            SELECT id, nombre, apellido, telefono, direccion, correo 
            FROM clientes 
            ORDER BY apellido, nombre
        """)
        return cursor.fetchall()
        
    except mysql.connector.Error as err:
        print(f"❌ Error de MySQL al obtener clientes: {err}")
        return []
    except Exception as e:
        print(f"❌ Error inesperado al obtener clientes: {e}")
        return []

def eliminar_cliente(id):
    """
    Elimina un cliente por su ID
    Devuelve: True si se eliminó correctamente, False si hubo error
    """
    try:
        # Verificar si el cliente existe
        cursor.execute("SELECT id FROM clientes WHERE id = %s", (id,))
        if not cursor.fetchone():
            print("❌ No existe un cliente con ese ID")
            return False

        # Verificar si el cliente tiene ventas asociadas
        cursor.execute("SELECT id FROM ventas WHERE id_cliente = %s LIMIT 1", (id,))
        if cursor.fetchone():
            print("❌ No se puede eliminar - El cliente tiene ventas registradas")
            return False

        cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
        conexion.commit()
        print("✅ Cliente eliminado correctamente")
        return True
        
    except mysql.connector.Error as err:
        print(f"❌ Error de MySQL al eliminar cliente: {err}")
        conexion.rollback()
        return False
    except Exception as e:
        print(f"❌ Error inesperado al eliminar cliente: {e}")
        conexion.rollback()
        return False

def actualizar_cliente(id, nombre, apellido, telefono, direccion=None, correo=None):
    """
    Actualiza los datos de un cliente existente
    Devuelve: True si se actualizó correctamente, False si hubo error
    """
    try:
        # Validar datos antes de actualizar
        if not validar_datos_cliente(nombre, apellido, telefono, direccion, correo):
            return False

        # Verificar si el cliente existe
        cursor.execute("SELECT id FROM clientes WHERE id = %s", (id,))
        if not cursor.fetchone():
            print("❌ No existe un cliente con ese ID")
            return False

        # Verificar si el nuevo correo ya existe en otro cliente
        if correo:
            cursor.execute("""
                SELECT id FROM clientes 
                WHERE correo = %s AND id != %s
            """, (correo.strip().lower(), id))
            if cursor.fetchone():
                print("❌ Ya existe otro cliente con este correo electrónico")
                return False

        cursor.execute("""
            UPDATE clientes SET 
                nombre = %s,
                apellido = %s,
                telefono = %s,
                direccion = %s,
                correo = %s
            WHERE id = %s
        """, (nombre.strip(), apellido.strip(), telefono.strip(),
              direccion.strip() if direccion else None,
              correo.strip().lower() if correo else None,
              id))
        
        conexion.commit()
        print("✅ Cliente actualizado correctamente")
        return True
        
    except mysql.connector.Error as err:
        print(f"❌ Error de MySQL al actualizar cliente: {err}")
        conexion.rollback()
        return False
    except Exception as e:
        print(f"❌ Error inesperado al actualizar cliente: {e}")
        conexion.rollback()
        return False

def buscar_clientes_por_nombre(nombre):
    """
    Busca clientes por coincidencia en nombre o apellido
    Devuelve: Lista de clientes o lista vacía si hay error
    """
    try:
        if not nombre or not isinstance(nombre, str):
            print("❌ Nombre de búsqueda inválido")
            return []

        parametro_busqueda = f"%{nombre.strip().lower()}%"
        cursor.execute("""
            SELECT id, nombre, apellido, telefono 
            FROM clientes 
            WHERE LOWER(nombre) LIKE %s OR LOWER(apellido) LIKE %s
            ORDER BY apellido, nombre
        """, (parametro_busqueda, parametro_busqueda))
        
        return cursor.fetchall()
        
    except mysql.connector.Error as err:
        print(f"❌ Error de MySQL al buscar clientes: {err}")
        return []
    except Exception as e:
        print(f"❌ Error inesperado al buscar clientes: {e}")
        return []