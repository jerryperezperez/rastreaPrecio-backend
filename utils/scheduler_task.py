from datetime import date

from extensions import scheduler
from model import Precio
from resources.ArticuloListResource import ArticuloListResource
from resources.ArticuloResource import ArticuloResource
from schema.ArticuloSchema import ArticuloSchema
from schema.PrecioSchema import PrecioSchema
from utils.wepScrapping import makeWebScrapping


def update_database():
    fecha_actual = date.today()
    print(fecha_actual)
    with scheduler.app.app_context():
        for articulo in ArticuloListResource().get():
            print("------------------------------------------------------------------------------------------")

            try:
                Precio(fecha=fecha_actual, precio=makeWebScrapping(articulo), articulo_id=articulo["id"]).save()
            except:
                try:
                    Precio(fecha=fecha_actual, precio=makeWebScrapping(articulo), articulo_id=articulo["id"]).save()
                except:
                    print("there was a problem retrieving information about", articulo["name"])
