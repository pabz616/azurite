import moment
from locators.page_elements import *
from utils import environment as env

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class SignInPage(BasePage):
    def title_is_visible(self):
        #
        timestamp = moment.now().strftime("%m-%d-%y_%H-%M-%S")
        file_loc = '../screenshots/'
        file_name = 'SignInPage'
        file_type = '.png'
        screenshot = file_loc + file_name + '_' + timestamp + file_type
        self.driver.get_screenshot_as_file(screenshot)
        #
        sign_in_title = self.driver.find_element(*SignInPageLocators.TITLE)
        assert sign_in_title.is_displayed()

    def continue_as_returning_customer(self):
        email_input = self.driver.find_element(*SignInPageLocators.USN)
        email_input.send_keys(env.cust_email)

        pwd_input = self.driver.find_element(*SignInPageLocators.PWD)
        pwd_input.send_keys(env.cust_pwd)

        sign_in_cta = self.driver.find_element(*SignInPageLocators.CTA)
        sign_in_cta.click()