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
from Pages.ResultPage import ResultPage
from Templates.StaticMethods import StaticMethods

# Example Test Case with one test for validations of home page search engine.
class TestSearchResult(TestTemplate):

    flag = True

    # Here you can insert the query you would like to use for searching.
    # "cokolwiek" can be used as example for unrecognized query exception.
    query = "Hotel Bania Thermal & Ski"

    def test01_query_validation(self):
        print("Test has started")
        home_page = HomePage(self.driver)
        query = TestSearchResult.query
        home_page.set_place_to_search(query)
        # Here you can insert check in and check out date in format "yyyy-mm-dd".
        home_page.set_check_in_check_out_date("2019-09-12", "2019-09-14")
        home_page.search()
        msg = "Empty query"
        msg_2 = "Search result could not be confirmed - query not recognized by search engine"
        msg_3 = "Data range exceeds 30 days"
        with self.subTest("Checking for empty query"):
            self.assertTrue(home_page.check_for_empty_query(), msg)
        with self.subTest("Checking for invalid query"):
            self.assertTrue(home_page.check_for_invalid_query(), msg_2)
        with self.subTest("Checking for invalid data range"):
            self.assertTrue(home_page.check_for_invalid_date_range(), msg_3)
        for method, error in self._outcome.errors:
            if error:
                TestSearchResult.flag = False

    def test02_search_result_validation(self):
        if TestSearchResult.flag == False:
            self.skipTest("Result page is not loaded")
        search_page = ResultPage(self.driver)
        query = TestSearchResult.query
        msg_1 = "Wrong search result"
        with self.subTest("Checking if actual place is equal to expected"):
            self.assertTrue(search_page.check_result_place_or_destination(query), msg_1)
        # Here is the place to insert expected check in and out date from result page as they are in different format than before:
        # "day of the week dd month yyyy" (you have to use same language as page is displayed).
        with self.subTest("Checking if actual check in date is equal to expected"):
            self.assertTrue(search_page.validate_check_in_date("czwartek 12 Wrzesień 2019"))
        with self.subTest("Checking if actual check out date is equal to expected"):
            self.assertTrue(search_page.validate_check_out_date("sobota 14 Wrzesień 2019"))

# With this line Test Case can be executed from command line and report will be created.
if __name__ == '__main__':
    folder = StaticMethods.report_folder()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=folder), verbosity=2)