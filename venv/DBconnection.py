from pymongo import MongoClient
from customized.controllerLog import controllerLog as cLog

class DBConnection:
    def __init__(self):
        pass



    @staticmethod
    def Get_SiteProduto():
        '''
        returno a lista de sites
        :return:
        '''
        try:
            client = MongoClient('localhost', 27017)
            db = client['Oncase']
            site = db['Site']
            return site.find()
        except:
            cLog.Set_LogErro("Erro ao Acessa a base de dados")

    @staticmethod
    def Set_Produto(ListProduto):
        client = MongoClient('localhost', 27017)
        db = client['Oncase']
        produto = db['Produto']
        if len(ListProduto)>0:
           try:
               produto.insert_many(ListProduto)
               cLog.Set_LogSucess("Dados coletaos com Sucesso")
               print("Dados coletaos com Sucesso")
           except:
               cLog.Set_LogErro("Erro ao Inserir produto na base de dados")

    @staticmethod
    def Del_Produto(Where):
        client = MongoClient('localhost', 27017)
        db = client['Oncase']
        produto = db['Produto']

        try:
            produto.delete_many(Where)
        except:
            cLog.Set_LogErro("Erro ao deletar produto com a contição " +Where)
