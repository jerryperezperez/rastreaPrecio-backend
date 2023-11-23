from extensions import scheduler
from resources.ArticuloResource import ArticuloResource
from datetime import datetime

def job1():
    with scheduler.app.app_context():
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)

    #     print(ArticuloResource().get(articulo_id=7))