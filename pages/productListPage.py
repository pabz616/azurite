from locators.page_elements import *
from assertpy import assert_that


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class ProductListPage(BasePage):
    def select_available_product(self):
        results = self.driver.find_element(*PLPLocators.PROD_DATA)

        category_title = self.driver.find_element(*PLPLocators.PLP_TITLE)
        item_image = self.driver.find_element(*PLPLocators.PROD_IMG)
        item_name = self.driver.find_element(*PLPLocators.PROD_NAME)
        item_price = self.driver.find_element(*PLPLocators.PROD_PRICE)
        buyNow_CTA = self.driver.find_element(*PLPLocators.CTA)
        item_not_available = self.driver.find_element(*PLPLocators.NO_ITEM_MSG)
        assert category_title.is_displayed()

        if item_not_available is not None:
            assert_that(item_image).is_in(results)
            assert_that(item_name).is_in(results)
            assert_that(item_price).is_in(results)
            buyNow_CTA.click()
        else:
            pass
            print("There are no products available in this category.")