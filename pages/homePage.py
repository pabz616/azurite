from locators.page_elements import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    def is_title_matches(self):
        return "Welcome to 5ElementsLearning" in self.driver.title

    def select_product(self):
        prod1 = self.driver.find_element(*HomePageLocators.PROD1)
        prod1.click()