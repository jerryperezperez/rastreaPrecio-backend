from flask_cors import cross_origin
from flask_restful import Resource, reqparse
from extensions import db
from model.Articulo import Articulo
from utils.util import decodificarPrecio


class ArticuloListResource(Resource):
    @cross_origin()
    def get(self):
        articulos = db.session.query(Articulo)
        articulos = [{'id': articulo.id, 'name': articulo.name, 'url': articulo.url, 'store': articulo.store,
                      'precios': [decodificarPrecio(objeto_precio) for objeto_precio in articulo.precios]} for articulo in articulos]

        return articulos

    @cross_origin()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Nombre del producto')
        parser.add_argument('url', type=str, required=True, help='URL del producto')
        parser.add_argument('store', type=str, required=True, help='Tienda del producto')

        args = parser.parse_args()

        new_product = Articulo(name=args['name'], url=args['url'], store=args['store'])
        db.session.add(new_product)
        db.session.commit()
        return "todo bien"