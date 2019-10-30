from locators.page_elements import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class ShippingPage(BasePage):
    def title_is_visible(self):
        shipping_page_title = self.driver.find_element(*ShippingPageLocators.TITLE)
        assert shipping_page_title.is_displayed()

    def confirm_shipping_method(self):
        shipping_method_title = self.driver.find_element(*ShippingPageLocators.SHIPPING_SUBTITLE)
        assert shipping_method_title.is_displayed()

        shipping_option = self.driver.find_element(*ShippingPageLocators.SHIPPING_OPTION)
        assert shipping_option.is_displayed()

        shipping_method = self.driver.find_element(*ShippingPageLocators.SHIPPING_METHOD)
        assert shipping_method.is_displayed()

    def confirm_shipping_address(self):
        shipping_address = self.driver.find_element(*ShippingPageLocators.SHIPPING_ADDRESS)
        shipping_address.is_displayed()

    def proceed_to_billing(self):
        continue_cta = self.driver.find_element(*ShippingPageLocators.CTA)
        continue_cta.click()