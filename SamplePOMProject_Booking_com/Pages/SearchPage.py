from selenium.common.exceptions import NoSuchElementException
from Templates.BasePage import BasePage
from Locators.Locators import Locators

class SearchPage(BasePage):

    # Method checks whether warning related to empty query is displayed or not.
    def check_for_empty_query(self):
        try:
            self.driver.find_element_by_xpath(Locators.empty_query_alert_xpath).is_displayed()
        except NoSuchElementException:
            print("Query not empty")
            return True
        else:
            return False

    # Method checks whether warning related to unrecognized query is displayed or not.
    def check_for_invalid_query(self):
        try:
            self.driver.find_element_by_class_name(Locators.invalid_query_alert_class_name).is_displayed()
        except NoSuchElementException:
            print("Query ok")
            return True
        else:
            return False

    # Method checks whether warning related to date range exceeding 30 days is displayed or not.
    def check_for_invalid_date_range(self):
        try:
            self.driver.find_element_by_xpath(Locators.invalid_date_range_alert_xpath).is_displayed()
        except NoSuchElementException:
            print("Date range ok")
            return True
        else:
            return False

    # Method checks if chosen destination e.g. city or place e.g. hotel is displayed on result page.
    # It returns True or False to assertion from Test Case.
    def check_result_place_or_destination(self, query):
        result = self.driver.find_element_by_xpath(Locators.search_destination_result_xpath)
        if query in result.text:
            return True
        else:
            try:
                self.driver.find_element_by_xpath(Locators.search_result_xpath % query).is_displayed
            except NoSuchElementException:
                return False
        result = self.driver.find_element_by_xpath(Locators.search_result_xpath % query)
        if query in result.text:
            return True
        return False

    # Method for checking if check in date displayed on result page is same with expected.
    # It returns is_displayed statement to assertion from Test Case.
    def validate_check_in_date(self, check_in):
        return self.driver.find_element_by_xpath(Locators.search_result_check_in_date_xpath % check_in).is_displayed

    # Same as above for check out date.
    def validate_check_out_date(self, check_out):
        return self.driver.find_element_by_xpath(Locators.search_result_check_out_date_xpath % check_out).is_displayed