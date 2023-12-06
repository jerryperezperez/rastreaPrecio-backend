# from app import db
from sqlalchemy import ForeignKey, UniqueConstraint
from extensions import db

class Precio(db.Model):
    __tablename__ = "precio"
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    precio = db.Column(db.Double, nullable=False)
    articulo_id = db.Column(db.Integer, db.ForeignKey('articulo.id'))
    __table_args__ = (UniqueConstraint("fecha", "articulo_id"),)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()