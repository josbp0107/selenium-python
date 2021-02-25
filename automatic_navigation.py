import unittest
from selenium import webdriver
from time import sleep  #  Este modulo ayuda a agregar un tiempo para realizar la siguiente operacion o accion, pero no es recomendable
                        #  Ya que esto puede perjudicar el tiempo de ejecucion del script


class AutomaticNavigation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()  # Maximiza la ventana para evitar cualquier responsive desing de la pagina web
        driver.get("https://www.google.com")

    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('python')
        search_field.submit()

        driver.back()  # Retroceder en el navegador
        sleep(3)  # Espera por 3 segundos
        driver.forward()  # avanza a la pagina de resultados
        driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[9]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/a/h3/span').click()
        driver.refresh()  # Refrescar la pagina

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)