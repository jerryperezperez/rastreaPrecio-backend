from extensions import db


class Articulo(db.Model):
    __tablename__ = "articulo"
    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(500), nullable=False, unique=True)
    url = db.Column(db.String(800), nullable=False, unique=True)
    store = db.Column(db.String(255), nullable=False)
    # Indica si la busqueda se realiza con Google Shopping o de la propia tienda
    website = db.Column(db.String(255), nullable=False)
    precios = db.relationship('Precio', backref='articulo')

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            print("hecho rollback")

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
            print("hecho rollback")
