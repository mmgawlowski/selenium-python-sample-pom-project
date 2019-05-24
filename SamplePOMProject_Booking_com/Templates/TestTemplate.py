import unittest
import os
import sys
from selenium import webdriver
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from Templates.StaticMethods import StaticMethods

# This class contains code shared in all Test Cases.
# It helps to avoid duplication of the code.
class TestTemplate(unittest.TestCase):

    # Prerequisites for Test Cases. They are setup once for all test from given Test Case.
    # If changed to setUp(self) they will be executed with instance of every test.
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        print("Run started")
        cls.driver.maximize_window()
        cls.driver.get("https://www.booking.com/index.pl.html")

    # In two next methods I used addCleanup for making screenshot everytime test is interrupted by exception or assertion error.
    def setUp(self):
        self.addCleanup(self.screen_shot)


    def screen_shot(self):
        # This line allows addition of test name to the name of screenshot file.
        # I would use self.id() to get also Test Case name but it does't work when Test Case is loaded in Test Suite from different file...
        test_method_name = self._testMethodName
        for method, error in self._outcome.errors:
            if error:
                StaticMethods.save_screenshot_picture(self.driver, test_method_name)

    # Actions to be done after all tests from Test Case are executed.
    # Closing browser in this case.
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
