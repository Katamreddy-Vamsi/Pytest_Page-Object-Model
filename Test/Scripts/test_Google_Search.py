import unittest
from time import sleep
from Pytest_Page_Object_Model.Src.TestBase.WebDriverSetup import WebDriverSetup
from Pytest_Page_Object_Model.Src.PageObject.Pages.HomePage import Home


class Google_Search(WebDriverSetup):
    def test_GoogleSearch(self):
        driver = self.driver
        self.driver.get("https://www.google.com/")
        self.driver.set_page_load_timeout(30)

        # Create an instance of the class so that we can make use of the methods in the class
        home = Home(driver)
        home.search_text.send_keys("Page object model")
        sleep(5)
        home.search_text.submit()
        sleep(10)


if __name__ == '__main__':
    unittest.main()
