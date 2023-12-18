import time

from bs4 import BeautifulSoup
from selenium import webdriver

def makeScrapping(articulo):
    driver = webdriver.Chrome() # This is a simplified example
    driver.get(articulo['url'])

    time.sleep(5)
    print("conectado")

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()
    ## Extrayendo los datos desde el html recuperado
    name = soup.find("span", id="productTitle").getText()
    price = soup.find("span", class_="a-offscreen").getText()
    #Removing the dollar sign
    price = price.replace("$", "")
    print(name)
    print(price)
    return {"name": name, "price": price}