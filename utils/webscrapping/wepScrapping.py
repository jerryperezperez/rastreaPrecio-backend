import json
import re
from datetime import date

import requests
from bs4 import BeautifulSoup

#TODO Modificar el uso de requests por el de selenium para verificar si mejora la consistencia en la
# informacion extraida
def makeWebScrapping(articulo):
        print(articulo["name"])
        response = requests.get(articulo["url"])

        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Parsear el contenido HTML de la página
            soup = BeautifulSoup(response.text, 'html.parser')
            print("bien con la url")
        else:
            print(f'Error al hacer la solicitud. Código de estado: {response.status_code}')

        texto = soup.get_text()
        newText = texto[texto.index("- Google")::]
        # print(newText)

        newText = newText[newText.index(articulo["name"])::]

        print("BIEN CON ENCONTRAR EL NOMBRE")
        newText = newText[newText.index("MXN")::]
        newText[0:newText.index(articulo["store"])]
        print("BIEN CON ENCONTRAR LA TIENDA")
        # Buscar todas las cifras (incluyendo punto decimal) en el texto usando una expresión regular
        cifras_encontradas = re.findall(r"([0-9,]+(\.[0-9]+)?)", newText[0:newText.index(articulo["store"])])

        # Extraer las cantidades encontradas
        cantidades = [float(coincidencia[0].replace(",", "")) for coincidencia in cifras_encontradas]

        print(cantidades[0])
        return cantidades[0]
