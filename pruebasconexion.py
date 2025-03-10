# Importamos pymysql

import pymysql

# Creamos la conexión a la base de datos
conexion = pymysql.connect(host='localhost',user='root',password='',db='sakila')

try:
    with conexion.cursor() as cursor:
        # Creamos una consulta SQL
        consulta = "SELECT * FROM actor"
        # Ejecutamos la consulta
        cursor.execute(consulta)
        # Obtenemos los resultados
        resultados = cursor.fetchall()
        # Recorremos los resultados y los mostramos
        for resultado in resultados:
            print(resultado)
except Exception as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conexion.close()
    print("Conexión cerrada")