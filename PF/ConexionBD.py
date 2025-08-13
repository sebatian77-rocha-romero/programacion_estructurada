import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",      
        user="root",          
        password="",           
        database="bd_agencia_de_autos", 
            
    )
    cursor = conexion.cursor(buffered=True) 
except mysql.connector.Error as err:
    print(f"No se pudo conectar a la base de datos. Error: {err}")
    conexion = None
    cursor = None
