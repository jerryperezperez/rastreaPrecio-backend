from flask_restful import Resource, reqparse
from extensions import db
from model import Precio


class PrecioListResource(Resource):

    def get(self):

        return ""

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('fecha', type=str, required=True, help='Fecha del registro')
        parser.add_argument('precio', type=float, required=True, help='Precio del registro')
        parser.add_argument('articulo_id', type=str, required=True, help='ID del articulo del registro')

        args = parser.parse_args()

        new_price = Precio(fecha=args['fecha'], precio=args['precio'], articulo_id=args['articulo_id'])
        db.session.add(new_price)
        db.session.commit()
        return "Precio registrado"