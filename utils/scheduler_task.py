from extensions import scheduler
from resources.ArticuloListResource import ArticuloListResource
from resources.ArticuloResource import ArticuloResource
from utils.wepScrapping import makeWebScrapping


def update_database():
    with scheduler.app.app_context():
        for articulo in ArticuloListResource().get():
            makeWebScrapping(articulo)

