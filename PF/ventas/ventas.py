from ConexionBD import *
from datetime import datetime
import sys

def agregar_venta(id_cliente, id_auto, metodo_pago, precio_venta, notas=None):
    """Registra una nueva venta con validaciones"""
    try:
        if not id_cliente or not id_auto or not metodo_pago or not precio_venta:
            print("❌ Todos los campos obligatorios deben estar completos")
            return False

        cursor.execute("SELECT id FROM clientes WHERE id = %s", (id_cliente,))
        if not cursor.fetchone():
            print(f"❌ No existe el cliente con ID {id_cliente}")
            return False

        cursor.execute("SELECT id, estado FROM autos WHERE id = %s", (id_auto,))
        auto = cursor.fetchone()
        if not auto:
            print(f"❌ No existe el auto con ID {id_auto}")
            return False
        if auto[1] != 'Disponible':
            print(f"❌ El auto no está disponible (estado: {auto[1]})")
            return False

        metodos_validos = ['efectivo', 'tarjeta', 'transferencia', 'financiado']
        if metodo_pago.lower() not in metodos_validos:
            print(f"❌ Método de pago inválido. Use: {', '.join(metodos_validos)}")
            return False

        try:
            precio_venta = float(precio_venta)
        except ValueError:
            print("❌ El precio debe ser un valor numérico")
            return False

        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        cursor.execute("""
            INSERT INTO ventas 
            (id_cliente, id_auto, fecha_venta, metodo_pago, precio_venta, notas)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (id_cliente, id_auto, fecha_actual, metodo_pago, precio_venta, notas))

        cursor.execute("UPDATE autos SET estado = 'Vendido' WHERE id = %s", (id_auto,))

        conexion.commit()
        print(f"✅ Venta registrada correctamente (ID Auto: {id_auto}, ID Cliente: {id_cliente})")
        return True

    except mysql.connector.Error as err:
        print(f"❌ Error de MySQL: {err}")
        conexion.rollback()
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {sys.exc_info()[0]}: {e}")
        conexion.rollback()
        return False

def mostrar_ventas():
    """Obtiene todas las ventas con información completa"""
    try:
        cursor.execute("""
            SELECT 
                v.id, 
                CONCAT(COALESCE(c.nombre, ''), ' ', COALESCE(c.apellido, '')) AS cliente,
                CONCAT(COALESCE(a.marca, ''), ' ', COALESCE(a.modelo, '')) AS auto,
                DATE_FORMAT(v.fecha_venta, '%Y-%m-%d') AS fecha_venta,
                v.precio_venta,
                v.metodo_pago,
                v.notas,
                c.id AS id_cliente,
                a.id AS id_auto
            FROM ventas v
            LEFT JOIN clientes c ON v.id_cliente = c.id
            LEFT JOIN autos a ON v.id_auto = a.id
            ORDER BY v.fecha_venta DESC
        """)
        return cursor.fetchall()
    except Exception as e:
        print(f"❌ Error al obtener ventas: {e}")
        return []

def obtener_venta_por_id(id_venta):
    """Obtiene una venta específica por su ID con formato estructurado"""
    try:
        cursor.execute("""
            SELECT 
                v.id,
                v.id_cliente,
                v.id_auto,
                DATE_FORMAT(v.fecha_venta, '%Y-%m-%d') AS fecha_venta,
                v.metodo_pago,
                v.precio_venta,
                v.notas,
                CONCAT(COALESCE(c.nombre, ''), ' ', COALESCE(c.apellido, '')) AS cliente_nombre,
                c.telefono,
                c.correo,
                CONCAT(COALESCE(a.marca, ''), ' ', COALESCE(a.modelo, '')) AS auto_nombre,
                a.precio AS precio_original,
                a.año
            FROM ventas v
            LEFT JOIN clientes c ON v.id_cliente = c.id
            LEFT JOIN autos a ON v.id_auto = a.id
            WHERE v.id = %s
        """, (id_venta,))
        
        venta = cursor.fetchone()
        
        if venta:
            return {
                'id': venta[0],
                'cliente': {
                    'id': venta[1],
                    'nombre': venta[7],
                    'telefono': venta[8],
                    'correo': venta[9]
                },
                'auto': {
                    'id': venta[2],
                    'nombre': venta[10],
                    'precio_original': venta[11],
                    'año': venta[12]
                },
                'fecha': venta[3],
                'metodo_pago': venta[4],
                'precio_venta': venta[5],
                'notas': venta[6]
            }
        return None
    except Exception as e:
        print(f"❌ Error al buscar venta: {e}")
        return None

def obtener_ventas_por_cliente(id_cliente):
    """Obtiene todas las ventas de un cliente específico"""
    try:
        cursor.execute("""
            SELECT 
                v.id, 
                CONCAT(COALESCE(a.marca, ''), ' ', COALESCE(a.modelo, '')) AS auto,
                DATE_FORMAT(v.fecha_venta, '%Y-%m-%d') AS fecha_venta,
                v.precio_venta,
                v.metodo_pago
            FROM ventas v
            LEFT JOIN autos a ON v.id_auto = a.id
            WHERE v.id_cliente = %s
            ORDER BY v.fecha_venta DESC
        """, (id_cliente,))
        return cursor.fetchall()
    except Exception as e:
        print(f"❌ Error al obtener ventas por cliente: {e}")
        return []

def obtener_ventas_por_fecha(fecha_inicio, fecha_fin):
    """Obtiene ventas en un rango de fechas con formato consistente"""
    try:
        datetime.strptime(fecha_inicio, '%Y-%m-%d')
        datetime.strptime(fecha_fin, '%Y-%m-%d')
        
        cursor.execute("""
            SELECT 
                v.id, 
                CONCAT(COALESCE(c.nombre, ''), ' ', COALESCE(c.apellido, '')) AS cliente,
                CONCAT(COALESCE(a.marca, ''), ' ', COALESCE(a.modelo, '')) AS auto,
                DATE_FORMAT(v.fecha_venta, '%Y-%m-%d') AS fecha_venta,
                v.precio_venta
            FROM ventas v
            LEFT JOIN clientes c ON v.id_cliente = c.id
            LEFT JOIN autos a ON v.id_auto = a.id
            WHERE v.fecha_venta BETWEEN %s AND %s
            ORDER BY v.fecha_venta DESC
        """, (fecha_inicio, fecha_fin))
        
        return cursor.fetchall()
    except ValueError:
        print("❌ Formato de fecha incorrecto. Use AAAA-MM-DD")
        return []
    except Exception as e:
        print(f"❌ Error al obtener ventas por fecha: {e}")
        return []

def eliminar_venta(id_venta):
    """Elimina una venta y restaura el auto a disponible con validaciones"""
    try:
        cursor.execute("SELECT id_auto FROM ventas WHERE id = %s", (id_venta,))
        resultado = cursor.fetchone()
        
        if not resultado:
            print("❌ Venta no encontrada")
            return False

        id_auto = resultado[0]

        cursor.execute("UPDATE autos SET estado = 'Disponible' WHERE id = %s", (id_auto,))

        cursor.execute("DELETE FROM ventas WHERE id = %s", (id_venta,))

        conexion.commit()
        print("✅ Venta eliminada y auto restaurado")
        return True

    except Exception as e:
        print(f"❌ Error al eliminar venta: {e}")
        conexion.rollback()
        return False

def obtener_resumen_ventas():
    """Devuelve estadísticas de ventas con manejo de errores"""
    try:
        cursor.execute("SELECT COUNT(id), SUM(precio_venta) FROM ventas")
        total_ventas, total_ingresos = cursor.fetchone()
        
        
        cursor.execute("""
            SELECT metodo_pago, COUNT(*), SUM(precio_venta) 
            FROM ventas 
            GROUP BY metodo_pago
            ORDER BY COUNT(*) DESC
        """)
        por_metodo = cursor.fetchall()
        
       
        cursor.execute("""
            SELECT 
                DATE_FORMAT(fecha_venta, '%Y-%m') AS mes,
                COUNT(*) AS cantidad,
                SUM(precio_venta) AS total
            FROM ventas
            GROUP BY mes
            ORDER BY mes DESC
        """)
        por_mes = cursor.fetchall()
        
        return {
            'total_ventas': total_ventas or 0,
            'total_ingresos': float(total_ingresos) if total_ingresos else 0.0,
            'por_metodo_pago': por_metodo,
            'por_mes': por_mes
        }
    except Exception as e:
        print(f"❌ Error al obtener resumen: {e}")
        return None