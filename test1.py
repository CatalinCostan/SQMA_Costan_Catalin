import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestOne(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.pro-s.ro")  

    def test_title(self):
        """Verify the title of the page."""
        self.assertEqual(self.driver.title, "ProSoft S.R.L. Valcea Network&Security")

    def test_element(self):
        """Verify an element is present on the page."""
        element = self.driver.find_element(By.CSS_SELECTOR, "h3")
        self.assertEqual(element.text, "SUDURA F.O.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
