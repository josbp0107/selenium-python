import unittest
# Nos permitirá utilizar DDT con datos que vamos a designar y desempacquetarlos de las tuplas de donde estarán
from ddt import ddt, data, unpack
from selenium import webdriver

"""
DDT Es una metodología utilizada en el testing de software (Se puede usar con selenium) y 
esto va ayudar que las automatizaciones sean mucho mas robustas y versátiles.
"""

# Siempre agregar el decorador DDT justamente antes de donde se encuentra nuestra clase de prueba
@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com")

    #  @data Va a incluir tuplas con los terminos que vamos a buscar
    #  dress -> lo que se va a bucar
    #  6 -> la cantidad de elementos que se esperamos como resultados
    @data(('dress', 6), ('music', 5))
    # @unpack -> para desempaquetar estas tuplas y puedan ser consultadas individualmente
    @unpack
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()  # Como buena practicas es importante siempre borrar los textfields
        search_field.send_keys(search_value)  # Simularemos la entrada de teclado donde se llamará search_value
        search_field.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')

        for product in products:
            print(product.text)

        self.assertEqual(expected_count, len(products))

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
