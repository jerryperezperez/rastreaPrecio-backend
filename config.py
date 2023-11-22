import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler


app = Flask(__name__)

api = Api(app)
CORS(app, origins='http://localhost:4200/')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")  # Cambia la URI según tu base de datos
db = SQLAlchemy(app)
migrate = Migrate(app, db)
scheduler = APScheduler()

scheduler.init_app(app)


@scheduler.task('interval', id='my_job', seconds=7)
def my_job():
        # ArticuloList.get()
        # print(funcionUtil(1))
        print('This job is executed every 10 seconds.')

scheduler.start()