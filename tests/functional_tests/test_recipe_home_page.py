from django.test import LiveServerTestCase # importando teste do servidor ativo - aparecer coisas na tela - executar o site sem css
from django.contrib.staticfiles.testing import StaticLiveServerTestCase # exercutar servido ativo - com css
from utils.browser import make_chrome_browser # importando nossa configuracao do selenium
import time
from selenium.webdriver.common.by import By # para pegamos dados HTML

class RecipeHomePageFunctionalTest(StaticLiveServerTestCase):
    # parar o site por um determinado tempo
    def sleep(self, seconds=5):
        time.sleep(seconds)

    # nosso teste
    def test_the_test(self): 
        browser = make_chrome_browser() # criando nosso webdriver - sempre pegamos um browser
        browser.get(self.live_server_url) # pegando a url do nosso webdriver sem saber qual e
        self.sleep(6) # pausa o site por um determinado tempo
        body = browser.find_element(By.TAG_NAME, 'body') # para encontrar um elemento HTML com determinada classe, id, tag, texto, etc.
        self.assertIn('No recipes found here 🥲', body.text) # verificar se o texto esta no meu site
        browser.quit() # parar fechar o nosso webdriver - sempre fechamos um browser
