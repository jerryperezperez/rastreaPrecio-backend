from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
# from flask_apscheduler import BackgroundScheduler
db = SQLAlchemy()
scheduler = APScheduler()
marshmallow = Marshmallow()
migrate = Migrate()
api = Api()

