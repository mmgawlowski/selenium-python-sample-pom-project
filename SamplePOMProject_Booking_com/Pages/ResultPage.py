from selenium.common.exceptions import NoSuchElementException
from Templates.BasePage import BasePage


class ResultPage(BasePage):

    search_destination_result_xpath = "//div[@role='heading']/h1"
    search_result_xpath = "//span[contains(text(), '%s')]"
    search_result_check_in_date_xpath = "//div[text()='%s']"
    search_result_check_out_date_xpath = "//div[text()='%s']"
    '''
    $s is not a part of the selector. It is Python's operator used for inserting additional elements to the string
    E.g. self.driver.find_element_by_xpath(ResultPage.check_in_date_xpath % check_in) will be translated to:
    self.driver.find_element_by_xpath("//td[@data-date='%s']" % 2019-09-12) and finally to:
    self.driver.find_element_by_xpath("//td[@data-date='2019-09-12']")
    '''

    # Method checks if chosen destination e.g. city or place e.g. hotel is displayed on result page.
    # It returns True or False to assertion from Test Case.
    def check_result_place_or_destination(self, query):
        result = self.driver.find_element_by_xpath(ResultPage.search_destination_result_xpath)
        if query in result.text:
            return True
        else:
            try:
                self.driver.find_element_by_xpath(ResultPage.search_result_xpath % query).is_displayed
            except NoSuchElementException:
                return False
        result = self.driver.find_element_by_xpath(ResultPage.search_result_xpath % query)
        if query in result.text:
            return True
        return False

    # Method for checking if check in date displayed on result page is same with expected.
    # It returns is_displayed statement to assertion from Test Case.
    def validate_check_in_date(self, check_in):
        return self.driver.find_element_by_xpath(ResultPage.search_result_check_in_date_xpath % check_in).is_displayed

    # Same as above for check out date.
    def validate_check_out_date(self, check_out):
        return self.driver.find_element_by_xpath(ResultPage.search_result_check_out_date_xpath % check_out).is_displayed
