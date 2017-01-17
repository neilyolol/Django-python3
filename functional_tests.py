from selenium import webdriver
import unittest

class NewVistorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get('http://localhost:8000')

if __name__ == '__main__':
    unittest.main(warnings='ignore')


