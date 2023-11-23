import os

from flask import Flask, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
# from flask_uploads import configure_uploads, patch_request_class

from config import Config
from extensions import db, scheduler

from resources.PrecioResource import PrecioResource
from resources.ArticuloResource import ArticuloResource
from resources.ArticuloListResource import ArticuloListResource
from scheduleTask import job1


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

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):
    CORS(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    scheduler.init_app(app)
    scheduler.start()
    scheduler.add_job(func=job1, trigger='interval', seconds=4, id="dd")

def register_resources(app):
    api = Api(app)

    api.add_resource(PrecioResource, '/precio')
    api.add_resource(ArticuloListResource, '/articulo')
    api.add_resource(ArticuloResource, '/articulo/<articulo_id>')



if __name__ == '__main__':
    app = create_app()
    app.run(use_reloader=False)