from locators.page_elements import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class AccountSuccessPage(BasePage):
    def proceed_to_next_step(self):
        success_title = self.driver.find_element(*AccountSuccessLocators.TITLE)
        continue_button = self.driver.find_element(*AccountSuccessLocators.CTA)

        assert success_title.is_displayed()
        continue_button.click()