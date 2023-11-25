from flask_restful import Resource, reqparse
from extensions import db
from model.Articulo import Articulo
from schema.ArticuloSchema import articuloSchema, articulosSchema
from schema.PrecioSchema import preciosSchema


class ArticuloResource(Resource):

    def get(self, articulo_id):
        articulo = db.session.execute(db.select(Articulo).filter_by(id=articulo_id)).scalar()
        if articulo:
            objeto = articuloSchema.dump(articulo)
            objeto["precios"] = preciosSchema.dump(articulo.precios)
            return objeto
        else:
            return {'message': 'Producto no encontrado'}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Nombre del producto')
        parser.add_argument('url', type=str, required=True, help='URL del producto')
        parser.add_argument('store', type=str, required=True, help='Tienda del producto')

        args = parser.parse_args()

        # TODO Retornar ID del objeto recién creado

        new_product = Articulo(name=args['name'], url=args['url'], store=args['store'])
        db.session.add(new_product)
        db.session.commit()
        return "todo bien"

    def delete(self, articulo_id):
        articulo = db.session.execute(db.select(Articulo).filter_by(id=articulo_id)).scalar()
        if articulo:
            Articulo.delete(articulo)
            return "eliminado  exitosamente"
        else:
            return {'message': 'Producto no encontrado'}, 404
