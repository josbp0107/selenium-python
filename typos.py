import unittest
from selenium import webdriver
from time import sleep


class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Typos').click()

    def test_typos(self):
        driver = self.driver
        text_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)').text
        tries = 1
        flag = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while not flag:
            sleep(2)
            if text_to_check == correct_text:
                flag = True
            else:
                tries += 1
                driver.refresh()
                text_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)').text

        print(f'It took {tries} to find the typo')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)