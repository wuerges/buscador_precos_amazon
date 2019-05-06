from urllib.parse import quote

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import traceback
import re


class Crawler:
    def __init__(self):
        self.driver = webdriver.Firefox()


    def ler_url(self, url):
        self.driver.get(url)

        xpath_q = '//div[@data-cel-widget="search_result_1"]'
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_q))
        )
        #print(element.get_attribute('innerHTML'))
        return element.text

    def cria_url(self, texto):
        url = "https://www.amazon.com.br/s?k={}"
        return url.format(quote(texto))



    def chutar_preco1(self, texto):
        return re.findall('R\$\d+\,\d+', texto.split('Capa comum')[1])[0]


    def procura(self, texto):
        u = self.cria_url(texto)
        preco = "R$0,00"
        try:
            html = self.ler_url(u)
            preco = self.chutar_preco1(html)
        except:
            traceback.print_exc()
        return preco

    def __del__(self):
        self.driver.close()

c = Crawler()
u = c.procura("LOPES, Maura Corcini. Surdez & educação. Autêntica, 2017.")
print(u)
