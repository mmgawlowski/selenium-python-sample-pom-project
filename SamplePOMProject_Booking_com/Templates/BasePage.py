# basic page template to avoid adding __init__ function everywhere
class BasePage(object):

    def __init__(self, driver):
        self.driver = driver