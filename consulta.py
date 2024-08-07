#modulo1

import requests
import json

#esta funcion entrega tosos lod datos de la api para ser manejador en el diccionario
def request_get(url):
    response = requests.get(url)
    datos =json.loads(response.text)
    return datos



# url= 'https://aves.ninjas.cl/api/birds'

# resultados = request_get(url)


# print(resultados[0]['name'] ['spanish'])