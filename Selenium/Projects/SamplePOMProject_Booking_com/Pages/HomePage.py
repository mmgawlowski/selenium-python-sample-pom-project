from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Projects.SamplePOMProject_Booking_com.Templates.BasePage import BasePage
from Projects.SamplePOMProject_Booking_com.Locators.Locators import Locators


class HomePage(BasePage):

    # This method checks if search field on home page is present and then put there text from given query imitating input from keyboard
    def set_place_to_search(self, query: str):
        wait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, Locators.searchbox_id)))
        self.driver.find_element_by_id(Locators.searchbox_id).send_keys(query)

    # This method uses calendar to select chosen check in and out date imitating user's mouse left click.
    # It checks if chosen date is visible, if not it clicks "next" - arrow button until it is then clicks on date.
    def set_check_in_check_out_date(self, check_in, check_out):
        self.driver.find_element_by_class_name(Locators.calendar_button_class_name).click()
        while True:
            try:
                self.driver.find_element_by_xpath(Locators.check_in_date_xpath % check_in).is_displayed()
            except NoSuchElementException:
                self.driver.find_element_by_xpath(Locators.calendar_button_next_xpath).click()
            else:
                break
        self.driver.find_element_by_xpath(Locators.check_in_date_xpath % check_in).click()
        while True:
            try:
                self.driver.find_element_by_xpath(Locators.check_out_date_xpath % check_out).is_displayed()
            except NoSuchElementException:
                self.driver.find_element_by_xpath(Locators.calendar_button_next_xpath).click()
            else:
                break
        self.driver.find_element_by_xpath(Locators.check_out_date_xpath % check_out).click()

    # Method which finds and clicks on search button
    def search(self):
        self.driver.find_element_by_xpath(Locators.search_button_xpath).click()

    # Method for checking if home page is loaded and its title contains phrase "Booking.com"
    # It returns True or False to assertion from Test Case
    def check_home_page_loaded(self):
        try:
            wait(self.driver, 10).until(
            EC.title_contains('Booking.com'))
        except TimeoutException:
            return False
        else:
            return True

    # Method for checking if search field is present and enabled.
    # It returns is_enabled() statement to assertion from Test Case or raises exception
    def check_searchbox(self):
        wait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, Locators.searchbox_id)))
        return self.driver.find_element_by_id(Locators.searchbox_id).is_enabled()

    # Method for checking if calendar is enabled.
    # It returns is_enabled() statement to assertion from Test Case or raises exception
    def check_calendar(self):
        return self.driver.find_element_by_class_name(Locators.calendar_button_class_name).is_enabled()

    # Method for checking if search button is and enabled.
    # It returns is_enabled() statement to assertion from Test Case or raises exception
    def check_search_button(self):
        return self.driver.find_element_by_xpath(Locators.search_button_xpath).is_enabled()
