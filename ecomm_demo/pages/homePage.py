import moment
from locators.page_elements import *
from utils import environment as env


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    def is_title_matches(self):
        timestamp = moment.now().strftime("%d-%m-%y_%H-%M-%S")
        file_name = env.whoami()
        file_type = '.png'
        screenshot = file_name+timestamp+file_type
        self.driver.get_screenshot_as_file("../screenshots_"+screenshot)
        #
        return "Welcome to 5ElementsLearning" in self.driver.title

    def select_product(self):
        prod1 = self.driver.find_element(*HomePageLocators.PROD1)
        prod1.click()