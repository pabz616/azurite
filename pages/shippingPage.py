from locators.page_elements import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class ShippingPage(BasePage):
    def proceed_to_billing(self):
        shipping_page_title = self.driver.find_element(*ShippingPageLocators.TITLE)
        shipping_method_title = self.driver.find_element(*ShippingPageLocators.SHIPPING_SUBTITLE)
        shipping_option = self.driver.find_element(*ShippingPageLocators.SHIPPING_OPTION)
        shipping_method = self.driver.find_element(*ShippingPageLocators.SHIPPING_METHOD)
        shipping_address = self.driver.find_element(*ShippingPageLocators.SHIPPING_ADDRESS)
        continue_cta = self.driver.find_element(*ShippingPageLocators.CTA)

        ''' CONFIRM SHIPPING METHOD'''
        assert shipping_page_title.is_displayed()
        assert shipping_method_title.is_displayed()
        assert shipping_option.is_displayed()
        assert shipping_method.is_displayed()

        '''CONFIRM SHIPPING ADDRESS'''
        assert shipping_address.is_displayed()

        '''PROCEED TO BILLING INFO. STEP'''
        continue_cta.click()