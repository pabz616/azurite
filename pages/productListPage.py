import pytest

from locators.page_elements import *
from assertpy import assert_that
from extensions.commands import Commands as verify


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class ProductListPage(BasePage):
    @pytest.fixture
    def select_available_product(self):
        results = self.driver.find_elements(*PLPLocators.PROD_DATA)

        category_title = self.driver.find_element(*PLPLocators.PLP_TITLE)
        item_image = self.driver.find_element(*PLPLocators.PROD_IMG)
        item_name = self.driver.find_element(*PLPLocators.PROD_NAME)
        item_price = self.driver.find_element(*PLPLocators.PROD_PRICE)
        buyNow_CTA = self.driver.find_element(*PLPLocators.CTA)
        no_items_msg = 'There are no products available in this category.'

        assert category_title.is_displayed()
        assert_that(item_image).is_not_none()
        assert_that(item_name).is_not_none()
        assert_that(item_price).is_not_none()
        buyNow_CTA.click()