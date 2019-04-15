import moment
from locators.page_elements import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class PaymentInfoPage(BasePage):
    def title_is_visible(self):
        #
        timestamp = moment.now().strftime("%m-%d-%y_%H-%M-%S")
        file_loc = '../screenshots/'
        file_name = 'PaymentInfoPage'
        file_type = '.png'
        screenshot = file_loc + file_name + '_' + timestamp + file_type

        self.driver.save_screenshot(screenshot)
        #
        billing_page_title = self.driver.find_element(*PaymentInfoPageLocators.TITLE)
        assert billing_page_title.is_displayed()

    def billing_address_is_visible(self):
        billing_address = self.driver.find_element(*PaymentInfoPageLocators.BILLING_ADDR)
        assert billing_address.is_displayed()

    def select_payment_method(self):
        pymt_cod = self.driver.find_element(*PaymentInfoPageLocators.PAYMENT_METHOD_1)
        pymt_cod.click()

        continue_cta = self.driver.find_element(*PaymentInfoPageLocators.CTA)
        continue_cta.click()