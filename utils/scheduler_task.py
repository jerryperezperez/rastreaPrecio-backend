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
    # print(fecha_actual)
    with scheduler.app.app_context():
        for articulo in ArticuloListResource().get():
            recuperado = True
            print("----------------------------------------------------------------------")

            try:
                precio = makeWebScrapping(articulo)
                # Se analiza de nuevo debido a una posible falla al extraer el precio laprimera vez
                precio = makeWebScrapping(articulo)

            except:
                print("there was a problem retrieving information about", articulo["name"])
                recuperado = False
            
            if recuperado == True:
                print("id_articulo: ", articulo["id"])
                Precio(fecha=fecha_actual, precio=precio, articulo_id=articulo["id"]).save()


                    

