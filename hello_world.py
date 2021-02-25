# Con unittest nos podemos traer todas nuestras pruebas
import unittest
"""Ayuda a orquestar cada una de las pruebas que estaremos
ejecutando junto con los reportes"""
from pyunitreport import HTMLTestRunner
# Para comunicarnos con el navegador usamos webdriver
from selenium import webdriver


class HelloWorld(unittest.TestCase):

    # @classmethod -> Decorador para que las distintas paginas corran en una sola pestaña
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')  # esperamos 10 seg antes de realizar la siguiente accion
        driver = cls.driver
        driver.implicitly_wait(10)

    # Caso de prueba donde realizaremos una serie de acciones para que el navegador las automatice
    def test_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org')

    # Cerramos el navegador una vez terminadas las pruebas
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='report-wikipedia'))


