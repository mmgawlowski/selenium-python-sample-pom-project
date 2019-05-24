from datetime import datetime
import os

# Class contains static methods which can be called as independent from classes and its methods.
class StaticMethods():

    # Method which creates folder with current date for reports and returns path to it
    @staticmethod
    def report_folder():
        date = StaticMethods.get_date()
        dir = os.path.normpath(os.path.join(os.path.dirname(__file__), os.pardir))
        folder = dir + "/Reports/Reports" + date + "/"
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    # Method for getting current date and time.
    # Format can be changed but slashes "/\" should be avoided.
    @staticmethod
    def get_date_time():
        dt_format = '%Y%m%d_%H%M%S'
        return datetime.now().strftime(dt_format)

    # Method for getting current time.
    @staticmethod
    def get_time():
        dt_format = '%H.%M.%S'
        return datetime.now().strftime(dt_format)

    # Method for getting current date.
    @staticmethod
    def get_date():
        d_format = '%Y%m%d'
        return datetime.now().strftime(d_format)

    # Method which takes screenshot and saves it to given report folder.
    @staticmethod
    def save_screenshot_picture(driver, file_name):
        date_time = StaticMethods.get_date_time()
        screenshot_folder = StaticMethods.report_folder()
        picture = screenshot_folder + file_name + ' ' + date_time + '.png'
        driver.save_screenshot(picture)
