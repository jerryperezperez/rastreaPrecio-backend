from flask_restful import Resource


from model.Precio import Precio
from utils.util import decodificarPrecio


class PrecioResource(Resource):

    def get(self, articulo_id):
        result = Precio.query.where(Precio.id_producto == articulo_id)
        # stmt = select(Precio).where()
        # result = db.session().execute(stmt)
        precios = [decodificarPrecio(objeto_precio) for objeto_precio in result.scalars()]

        if precios:
            return precios
        else:
            return {'message': 'Ningún precio encontrado'}, 404
