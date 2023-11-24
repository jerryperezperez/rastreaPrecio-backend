from flask_restful import Resource, reqparse
from extensions import db
from model.Articulo import Articulo
from schema.ArticuloSchema import articuloSchema, articulosSchema
from schema.PrecioSchema import preciosSchema


class ArticuloListResource(Resource):

    def get(self):
        articulos = db.session.execute(db.select(Articulo)).scalars()
        # objetos = articulosSchema.dump(articulos)
        resultado = [articuloSchema.to_json(articulo) for articulo in articulos]
        return resultado

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