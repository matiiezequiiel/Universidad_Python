import psycopg2 as bd

conexion = bd.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

# Con with tanto el commit como el rollback se hacen de forma automatica
try:
    with conexion: 
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Matias', 'Aguirre', 'maguirre@mail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan', 'Perez','juanperez@mail.com', 1)
            cursor.execute(sentencia, valores)
except Exception as e:
    print(f'Ocurrió un error, se hizo rollback: {e}')
finally:
    conexion.close()
print('Termina la transacción, se hizo commit')
    