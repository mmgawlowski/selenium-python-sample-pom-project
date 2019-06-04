# This class contains locators of all web elements used for testing
class Locators():

    # HomePage locators

    searchbox_id = "ss"
    calendar_button_class_name = "calendar-restructure-sb"
    calendar_button_next_xpath = "//div[@data-bui-ref='calendar-next']"
    check_in_date_xpath = "//td[@data-date='%s']"
    check_out_date_xpath = "//td[@data-date='%s']"
    search_button_xpath = "//span[text()='Szukaj']"
    invalid_query_alert_class_name = "sb-searchbox__error"
    invalid_date_range_alert_xpath = "//div[@data-component='search/dates/dates-errors']/div"
    empty_query_alert_xpath = "//div[@class='fe_banner fe_banner__accessible fe_banner__red -visible'][@id='destination__error']"

    # ResultPage locators

    search_destination_result_xpath = "//div[@role='heading']/h1"
    search_result_xpath = "//span[contains(text(), '%s')]"
    search_result_check_in_date_xpath = "//div[text()='%s']"
    search_result_check_out_date_xpath = "//div[text()='%s']"

    # $s is not a part of the selector. It is Python's operator used for inserting additional elements to the string
    # E.g. self.driver.find_element_by_xpath(Locators.check_in_date_xpath % check_in) will be translated to:
    # self.driver.find_element_by_xpath("//td[@data-date='%s']" % 2019-09-12) and finally to:
    # self.driver.find_element_by_xpath("//td[@data-date='2019-09-12']")