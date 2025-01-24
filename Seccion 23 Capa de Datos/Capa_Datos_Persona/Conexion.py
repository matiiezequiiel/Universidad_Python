from logger_base import *
import psycopg2 as bd
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USER_NAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None
        
    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(user=cls._USER_NAME,password=cls._PASSWORD,host=cls._HOST,port=cls._DB_PORT,database=cls._DATABASE)
                log.debug(f"Conexion exitosa: {cls._conexion}")
                return cls._conexion
            except Exception as e:
                log.error(f"Ocurrio una excepcion al obtener la conexion {e}")
                sys.exit()
        else:
            return cls._conexion
    
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f"Se abrio correctamente el cursor: {cls._cursor}")
                return cls._cursor
            except Exception as e:
                log.error(f"Ocurrio una excepcion al obtener el cursor {e}")
                sys.exit()
        else:
            return cls._cursor

    @classmethod
    def cerrar(cls):
        if cls._conexion is not None and cls._cursor is not None:
            try:
                cls._conexion.close()
                cls._cursor.close()
                log.debug(f"Se cerraron las conexiones correctamente {cls._cursor} {cls._conexion}")
            except Exception as e:
                log.error(f"Ocurrio una excepcion al cerrar la conexion {e}")
                sys.exit()
        else:
            log.debug(f"No se inicio la conexion")
            

if __name__ == "__main__":
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()
    Conexion.cerrar()