# Scrapper de paginas de produtos

Esse Projeto coleta dados de produtos do site de duas grandes marcas de maquiagem.
Mary kay e Quem Disse.

O projeto foi desenvolvido em Python 3.7 persistindo os dados em uma base MongoDB

A  IDE usada para desenvolvimento foi a PyCharm

### Bibliotecas Python usadas:  
	* Pandas
	* Scrapper
	* pymongo
	* bs4

Base de Dados MongoDB 4.2.3 Community


## Segue um Passo a Passo de como configurar o ambiente para rodar a solução

### Instalação do Python e do pip para importar as bibliotecas:
	* sudo apt Install python3
	* sudo apt install python3-pip

### Importação das bibliotecas usadas pela solução
	* python -m pip install pandas
	* python -m pip install  Scrapper
	* python -m pip install pymongo
	* python -m pip install bs4


## Classe do da Solução:
	Main ⇒ Classe da a ser iniciada para realizar o scrapper
  	DBConnection ⇒ Classe responsável pelo acesso ao mongodb
  	scrapper ⇒ Classe responsável pelos métodos de scrapper

Dentro do diretório customised temos as classe responsáveis pelo tratamento do sopa de letrinhas(html) retornado pelo scrapper

	scrapperSiteMaryKay ⇒ Trata retorno do site da Mary Kay
	ScrapperSiteQuemDisse ⇒ Trata retorno do site da Quem Disse

Também implementei um log de arquivo apenas para uma rápida auditório em caso de falha.

	ControllerLog ⇒ Log da aplicação


## Para configurar a base de dados em mongodb disponibilizamos um backup com as collections que usamos para armazenar o resultado do nosso scrapper.

### instalação do mongodb
	sudo apt install mongodb

### fica no diretório Scrapper/db/Oncase.json/Oncase/
	mongorestore -d Oncase ./Scrapper/db/Oncase.json/Oncase/

### Com isso já temos todo o ambiente pronto para uso, agora é só acessar o diretório Scrapper/venv/ e executar o arquivo Main.py
	python3 Main.py

### os dados serão armazenados na collection produto da base de dados Oncase. estamos coletando os seguintes dados:
	Marca, Nome do produto, Preço, URL da imagem, e Data de Acesso.

### temos uma segunda Collection chamada Site, responsável por armazenar a url das páginas web a serem varridas pela solução.
	Marca, url page, Data Acesso


## Segue o link do visual do power Bi onde eu realizo uma análise do dados coletados
