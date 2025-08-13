from ConexionBD import *
import hashlib
import datetime

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar_usuario_y_empleado(username, email, contrasena,
                                  nombre, apellido, puesto, telefono, salario, fecha_contratacion):
    try:
        contrasena = hash_password(contrasena)
        estado = "activo"
        rol = "empleado"
        fecha_creacion = datetime.datetime.now()

        sql_usuario = """
            INSERT INTO usuario (username, email, password, fecha_creacion, estado, rol)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        val_usuario = (username, email, contrasena, fecha_creacion, estado, rol)
        cursor.execute(sql_usuario, val_usuario)

        sql_empleado = """
            INSERT INTO empleados 
            (`Nombre`, `Apellido`, `Cargo o puesto`, `Telefono`, `Correo`, `Fecha de contratacion`, `Estado del empleado`, `salario`)
            VALUES (%s, %s, %s, %s, %s, %s, 'Activo', %s)
        """
        val_empleado = (nombre, apellido, puesto, telefono, email, fecha_contratacion, salario)
        cursor.execute(sql_empleado, val_empleado)

        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al registrar usuario/empleado: {e}")
        return False

def iniciar_sesion(email, contrasena):
    try:
        contrasena = hash_password(contrasena)
        cursor.execute("""
            SELECT id, username, email, rol, estado FROM usuario
            WHERE email=%s AND password=%s AND estado='activo'
        """, (email, contrasena))
        usuario = cursor.fetchone()

        if usuario:
            cursor.execute("UPDATE usuario SET ultimo_acceso=NOW() WHERE id=%s", (usuario[0],))
            conexion.commit()

        return usuario
    except Exception as e:
        print(f"Error al iniciar sesión: {e}")
        return None
