import mysql.connector
from mysql.connector import Error


'''
peliculas=[ "john wick",
    "john wick: capítulo 2",
    "john wick: capítulo 3",
    "john wick: capítulo 4",
    "el origen",
    "el caballero de la noche",
    "transformers",
    "matrix",
    "gladiador",
    "interestelar",
    "el padrino",
    "el club de la pelea",
    "star war",
    "al filo del mañana",
    "spiderman"]
'''
#dict u objeto los atributos (nombre/categoria/clasificacion/genero/idioma)

'''
pelicula={
        "nombre":","
        "categoria""peliculas"
}
'''

pelicula={}

def borrarpantalla():
    import os
    os.system("cls")

def esperartecla():
    input("\n\toprima cualquier tecla para continuar... ")


def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas"

        )
        return conexion
    except Error as e:
        print(f"el error que se presento es: {e}")
        return None


def crearPeliculas():
  borrarpantalla()
  conexionBD=conectar()
  if conexionBD!=None:
      print("\n\t\t.:: Crear Películas ::. \n")
      pelicula.update({"nombre":input("\nIngresa el nombre: ").upper().strip()})
    # pelicula["nombre"]=input("\nIngresa el nombre: ").upper().strip()
      pelicula.update({"categoria":input("\nIngresa la categoría: ").upper().strip()})
      pelicula.update({"clasificacion":input("\nIngresa la clasificación: ").upper().strip()})
      pelicula.update({"genero":input("\nIngresa el genero: ").upper().strip()})
      pelicula.update({"idioma":input("\nIngresa el idioma: ").upper().strip()})
      ##### Sql para BD
      cursor=conexionBD.cursor()
      sql="insert into peliculas (nombre, categoria, clasificacion, genero, idioma) values ( %s, %s, %s, %s, %s)"
      val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"])
      cursor.execute(sql,val)
      conexionBD.commit()
      print("\n\t::: ¡LA OPERACIÓN SE REALIZÓ CON EXÍTO! :::")

def mostrarPeliculas():
  borrarpantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    cursor=conexionBD.cursor()
    sql="select * from peliculas"
    cursor.execute(sql)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelicula in registros:
        print(f"{pelicula[0]:<10}{pelicula[1]:<15}{pelicula[2]:<15}{pelicula[3]:<15}{pelicula[4]:<15}{pelicula[5]:<15}")
      print(f"-"*80) 
    else:
      print("\t ..:: No hay películas en el sistema ::. ")

def buscarPeliculas():
  borrarpantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    nombre=input("Ingresa el nombre de la pelicula a buscar: ").upper().strip()
    cursor=conexionBD.cursor()
    sql="select * from peliculas where nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelicula in registros:
        print(f"{pelicula[0]:<10}{pelicula[1]:<15}{pelicula[2]:<15}{pelicula[3]:<15}{pelicula[4]:<15}{pelicula[5]:<15}")
      print(f"-"*80) 
    else:
      print("\t ..:: Las películas a buscar no estan en el sistema ::. ")      

def borrarPeliculas():
  borrarpantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    nombre=input("Ingresa el nombre de la pelicula a borrar: ").upper().strip()
    cursor=conexionBD.cursor()
    sql="select * from peliculas where nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelicula in registros:
        print(f"{pelicula[0]:<10}{pelicula[1]:<15}{pelicula[2]:<15}{pelicula[3]:<15}{pelicula[4]:<15}{pelicula[5]:<15}")
      print(f"-"*80) 
      resp=input(f"¿Deseas borrar la pelicula {nombre}? (Si/No): ").lower().strip()
      if resp=="si":
        sql="delete from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        conexionBD.commit()
    else:
      print("\t ..:: Las películas a buscar no estan en el sistema ::. ")   

def modificarPeliculas():
  borrarpantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    nombre=input("Ingresa el nombre de la pelicula a modificar: ").upper().strip()
    cursor=conexionBD.cursor()
    sql="select * from peliculas where nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelicula in registros:
        print(f"{pelicula[0]:<10}{pelicula[1]:<15}{pelicula[2]:<15}{pelicula[3]:<15}{pelicula[4]:<15}{pelicula[5]:<15}")
      print(f"-"*80) 
      resp=input(f"¿Deseas borrar la pelicula {nombre}? (Si/No): ").lower().strip()
      if resp == "si":
              # Obtener nuevos datos
              nuevos_datos = {
                  "nombre": input("\nNuevo nombre: ").upper().strip(),
                  "categoria": input("Nueva categoría: ").upper().strip(),
                  "clasificacion": input("Nueva clasificación: ").upper().strip(),
                  "genero": input("Nuevo género: ").upper().strip(),
                  "idioma": input("Nuevo idioma: ").upper().strip()
              }
                
              # Actualizar en la base de datos
              sql_update = """
              UPDATE peliculas 
              SET nombre = %s, categoria = %s, clasificacion = %s, genero = %s, idioma = %s
              WHERE id = %s
              """
              val_update = (
                  nuevos_datos["nombre"],
                  nuevos_datos["categoria"],
                  nuevos_datos["clasificacion"],
                  nuevos_datos["genero"],
                  nuevos_datos["idioma"],
                  pelicula[0]  # ID de la película
              )
                
              cursor.execute(sql_update, val_update)
              conexionBD.commit()
                
              print("\n¡Película actualizada correctamente!")
      else:
          print("\nOperación cancelada")
    else:
        print("\nError: La película no existe en el sistema")
        
    cursor.close()
    conexionBD.close()
  else:
      print("\nError: No se pudo conectar a la base de datos")

