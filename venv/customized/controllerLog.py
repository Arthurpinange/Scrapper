from datetime import datetime

class controllerLog:

    def __init__(self):
        pass


    @staticmethod
    def Set_LogErro(texto):
        arqv = open("Controller.txt","a")
        arqv.write("Erro: "+texto+"\n")
        arqv.close()

    @staticmethod
    def set_headLog(marca):
        arqv = open("Controller.txt", "a")
        arqv.write("************* "+datetime.today().strftime('%Y-%m-%d')+" ***************\n")
        arqv.write(marca)

        arqv.close()


    @staticmethod
    def Set_LogSucess(texto):
        arqv = open("Controller.txt", "a")
        arqv.write("Sucess: " + texto + "\n")
        arqv.close()