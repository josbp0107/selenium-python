import unittest
from selenium import webdriver
# Este submodulo nos ayudará a poder utilizar los dropdown de sitios webs
from selenium.webdriver.support.ui import Select


class LanguageOptions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window()  # Maximiza la ventana para evitar cualquier responsive desing de la pagina web
        driver.implicitly_wait(15)

    def test_select_language(self):
        # Orden en que se encuentra en el sitio web
        exp_options = ['English', 'French', 'German']

        # Esta variable se va a encargar de almacenar las opciones
        active_options = []

        # Acceder a las opciones del dropdown
        select_language = Select(self.driver.find_element_by_id('select-language'))

        # para comprobar que si esté la cantidad de  opciones correcta
        self.assertEqual(3, len(select_language.options))

        # 'options' permite ingresar directamente a las opciones del dropdown
        for option in select_language.options:
            print(option.text)
            active_options.append(option.text)  # Agrega los valores a la varialbe active_options

        # verifica que la lista de opciones disponibles y activas sean indénticas
        self.assertListEqual(exp_options, active_options)

        # Verifica la palabra "English" sea la primera opción seleccionada del dropdown
        self.assertEqual('English', select_language.first_selected_option.text)

        # selecciona "German" por el texto visible
        select_language.select_by_visible_text('German')

        # verifica que el sitio cambio a Alemán y valida que la url del sitio contiene la palabra store=german
        self.assertTrue('store=german' in self.driver.current_url)
        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)

    # Close browser
    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)