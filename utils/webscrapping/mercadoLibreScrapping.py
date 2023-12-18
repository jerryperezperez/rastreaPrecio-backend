import time
from bs4 import BeautifulSoup
from selenium import webdriver


def makeScrapping(articulo):
    driver = webdriver.Chrome() # This is a simplified example
    driver.get(articulo["url"])

    print("conectado")
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()

    ## Extrayendo los datos desde el html recuperado
    name = soup.find("h1", class_="ui-pdp-title").getText()
    price = None
    tags = soup.find_all('meta')
    for tag in tags:
        try:
            if tag['itemprop'] == 'price':
                price = tag['content']
        except:
            print("Unable to get price")
    print(name)
    print(price)

    return {"name": name, "price":price}