from flask_restful import Resource, reqparse
from sqlalchemy import select

from extensions import db
from model.Precio import Precio
from schema.PrecioSchema import precioSchema
from utils.util import decodificarPrecio


class PrecioResource(Resource):

    def get(self, articulo_id, precio_id):
        precio = db.session.execute(db.select(Precio).filter_by(articulo_id=articulo_id, id=precio_id)).scalar()
        if precio:
            return precioSchema.dump(precio)
        else:
            return {'message': 'Ningún precio encontrado'}, 404

    # def post(self):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('fecha', type=db.Date, required=True, help='Fecha del registro')
    #     parser.add_argument('precio', type=db.Double, required=True, help='Precio del registro')
    #     parser.add_argument('articulo_id', type=str, required=True, help='ID del articulo del registro')
    #
    #     args = parser.parse_args()
    #
    #     new_price = Precio(fecha=args['fecha'], precio=args['precio'], articulo_id=args['articulo_id'])
    #     db.session.add(new_price)
    #     db.session.commit()
    #     return "Precio registrado"