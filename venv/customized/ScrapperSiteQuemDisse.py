from  Scrapper import scrapper as sc
from datetime import datetime
class ScrapperSiteMQuemDisse:
    def __init__(self):
        pass

    @staticmethod
    def Get_Produto(url):
        soup =  sc.Get_Soup(url)
        mydivs = soup.find_all("div",class_ = "product")
        lista = []
        for div in mydivs:
            TagProductName = div.find_all("div", class_="product-content")
            texto = TagProductName[0].text.split('\n')
            TagImage = div.find_all("img")
            productImage = TagImage[0].get('src')

            contador = 0
            for r in texto:
                if r != '':
                    contador = contador + 1
                    if contador == 1:
                        productname = r
                    if contador == 2:
                        valor = r.replace("R$", "").replace(",", ".")
                        productPrice = float(valor)

            ProductDataAcesso = datetime.today().strftime('%Y-%m-%d')
            lista.append({"Marca":"Quem Disse","Nome":productname,"Preco":productPrice,"imagem":productImage,"DataAcesso":ProductDataAcesso})

        return lista
