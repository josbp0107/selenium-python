import unittest
from selenium import webdriver


class CompareProducts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window()  # Maximiza la ventana para evitar cualquier responsive desing de la pagina web
        driver.implicitly_wait(15)

    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

        driver.find_element_by_class_name('link-compare').click()
        driver.find_element_by_link_text('Clear All').click()

        # Haga un cambio de focus hacia la Alert
        alert = driver.switch_to_alert()

        # Obtiene el texto que contiene la alerta
        alert_text = alert.text

        # verificar si es el texto que queremos
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

        # Simular un click en el boton aceptar
        alert.accept()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)