from usuarioDao import UsuarioDao,Usuario

salir = False

print('Iniciando el sistema de Usuarios')
while not salir:
    print(f'''Menu:
    1. Listar usuarios
    2. Agregar usuario
    3. Actualizar usuario
    4. Eliminar usuario
    5. Salir''')
    opcion = int(input('Escoje una opción: '))
    if opcion == 1:
        lista_usuarios = UsuarioDao.seleccionar()
        for usuario in lista_usuarios:
            print(usuario)
    elif opcion == 2:
        username = input("Ingrese el nombre de usuario: ")
        password = input("Ingrese la password: ")
        usuario_alta = Usuario(username=username,password=password)
        UsuarioDao.insertar(usuario_alta)
    elif opcion == 3:
        id_actualizar = input("Ingrese el id del usuario a actualizar: ")
        user_actualizar = input("Ingrese el nuevo username: ")
        pass_actualizar = input("Ingrese la nueva password: ")
        usuario_actualizar = Usuario(id_usuario=id_actualizar,username=user_actualizar,password=pass_actualizar)
        UsuarioDao.actualizar(usuario_actualizar)
    elif opcion == 4:
        id_eliminar = input("Ingrese el id del usuario a eliminar: ")
        usuario_eliminar = Usuario(id_usuario=id_eliminar)
        UsuarioDao.eliminar(usuario_eliminar)
    elif opcion == 5:
        print('Saliendo del sistema. Hasta pronto!\n')
        salir = True
    else:
        print('Opción inválida, proporciona otra opción...\n')
else:
    print('Terminando el sistema de Usuarios')
    