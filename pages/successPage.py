from locators.page_elements import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class SuccessPage(BasePage):
    def confirm_order_is_successful_and_continue(self):
        success_page_title = self.driver.find_element(*SuccessPageLocators.TITLE)
        continue_cta = self.driver.find_element(*SuccessPageLocators.CTA)

        success_msg = 'Your order has been successfully processed!'
        shipping_msg = 'Your products will arrive at their destination within 2-5 working days.'
        thanks_msg = 'Thanks for shopping with us online!'

        '''CONFIRM ORDER'''
        assert success_page_title.is_displayed()
        assert success_msg in self.driver.page_source
        assert shipping_msg in self.driver.page_source
        assert thanks_msg in self.driver.page_source

        '''CONTINUE SHOPPING'''
        continue_cta.click()