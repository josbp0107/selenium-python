import unittest
from selenium import webdriver
# Nos ayuda a hacer referencia a un elemento del sitio web atraves ed sus selectores, para identificarlo sino para
# interactuar
from selenium.webdriver.common.by import By
#  Nos permitira a hacer usos de los exspect conditions junto con las esperas explicitas
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # Esperas explicitas


class ExplicitWaitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get('http://demo-store.seleniumacademy.com')

    def test_account_link(self):
        # Esperará maximo hasta 10 segundos hasta que se cumpla nuestra condicion esperada que en este caso es
        # encontrar 'select-language' Luego se obtiene el tamaño, o elementos que tiene en total
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')

        # hace referecnai a la visibilidad al elementoq que se esta utilizando
        # LINK_TEXT -> Hace referencia al elemento
        # ACCOUNT -> El texto que se encuentra en el elemento
        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()

    def test_create_new_customer(self):
        # find_element_by_link_text -> Para enlaces
        # ACCOUNT -> El nombre que tiene el enlace
        self.driver.find_element_by_link_text('ACCOUNT').click()

        # EC -> Expected Condition ó condicion esperada
        # visibility_of_element_located -> Para Identificar un elemento que este visible
        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()

        # element_to_be_clickable -> Un elemento pueda ser clickeable
        create_account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_button.click()

        # title_contains -> Va a verificar que el sitio web en su titulo  contenga el texto Create New Customer Account
        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)