try:
    archivo = open('prueba.txt', 'w')
    archivo.write('Agregamos informacion al archivo\nAdios')
except Exception as e:
    print(e)
finally:
    archivo.close()