import unittest
from selenium import webdriver

"""
    Esta clase se encarga de realizar un scraping a una tabla y guardarlas en una variable donde se encuentra su cabezara y sus filas
"""


class DataTables(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Sortable Data Tables').click()

    def test_data_tables(self):
        driver = self.driver
        table = [[] for i in range(5)]

        for i in range(4):
            for j in range(3):
                head_table = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{j + 1}]/span').text
                row_table = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{i + 1}]/td[{j + 1}]').text
                table[i].append({head_table: row_table})
        print(table)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)