from flask_sqlalchemy import SQLAlchemy

from flask_apscheduler import APScheduler
# from flask_apscheduler import BackgroundScheduler
db = SQLAlchemy()
scheduler = APScheduler()

