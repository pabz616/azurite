import moment
from locators.page_elements import *
from utils import environment as env


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class SuccessPage(BasePage):
    def order_is_successful(self):
        #
        timestamp = moment.now().strftime("%d-%m-%y_%H-%M-%S")
        file_name = env.whoami()
        file_type = '.png'
        screenshot = file_name + timestamp + file_type
        self.driver.get_screenshot_as_file("../screenshots_" + screenshot)
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