from model.Articulo import Articulo


def decodificarPrecio(objeto_precio):
    return {'id': objeto_precio.id, 'id_producto': objeto_precio.id_producto,
                            'fecha': objeto_precio.fecha.isoformat(), 'precio': objeto_precio.precio}

def funcionUtil(articulo_id):
    articulo = Articulo.query.get(articulo_id)
    precios = [decodificarPrecio(objeto_precio) for objeto_precio in articulo.precios]
    if articulo:
        return {'id': articulo.id, 'name': articulo.name, 'url': articulo.url, 'store': articulo.store,
                'precios': precios}
    else:
        return {'message': 'Producto no encontrado'}, 404