import pandas as pd
import requests
from bs4 import BeautifulSoup

class scrapper:

    def __init__(self):
        pass


    @staticmethod
    def Get_Soup( url):
        '''
        returna o resultado do rtml da pagina pronto para ser varrido
        :param url:
        :return:
        '''
        req = requests.get(url)
        if req.status_code == 200:
            content = req.content
            soup = BeautifulSoup(content, 'html.parser')

        return soup

