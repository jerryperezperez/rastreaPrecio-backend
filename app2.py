# from flask_cors import cross_origin, CORS
# from flask_restful import Resource, reqparse
# CORS(app)
#
# def algo(articulo_id):
#     return ArticuloList.get()
# class ArticuloResource(Resource):
#     @cross_origin()
#     def get(self, articulo_id):
#         # Lógica para obtener un producto por ID
#         articulo = Articulo.query.get(articulo_id)
#         precios = [decodificarPrecio(objeto_precio) for objeto_precio in articulo.precios]
#         if articulo:
#             return {'id': articulo.id, 'name': articulo.name, 'url': articulo.url, 'store': articulo.store,
#                     'precios': precios}
#         else:
#             return {'message': 'Producto no encontrado'}, 404
#
#
# # class PrecioResource(Resource):
# #     @cross_origin()
# #     def get(self, articulo_id):
# #         stmt = select(Precio).where(Precio.id_producto == articulo_id)
# #         result = db.session().execute(stmt)
# #         precios = [decodificarPrecio(objeto_precio) for objeto_precio in result.scalars()]
# #
# #         if precios:
# #             return precios
# #         else:
# #             return {'message': 'Ningún precio encontrado'}, 404
#
#
# class ArticuloList(Resource):
#     @cross_origin()
#     def get(self):
#         articulos = db.session.query(Articulo)
#         articulos = [{'id': articulo.id, 'name': articulo.name, 'url': articulo.url, 'store': articulo.store,
#                       'precios': [decodificarPrecio(objeto_precio) for objeto_precio in articulo.precios]} for articulo in articulos]
#
#         return articulos
#
#     @cross_origin()
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('name', type=str, required=True, help='Nombre del producto')
#         parser.add_argument('url', type=str, required=True, help='URL del producto')
#         parser.add_argument('store', type=str, required=True, help='Tienda del producto')
#
#         args = parser.parse_args()
#
#         new_product = Articulo(name=args['name'], url=args['url'], store=args['store'])
#         db.session.add(new_product)
#         db.session.commit()
#         return "todo bien"
#
#
#
# api.add_resource(ArticuloResource, '/articulo/<articulo_id>')
# api.add_resource(PrecioResource, '/precio/<articulo_id>')
# api.add_resource(ArticuloList, '/articulo')


# @scheduler.task('interval', id='my_job', seconds=7)
# def my_job():
#
#     with app.request_context():
#         # ArticuloList.get()
#         # print(funcionUtil(1))
#         print('This job is executed every 10 seconds.')
