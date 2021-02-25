import unittest
from selenium import webdriver
# Sirve como excepción para los assertions cuando queremos
# validar la presencia de un elemento
from selenium.common.exceptions import NoSuchElementException
# By nos ayudará a llamar a las excepciones que queremos validar
from selenium.webdriver.common.by import By


class AssertionTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_search_field(self):
        self.assertTrue(self.is_elements_present(By.NAME, 'q'))

    def test_language_option(self):
        self.assertTrue(self.is_elements_present(By.ID, 'select-language'))

    def tearDown(self):
        self.driver.quit()

    """
        el metodo is_element_present nos va a permitir encontrar los elementos.
        Va a ser una funcion de utilidad para identificar cuando un elemento está presente de acuerdo a sus parametros
    """

    # how -> Nos va a identificar el tipo de selector
    # what -> Nos va identificar el valor que tiene el selector
    def is_elements_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)  # Busca los elementos según el parámetro
        except NoSuchElementException as variable:
            return False
        return True

# if __name__ == '__main__':
#     unittest.main(verbosity=2)
