from  Scrapper import scrapper as sc
from datetime import datetime
class ScrapperSiteMaryKay:
    def __init__(self):
        pass

    @staticmethod
    def Get_Produto(url):
        soup =  sc.Get_Soup(url)
        mydivs = soup.find_all("div", class_="product cf")
        lista = []
        for div in mydivs:
            TagProductName = div.find_all("a", class_="product-name")
            TagProductType = div.find_all("span", class_="name")
            TagPreco = div.find_all("p", class_="price")
            TagImage = div.find_all("img")

            productname = TagProductName[0].text +" "+TagProductType[0].text
            productPrice = TagPreco[0].text.replace("R$", "")
            productPrice = float(productPrice) / 100
            productImage = TagImage[0].get('src').replace("//", "")
            ProductDataAcesso = datetime.today().strftime('%Y-%m-%d')
            lista.append({"Marca":"Mary kay","Nome":productname,"Preco":productPrice,"imagem":productImage,"DataAcesso":ProductDataAcesso})

        return lista
