from pathlib import Path # importando Path - Para pegar raiz do nosso projeto
from selenium import webdriver # importando a webdriver
from selenium.webdriver.chrome.service import Service # Importando o Service - precisamos dele
from time import sleep # para o tempo
import os # importando o os


ROOT_PATH = Path(__file__).parent.parent # pegar raiz do projeto - nome da pasta raiz
CHROMEDRIVER_NAME = 'chromedriver' # nome do chromedriver
CHROMEDRIVER_PATH = ROOT_PATH / 'bin' / CHROMEDRIVER_NAME # caminho completo do projeto ate o chromedriver


# funcao para criar o nosso browser - parar de execurta o browser aleatoriamente
# --headless - opcao do chromedriver que nao abre o navegador
def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions() # para passar opções ao webdriver quando exercutado

    # verificao pra sabe se tem o options
    if options is not None:
        for option in options:
            chrome_options.add_argument(option) # adicionando argumentos na nossas options

    if os.environ.get('SELENIUM_HEADLESS') == '1':
        chrome_options.add_argument('--headless')

    chrome_service = Service(executable_path=CHROMEDRIVER_PATH) # para passamos onde esta nosso chromedriver
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options) # criando o nosso browser

    return browser

if __name__ == '__main__':
    browser = make_chrome_browser('--headless') # chamando minha funcao - para exercutar o browser
    browser.get('http://www.google.com.br/') # para abrir o navegador automaticamente
    sleep(10) # fazer o site dormir por alguns segundos
    browser.quit() # para fechar o navegador