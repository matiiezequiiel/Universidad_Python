import urllib.request
import json

peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/api/clima.json',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
respuesta = urllib.request.urlopen(peticion)
cuerpo_respuesta = respuesta.read()
json_respuesta = json.loads(cuerpo_respuesta.decode("utf-8"))
# Es una diccionario de key CLIMA en donde los valores es un array de diccionarios.
print(f'Descripcion: {json_respuesta["clima"][0]["descripcion"]}')
# Es una diccionario de key PRINCIPAL en donde los valores es un diccionario.
print(f'Temp minima: {json_respuesta["principal"]["temp_min"]}')
print(f'Temp minima: {json_respuesta["principal"]["temp_max"]}')
