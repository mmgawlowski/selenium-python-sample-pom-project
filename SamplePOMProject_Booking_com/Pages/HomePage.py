from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Templates.BasePage import BasePage


class HomePage(BasePage):

    searchbox_id = "ss"
    calendar_button_class_name = "calendar-restructure-sb"
    calendar_button_next_xpath = "//div[@data-bui-ref='calendar-next']"
    check_in_date_xpath = "//td[@data-date='%s']"
    check_out_date_xpath = "//td[@data-date='%s']"
    search_button_xpath = "//span[text()='Szukaj']"
    invalid_query_alert_class_name = "sb-searchbox__error"
    invalid_date_range_alert_xpath = "//div[@data-component='search/dates/dates-errors']/div"
    empty_query_alert_xpath = "//div[@class='fe_banner fe_banner__accessible fe_banner__red -visible'][@id='destination__error']"

    '''
    "%s" is not a part of the selector. It is Python's operator used for inserting additional elements to the string
    E.g. self.driver.find_element_by_xpath(ResultPage.check_in_date_xpath % check_in) will be translated to:
    self.driver.find_element_by_xpath("//td[@data-date='%s']" % 2019-09-12) and finally to:
    self.driver.find_element_by_xpath("//td[@data-date='2019-09-12']")
    '''

    # This method checks if search field on home page is present and then put there text from given query imitating input from keyboard.
    def set_place_to_search(self, query: str):
        wait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, self.searchbox_id)))
        self.driver.find_element_by_id(self.searchbox_id).send_keys(query)

    # This method uses calendar to select chosen check in and out date imitating user's mouse left click.
    # It checks if chosen date is visible, if not it clicks "next" - arrow button until it is then clicks on date.
    def set_check_in_check_out_date(self, check_in, check_out):
        self.driver.find_element_by_class_name(self.calendar_button_class_name).click()
        while True:
            try:
                self.driver.find_element_by_xpath(self.check_in_date_xpath % check_in).is_displayed()
            except NoSuchElementException:
                self.driver.find_element_by_xpath(self.calendar_button_next_xpath).click()
            else:
                break
        self.driver.find_element_by_xpath(self.check_in_date_xpath % check_in).click()
        while True:
            try:
                self.driver.find_element_by_xpath(self.check_out_date_xpath % check_out).is_displayed()
            except NoSuchElementException:
                self.driver.find_element_by_xpath(self.calendar_button_next_xpath).click()
            else:
                break
        self.driver.find_element_by_xpath(self.check_out_date_xpath % check_out).click()

    # Method which finds and clicks on search button.
    def search(self):
        self.driver.find_element_by_xpath(self.search_button_xpath).click()

    # Method for checking if home page is loaded and its title contains phrase "Booking.com".
    # It returns True or False to assertion from Test Case.
    def check_home_page_loaded(self):
        try:
            wait(self.driver, 10).until(
            EC.title_contains('Booking.com'))
        except TimeoutException:
            return False
        else:
            return True

    # Method for checking if search field is present and enabled.
    # It returns is_enabled() statement to assertion from Test Case or raises exception.
    def check_searchbox(self):
        wait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.searchbox_id)))
        return self.driver.find_element_by_id(self.searchbox_id).is_enabled()

    # Method for checking if calendar is enabled.
    # It returns is_enabled() statement to assertion from Test Case or raises exception.
    def check_calendar(self):
        return self.driver.find_element_by_class_name(self.calendar_button_class_name).is_enabled()

    # Method for checking if search button is and enabled.
    # It returns is_enabled() statement to assertion from Test Case or raises exception.
    def check_search_button(self):
        return self.driver.find_element_by_xpath(self.search_button_xpath).is_enabled()

    # Method checks whether warning related to empty query is displayed or not.
    def check_for_empty_query(self):
        try:
            self.driver.find_element_by_xpath(self.empty_query_alert_xpath).is_displayed()
        except NoSuchElementException:
            print("Query not empty")
            return True
        else:
            return False

    # Method checks whether warning related to unrecognized query is displayed or not.
    def check_for_invalid_query(self):
        try:
            self.driver.find_element_by_class_name(self.invalid_query_alert_class_name).is_displayed()
        except NoSuchElementException:
            print("Query ok")
            return True
        else:
            return False

    # Method checks whether warning related to date range exceeding 30 days is displayed or not.
    def check_for_invalid_date_range(self):
        try:
            self.driver.find_element_by_xpath(self.invalid_date_range_alert_xpath).is_displayed()
        except NoSuchElementException:
            print("Date range ok")
            return True
        else:
            return False
