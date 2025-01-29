from usuario import Usuario
from logger_base import *
from cursor_del_pool import CursorDelPool

class UsuarioDao:
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario (username,password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            lista_usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0],registro[1],registro[2])
                lista_usuarios.append(usuario)
            return lista_usuarios
        
    @classmethod
    def insertar(cls,usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username,usuario.password)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount        
    
    @classmethod
    def actualizar(cls,usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username,usuario.password,usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount     
    
    @classmethod
    def eliminar(cls,usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount        

if __name__ == '__main__':
    #Prueba SELECT
    lista_usuarios = UsuarioDao.seleccionar()
    for usuario in lista_usuarios:
        log.debug(usuario)
    
    #Prueba INSERT
    # usuario1 = Usuario(username = 'Alejandra', password='Al3JaNdr4')
    # usuarios_insertadas = UsuarioDao.insertar(usuario1)
    # log.debug(f'Usuarios insertadas: {usuarios_insertadas}')
    
    #Prueba UPDATE
    # usuario1 = Usuario(id_usuario=8,username = 'camilarojas12', password='Cam1laR0jas$12')
    # usuarios_actualizadas = UsuarioDao.actualizar(usuario1)
    # log.debug(f'usuarios actualizadas: {usuarios_actualizadas}')
    
    #Prueba DELETE
    # usuario1 = Usuario(id_usuario=15)
    # usuarios_eliminadas = UsuarioDao.eliminar(usuario1)
    # log.debug(f'usuarios eliminadas: {usuarios_eliminadas}')