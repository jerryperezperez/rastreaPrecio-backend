import json
import re
from datetime import date

import requests
from bs4 import BeautifulSoup

def makeWebScrapping(articulo):
        print(articulo)
        response = requests.get(articulo["url"])
        fecha_actual = date.today()
        print(fecha_actual)

        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Parsear el contenido HTML de la página
            soup = BeautifulSoup(response.text, 'html.parser')
        else:
            print(f'Error al hacer la solicitud. Código de estado: {response.status_code}')

        texto = soup.get_text()
        newText = texto[texto.index("- Google")::]

        newText = newText[newText.index(articulo["name"])::]

        newText = newText[newText.index("MXN")::]
        newText[0:newText.index(articulo["store"])]

        # Buscar todas las cifras (incluyendo punto decimal) en el texto usando una expresión regular
        cifras_encontradas = re.findall(r"([0-9,]+(\.[0-9]+)?)", newText[0:newText.index(articulo["store"])])

        # Extraer las cantidades encontradas
        cantidades = [float(coincidencia[0].replace(",", "")) for coincidencia in cifras_encontradas]

        print(cantidades[0])
