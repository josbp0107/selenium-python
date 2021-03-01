import unittest
from selenium import webdriver
from google_page import GooglePage

"""
    Este archivo llamará cada uno de los metodos que se realizaron en el archivo de google_page.py
    
"""


class GoogleTest(unittest.TestCase):

    @classmethod  #  @classmethod Corre en una sola instancia del navegador
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Python')

        self.assertEqual('Python', google.keyword)
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)