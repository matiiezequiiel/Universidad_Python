# GUI - Graphical User Interface
# Tkinter - TK Interface
# Importamos el módulo de tkinter
import tkinter as tk
# Importamos el módulo del tema de tkinter
from tkinter import ttk

# Creamos un objeto usando la clase Tk
ventana = tk.Tk()
# Modificamos el tamaño de la ventana (pixeles)
ventana.geometry('600x400')
# Cambiamos el nombre de la ventana
ventana.title('Hola Mundo')
# Configuramos el ícono de la aplicación
ventana.iconbitmap('Seccion 54 Interfaces graficas GUI\\icono.ico')
# Creamos un boton (widget), el objeto padre es ventana
boton1 = ttk.Button(ventana, text='Dar click')
# Utilizar el pack layout manager para mostrar el botón de la ventana
boton1.pack()
# Iniciamos la ventana (esta línea la ejecutamos al final)
# Si la ejecutamos antes, no se muestran los cambios anteriores
ventana.mainloop()