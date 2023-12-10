# from utils.wepScrapping import makeWebScrapping
# from model import Articulo

# name = 'Cafetera Black&decker 12 Tazas'
# url = 'https://www.google.com/search?q=cafetera+walmart&client=opera&hs=hLk&sa=X&sca_esv=e233ecf3a37d0d56&sca_upv=1&biw=1304&bih=601&tbm=shop&sxsrf=AM9HkKnEZFhpk4Ol-hMzuZyJ4TL_CothJw%3A1702141097321&ei=qZx0ZaDhErCdwbkP44qe0As&ved=0ahUKEwjg2dnb6YKDAxWwTjABHWOFB7oQ4dUDCAg&uact=5&oq=cafetera+walmart&gs_lp=Egtwcm9kdWN0cy1jYyIQY2FmZXRlcmEgd2FsbWFydDIKEAAYgAQYDRjWBTIKEAAYgAQYDRjWBTIKEAAYgAQYDRjWBTIKEAAYgAQYDRjWBTIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHkiwW1AAWL9acAN4AJABA5gBugGgAes1qgEENS41M7gBA8gBAPgBAagCCsICBBAjGCfCAgcQIxjqAhgnwgIEEAAYHsICDBAAGIAEGA0Y1gUYCogGAQ&sclient=products-cc'
# store = 'Walmart Súper'
# articulo = {"name":name, "url": url, "store":store}

# makeWebScrapping(articulo)

from bs4 import BeautifulSoup

import requests 
URL = "https://www.amazon.com.mx/s?k=Cybersecurity+for+Small+Networks%3A+A+Guide+for+the+Reasonably+Paranoid&__mk_es_MX=ÅMÅŽÕÑ&crid=N9JJOHUKD4PF&sprefix=cybersecurity+for+small+networks+a+guide+for+the+reasonably+paranoid%2Caps%2C216&ref=nb_sb_noss"
r = requests.get(URL) 

soup = BeautifulSoup(r.text)
print(soup) 