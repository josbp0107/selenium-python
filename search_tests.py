import unittest
from selenium import webdriver


class SearchTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window()  # Maximiza la ventana para evitar cualquier responsive desing de la pagina web
        driver.implicitly_wait(15)  # Unidad en segundos

    def test_search_tee(self):
        driver = self.driver  # evitar escribir repetidamente el parametro self
        search_field = driver.find_element_by_name('q')
        search_field.clear()  # Limpia el campo de busqueda, en el caso de que haya algun texto en el textfield

        search_field.send_keys('tee')  # Simula un teclado, el cual escribira "tee" en el textfield
        search_field.submit()  # Envía lo escrito

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')

        search_field.send_keys('salt shake')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1, len(products))

    # Close browser
    def tearDown(self) -> None:
        self.driver.quit()


# if __name__ == '__main__':
#     """
#         verbosity=2 -> muestra el resultado de test, es decir, muestra si hubo un error o si funciono perfectamente.
#         testRunner -> Se crea con un formato HTML el resultado de la ejecucion
#                     output -> como se llamará la carpeta
#                     report_name -> El nombre que llevará el reporte
#     """
#     unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='report-Home-Page'))
