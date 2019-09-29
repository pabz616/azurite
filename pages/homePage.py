import moment
from locators.page_elements import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    def is_title_matches(self):
        timestamp = moment.now().strftime("%m-%d-%y_%H-%M-%S")
        file_loc = '../screenshots/'
        file_name = 'HomePage'
        file_type = '.png'
        screenshot = file_loc + file_name + '_' + timestamp + file_type

        self.driver.save_screenshot(screenshot)
        #
        return "Welcome to 5ElementsLearning" in self.driver.title

    def select_product(self):
        prod1 = self.driver.find_element(*HomePageLocators.PROD1)
        prod1.click()