import os

from flask import Flask
from flask_cors import CORS
from extensions import db, scheduler, marshmallow, migrate, api
from resources import PrecioResource, ArticuloResource, PrecioListResource
from resources.ArticuloListResource import ArticuloListResource
from utils.scheduler_task import update_database


def create_app():

    env = os.environ.get('ENV', 'Development')

    if env == 'Production':
        config_str = 'config.ProductionConfig'
    elif env == 'Staging':
        config_str = 'config.StagingConfig'
    else:
        config_str = 'config.DevelopmentConfig'

    app = Flask(__name__)
    app.config.from_object(config_str)

    register_resources(api)

    register_extensions(app)


    return app


def register_extensions(app):
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)
    api.init_app(app)

    scheduler.init_app(app)
    scheduler.start()
    scheduler.add_job(func=update_database, trigger='interval', seconds=60, id="dd")

def register_resources(api):

    api.add_resource(ArticuloListResource, '/articulos')
    api.add_resource(ArticuloResource, '/articulos/<articulo_id>')
    api.add_resource(PrecioListResource, '/articulos/<articulo_id>/precios')
    api.add_resource(PrecioResource, '/articulos/<articulo_id>/precios/<precio_id>')


if __name__ == '__main__':
    app = create_app()
    app.run()
