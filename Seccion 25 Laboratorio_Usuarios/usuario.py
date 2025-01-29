class Usuario:
    
    def __init__(self,id_usuario = None,username = None,password = None ):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password
    
    @property
    def id_usuario(self):
        return self._id_usuario
    
    @id_usuario.setter
    def id_usuario(self,id_usuario):
        self._id_usuario = id_usuario
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self,username):
        self._username = username
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,password):
        self._password = password
        
        
    def __str__(self):
        return(f''' 
Id: {self.id_usuario}
Username: {self.username}
Password: {self.password}''')
        

if __name__ == "__main__":
    usuario1 = Usuario(id_usuario=1,username="aguirre",password="maguirre@mail.com")
    print(usuario1)