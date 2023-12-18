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
    name = soup.find("h1", class_="lh-copy").getText()
    price = soup.find("span", class_="flex-column").getText()
    price = price.replace("$", "")
    print(name)
    print(price)

    return {"name": name, "price": price}