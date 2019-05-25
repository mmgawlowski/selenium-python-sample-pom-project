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
from Pages.SearchPage import SearchPage
from Templates.StaticMethods import StaticMethods

# Example Test Case with one test for validations of home page search engine.
class TestSearchResult(TestTemplate):

    def test_search_for_place_by_query(self):
        print("Test has started")
        home_page = HomePage(self.driver)
        search_page = SearchPage(self.driver)
        # Here you can insert the query you would like to use for searching.
        # "cokolwiek" can be used as example for unrecognized query exception.
        query = "Hotel Bania Thermal & Ski"
        home_page.set_place_to_search(query)
        # Here you can insert check in and check out date in format "yyyy-mm-dd".
        home_page.set_check_in_check_out_date("2019-09-12", "2019-10-14")
        home_page.search()
        msg = "Empty query"
        msg_2 = "Search result could not be confirmed - query not recognized by search engine"
        msg_3 = "Data range exceeds 30 days"
        msg_4 = "Wrong search result"
        self.assertTrue(search_page.check_for_empty_query(), msg)
        self.assertTrue(search_page.check_for_invalid_query(), msg_2)
        self.assertTrue(search_page.check_for_invalid_date_range(), msg_3)
        self.assertTrue(search_page.check_result_place_or_destination(query), msg_4)
        # Here is the place to insert expected check in and out date from result page as they are in different format than before:
        # "day of the week dd month yyyy" (you have to use same language as page is displayed).
        self.assertTrue(search_page.validate_check_in_date("czwartek 12 Wrzesień 2019"))
        self.assertTrue(search_page.validate_check_out_date("sobota 14 Wrzesień 2019"))
        print("Result ok")

# With this line Test Case can be executed from command line and report will be created.
if __name__ == '__main__':
    folder = StaticMethods.report_folder()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=folder), verbosity=2)