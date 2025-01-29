from logger_base import *
from Conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None
    
    def __enter__(self):
        log.debug(f'Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self,tipo_exepcion, valor_excepcion, detalle_excepcion):
        log.debug(f'Se ejecuta metodo exit __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion, se hace rollback: {valor_excepcion} {tipo_exepcion} {detalle_excepcion}')
        else:
            self._conexion.commit()
            log.error(f'Commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == "__main__":
    with CursorDelPool() as cursor:
        cursor.execute('SELECT * FROM persona')
        print(cursor.fetchall())
    