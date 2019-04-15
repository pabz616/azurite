import moment
from locators.page_elements import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class ProductDetailsPage(BasePage):
    def product_title_is_visible(self):
        product_title = self.driver.find_element(*PDPLocators.PDP_TITLE)
        #
        timestamp = moment.now().strftime("%m-%d-%y_%H-%M-%S")
        file_loc = '../screenshots/'
        file_name = 'ProductDetailsPage'
        file_type = '.png'
        screenshot = file_loc + file_name + '_' + timestamp + file_type

        self.driver.save_screenshot(screenshot)
        #
        assert product_title.is_displayed()

    def select_options_and_add_to_cart(self):
        # SELECTING THE MEMORY
        ddl_memory = self.driver.find_element(*PDPLocators.MEMORY_LIST)
        ddl_memory.click()

        o_8mb = self.driver.find_element(*PDPLocators.MEMORY_VALUE)
        o_8mb.click()

        # SELECTING THE MODEL
        ddl_model = self.driver.find_element(*PDPLocators.MODEL_LIST)
        ddl_model.click()

        o_premium = self.driver.find_element(*PDPLocators.MODEL_VALUE)
        o_premium.click()

        # ADD TO CART
        add_to_cart = self.driver.find_element(*PDPLocators.CTA)
        add_to_cart.click()