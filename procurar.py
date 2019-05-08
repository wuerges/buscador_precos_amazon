from urllib.parse import quote

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re

import logging
logging.basicConfig(filename='exceptions.log', level=logging.DEBUG)
import traceback


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


    def converte(self, txt):
        return float(re.sub(',', '.', txt))


    def chutar_preco1(self, texto):
        # print()
        # print()
        # print()
        # print()
        # print("texto original", texto)
        txt = re.findall('R\$(\d+\,?\d*)', texto)
        return [x for x in (self.converte(t) for t in txt) if x > 0]


    def procura(self, texto):
        u = self.cria_url(texto)
        preco = [10000]
        try:
            html = self.ler_url(u)
            preco = self.chutar_preco1(html)
        except:
            logging.debug(traceback.format_exc())
        return preco

    def __del__(self):
        self.driver.close()
