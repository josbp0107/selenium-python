import csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver


def get_data(file_name):
    rows = [] # Numero de filas que contiene el archivo
    data_file = open(file_name, 'r')  # indica que se va abrir el archivo de csv en modo lectura
    reader = csv.reader(data_file)  # Se va a encargar de leer este archivo
    next(reader, None)  # Pasa a la siguiente fila del archivo

    for row in reader:
        rows.append(row)
    return rows


@ddt
class SearchCsvDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com")

    # En este caso se va a pasar los datos que contiene el archivo csv, donde va a tomar todos los valores y realizara la respectiva
    # Busqueda
    @data(*get_data('testdata_ddt.csv'))
    @unpack
    def test_search_csv_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()  # Como buena practicas es importante siempre borrar los textfields
        search_field.send_keys(search_value)  # Simularemos la entrada de teclado donde se llamará search_value
        search_field.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')

        expected_count = int(expected_count)  # se convierte a Int para que no haya inconvenientes

        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element_by_class_name('note-msg')
            self.assertEqual('Your search returns no results.', message)
        print(f'Found {len(products)}, products')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)