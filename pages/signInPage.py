from locators.page_elements import *
from utils import environment as env


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class SignInPage(BasePage):
    def title_is_visible(self):
        sign_in_title = self.driver.find_element(*SignInPageLocators.TITLE)
        assert sign_in_title.is_displayed()

    def continue_as_returning_customer(self):
        email_input = self.driver.find_element(*SignInPageLocators.USN)
        email_input.send_keys(env.cust_email)

        pwd_input = self.driver.find_element(*SignInPageLocators.PWD)
        pwd_input.send_keys(env.cust_pwd)

        sign_in_cta = self.driver.find_element(*SignInPageLocators.CTA)
        sign_in_cta.click()

    def continue_as_new_customer(self):
        guest_cta = self.driver.find_element(*SignInPageLocators.CONTINUE_CTA)
        guest_cta.click()
