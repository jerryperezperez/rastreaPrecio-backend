from datetime import date
from extensions import scheduler
from model import Precio
from resources.ArticuloListResource import ArticuloListResource

from utils.webscrapping import amazonScrapping
from utils.webscrapping import mercadoLibreScrapping
from utils.webscrapping import chedrauiScrapping
from utils.webscrapping import walmartScrapping
from utils.webscrapping import wepScrapping


def update_database():
    fecha_actual = date.today()

    # print(fecha_actual)
    with scheduler.app.app_context():

        for articulo in ArticuloListResource().get():
            recuperado = False
            # Inicializando el precio para cada articulo
            price = None
            print(articulo["name"])
            print(articulo["website"])
            print("----------------------------------------------------------------------")
            # Instrucciones para simular el switch case en Python y ejecutar de acuerdo al website
            if articulo["website"] == "Google":
                try:
                    price = wepScrapping.makeWebScrapping(articulo)
                    recuperado = True
                except:
                    print("No se ha podido recuperar información del sitio web Google Shopping")

            if articulo["website"] == "Amazon":
                try:
                    price = amazonScrapping.makeScrapping(articulo)["price"]
                    recuperado = True
                except:
                    print("No se ha podido recuperar información del sitio web Amazon")

            if articulo["website"] == "Chedraui":
                try:
                    price = chedrauiScrapping.makeScrapping(articulo)["price"]
                    recuperado = True
                except:
                    print("No se ha podido recuperar información del sitio web Chedraui")

            if articulo["website"] == "Mercado Libre":
                try:
                    price = mercadoLibreScrapping.makeScrapping(articulo)["price"]
                    recuperado = True
                except:
                    print("No se ha podido recuperar información del sitio web Mercado Libre")

            if articulo["website"] == "Walmart":
                try:
                    price = walmartScrapping.makeScrapping(articulo)["price"]
                    recuperado = True
                except:
                    print("No se ha podido recuperar información del sitio web Walmart")
            # Se intenta agregar el precio en la base de datos en caso de que se obtenga el precio
            if recuperado == True:
                print("id_articulo: ", articulo["id"])
                Precio(fecha=fecha_actual, precio=price, articulo_id=articulo["id"]).save()


                    

