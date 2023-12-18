import time
from bs4 import BeautifulSoup
from selenium import webdriver

def makeScrapping(articulo):
    driver = webdriver.Chrome() # This is a simplified example
    driver.get(articulo["url"])

    time.sleep(5)

    print("conectado")
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()

    ## Extrayendo los datos desde el html recuperado
    name = soup.find("span", class_="vtex-store-components-3-x-productBrand--global__product--name").getText()
    price = soup.find("span", class_="chedrauimx-frontend-applications-4-x-productPriceSellingContainerQSPDP").getText()
    price = price.replace("$", "")
    print(name)
    print(price)