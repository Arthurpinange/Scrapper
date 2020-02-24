from DBconnection import DBConnection  as db
from customized.ScrapperSiteMaryKay import ScrapperSiteMaryKay as scmk
from customized.ScrapperSiteQuemDisse import ScrapperSiteMQuemDisse as scqd
from datetime import datetime
from customized.controllerLog import controllerLog as cLog
class Main:
    if __name__ == '__main__':
        for r in db.Get_SiteProduto():
            page = r["Page"]
            nome = r["Nome"]
            produto=[]
            if nome=="Mary kay":
                cLog.set_headLog(nome)
                produto = scmk.Get_Produto(page)
            if nome=="Quem Disse":
                cLog.set_headLog(nome)
                produto = scqd.Get_Produto(page)

            print(nome)
            print(page)

            if len(produto)>0:
                print("Os dados dos produtos da marca "+nome+" Serão armazenados no MongoDB Base Oncase Collection Produto!")
                ProdutoDelete = {"Marca": nome, "DataAcesso": datetime.today().strftime('%Y-%m-%d')}
                db.Del_Produto(ProdutoDelete)
                db.Set_Produto(produto)
            else:
                print("Nenhum Produto foi retornado")
                cLog.Set_LogErro("Nenhum Produto foi retornado")
