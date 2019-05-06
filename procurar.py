from urllib.parse import quote

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import traceback
import re

driver = webdriver.Firefox()


def ler_url(url):
    driver.get(url)

    xpath_q = '//div[@data-cel-widget="search_result_1"]'
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_q))
    )
    #print(element.get_attribute('innerHTML'))
    return element.text

def procurar(texto):
    url = "https://www.amazon.com.br/s?k={}"
    return url.format(quote(texto))



def chutar_preco1(texto):
    return re.findall('R\$\d+\,\d+', texto.split('Capa comum')[1])[0]



u = procurar("LOPES, Maura Corcini. Surdez & educação. Autêntica, 2017.")
print(u)

try:
    html = ler_url(u)
    print(chutar_preco1(html))
except:
    traceback.print_exc()
finally:
    driver.close()


