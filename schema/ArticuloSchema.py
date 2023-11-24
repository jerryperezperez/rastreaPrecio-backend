from extensions import marshmallow
from model import Articulo
from schema.PrecioSchema import PrecioSchema


class ArticuloSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Articulo

    def to_json(self, articulo):
        objeto = self.dump(articulo)
        print(articulo)
        objeto["precios"] = PrecioSchema(many=True).dump(articulo.precios)
        return objeto

articuloSchema = ArticuloSchema()
articulosSchema = ArticuloSchema(many=True)
