import moment
from locators.page_elements import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class SuccessPage(BasePage):
    def order_is_successful(self):
        #
        timestamp = moment.now().strftime("%m-%d-%y_%h:%m")
        file_loc = '../screenshots/'
        file_name = 'SuccessPage'
        file_type = '.png'
        screenshot = file_loc + file_name + '_' + timestamp + file_type

        self.driver.save_screenshot(screenshot)
        #
        success_page_title = self.driver.find_element(*SuccessPageLocators.TITLE)
        assert success_page_title.is_displayed()

        success_msg = 'Your order has been successfully processed!'
        shipping_msg = 'Your products will arrive at their destination within 2-5 working days.'
        thanks_msg = 'Thanks for shopping with us online!'

        assert success_msg in self.driver.page_source
        assert shipping_msg in self.driver.page_source
        assert thanks_msg in self.driver.page_source

    def continue_shopping(self):
        continue_cta = self.driver.find_element(*SuccessPageLocators.CTA)
        continue_cta.click()