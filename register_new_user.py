import unittest
from selenium import webdriver


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()

        driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span').click()
        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        password = driver.find_element_by_id('password')
        confirmation = driver.find_element_by_id('confirmation')
        is_subscribed = driver.find_element_by_id('is_subscribed')
        submit_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button/span/span')

        # Se valida si los campos se encuentran habilitados
        self.assertTrue(first_name.is_enabled()
                        and middle_name.is_enabled()
                        and last_name.is_enabled()
                        and email_address.is_enabled()
                        and password.is_enabled()
                        and confirmation.is_enabled()
                        and is_subscribed.is_enabled()
                        and submit_button.is_enabled())

        # Se procede a rellenar los campos de registros en la plataforma con el metodo de send_keys
        first_name.send_keys("Test")
        middle_name.send_keys("Test")
        last_name.send_keys("Test")
        email_address.send_keys("Test@mitest.com")
        password.send_keys("Test")
        confirmation.send_keys("Test")
        submit_button.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

