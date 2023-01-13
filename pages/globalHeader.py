from locators.page_elements import *
from extensions.commands import Commands as confirm


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class GlobalHeader(BasePage):
    def check_all_ui(self):
        global_header_logo = self.driver.find_element(*GlobalHeaderLocators.LOGO)
        cart_button = self.driver.find_element(*GlobalHeaderLocators.CTA1)
        checkout_button = self.driver.find_element(*GlobalHeaderLocators.CTA2)
        my_account_button = self.driver.find_element(*GlobalHeaderLocators.CTA3)

        confirm.is_visible(global_header_logo)
        confirm.is_visible(cart_button)
        confirm.is_visible(checkout_button)
        confirm.is_visible(my_account_button)

        confirm.is_clickable(global_header_logo)
        confirm.is_clickable(cart_button)
        confirm.is_clickable(checkout_button)
        confirm.is_clickable(my_account_button)

    def view_cart_contents(self):
        cart_button = self.driver.find_element(*GlobalHeaderLocators.CTA1)
        cart_button.click()

    def navigate_to_checkout(self):
        checkout_button = self.driver.find_element(*GlobalHeaderLocators.CTA2)
        checkout_button.click()

    def navigate_to_my_account(self):
        my_account_button = self.driver.find_element(*GlobalHeaderLocators.CTA3)
        my_account_button.click()

    def logout(self):
        logoff_button = self.driver.find_element(*GlobalHeaderLocators.CTA4)
        logoff_button.click()
