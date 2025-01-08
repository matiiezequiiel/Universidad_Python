from random import randint

print("*** Sistema generador de ID unico\n")
nombre = input("¿Cual es tu nombre?: ")
apellido = input("\n¿Cual es tu apellido?: ")
año_nacimiento = input("\n¿Cual es tu año de nacimiento (YYYY)?: ")

clave_unica = f"{nombre[0:2].upper()}{apellido[0:2].upper()}{año_nacimiento[2:4].upper()}{randint(1,9999)}"
# clave_unica2 = "{}{}{}{}".format(nombre[0:2].upper(),apellido[0:2].upper(),año_nacimiento[2:4].upper(),randint(1,9999))

print(f'''Hola {nombre},
      Tu nuevo numero de identificacion (ID) generado por el sistema es:
      {clave_unica}
      Felicidades!''')

