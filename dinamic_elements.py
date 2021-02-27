import unittest
from selenium import webdriver


class DinamicElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Disappearing Elements').click()

    def test_name_elements(self):
        driver = self.driver

        options = []
        menu = 5
        tries = 1

        while len(options) < 5:
            options.clear() # Cada ciclo, se borrará lo que contenga la variable

            for i in range(menu):
                try:
                    options_name = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/ul/li[{i + 1}]/a')
                    options.append(options_name.text)
                    print(options)
                except:
                    print(f"Option number {i + 1} is NOT FOUND")
                    tries += 1
                    driver.refresh()
        print(f'Finishes in {tries} tries')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)


