from marshmallow import Schema, fields
from extensions import marshmallow
from model import Precio
from schema import ArticuloSchema


class PrecioSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Precio
        include_fk = True

precioSchema = PrecioSchema()
preciosSchema = PrecioSchema(many=True)
