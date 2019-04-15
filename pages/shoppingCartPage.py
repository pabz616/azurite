import moment
from locators.page_elements import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class ShoppingCartPage(BasePage):
    def check_all_ui(self):
        #
        timestamp = moment.now().strftime("%m-%d-%y_%H-%M-%S")
        file_loc = '../screenshots/'
        file_name = 'ShoppingCartPage'
        file_type = '.png'
        screenshot = file_loc + file_name + '_' + timestamp + file_type

        self.driver.save_screenshot(screenshot)
        #
        cart_page_title = self.driver.find_element(*MyCartPageLocators.CART_TITLE)
        assert cart_page_title.is_displayed()

        cart_prod_title = self.driver.find_element(*MyCartPageLocators.CART_SUBTITLE)
        assert cart_prod_title.is_displayed()

        cart_item_image = self.driver.find_element(*MyCartPageLocators.PROD_IMG)
        assert cart_item_image.is_displayed()

    def click_checkout(self):
        checkout_cta = self.driver.find_element(*MyCartPageLocators.CTA)
        checkout_cta.click()