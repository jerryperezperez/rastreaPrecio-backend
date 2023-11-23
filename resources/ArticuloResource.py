from flask_restful import Resource

from model.Articulo import Articulo
from utils.util import decodificarPrecio


class ArticuloResource(Resource):

    def get(self, articulo_id):
        # Lógica para obtener un producto por ID
        articulo = Articulo.query.get(articulo_id)
        precios = [decodificarPrecio(objeto_precio) for objeto_precio in articulo.precios]
        if articulo:
            return {'id': articulo.id, 'name': articulo.name, 'url': articulo.url, 'store': articulo.store,
                    'precios': precios}
        else:
            return {'message': 'Producto no encontrado'}, 404