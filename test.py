from utils.wepScrapping import makeWebScrapping
from model import Articulo

name = 'BASE DE DATOS'
url = 'https://www.google.com/search?q=base+de+datos+libro+amazon&client=opera&hs=16z&sca_esv=da5e68172fb73226&sca_upv=1&biw=1304&bih=601&tbm=shop&sxsrf=AM9HkKkp-JDhv6ZJTz4TnAW-FZodq06Yfw%3A1701883930391&ei=GrBwZdCIF4SbwbkP2_S3mAk&ved=0ahUKEwjQ_fnYq_uCAxWETTABHVv6DZMQ4dUDCAg&uact=5&oq=base+de+datos+libro+amazon&gs_lp=Egtwcm9kdWN0cy1jYyIaYmFzZSBkZSBkYXRvcyBsaWJybyBhbWF6b25ItBZQwgJYvhRwAngAkAEAmAGNAaABqAmqAQQwLjEwuAEDyAEA-AEBwgIEECEYCogGAQ&sclient=products-cc'
store = 'Amazon'
articulo = {"name":name, "url": url, "store":store}

makeWebScrapping(articulo)