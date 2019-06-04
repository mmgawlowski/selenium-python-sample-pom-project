import unittest
import HtmlTestRunner
import sys
import os

# This line returns path to the folder contains this file, then goes one folder up.
# Finally whole path is marked as additional path for searching modules.
# That's necessary to import below modules when start script from command line.
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

from Templates.TestTemplate import TestTemplate
from Pages.HomePage import HomePage
from Templates.StaticMethods import StaticMethods

# Example Test Case with two tests for checking if proper home page is loaded and its elements are available.
class TestHomePage(TestTemplate):

    flag = True

    def test01_home_page_loaded(self):
        print("Test has started")
        home_page = HomePage(self.driver)
        # Assertion if given condition is True with optional message when assertion error is raised.
        try:
            self.assertTrue(home_page.check_home_page_loaded(), 'Page could not be loaded')
            print('Home Page checked')
        except AssertionError:
            TestHomePage.flag = False
            raise

    def test02_home_page_elements_available(self):
        if TestHomePage.flag == False:
            self.skipTest("Home page is not loaded")
        home_page = HomePage(self.driver)
        with self.subTest("Checking searchbox"):
            self.assertTrue(home_page.check_searchbox())
        with self.subTest("Checking calendar"):
            self.assertTrue(home_page.check_calendar())
        with self.subTest("Checking search button"):
            self.assertTrue(home_page.check_search_button())

# With this line Test Case can be executed from command line and report will be created.
if __name__ == '__main__':
    folder = StaticMethods.report_folder()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=folder), verbosity=2)
