from locators.page_elements import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class GadgetsCatalogPage(BasePage):
    def checkUI(self):
        # TODO Future work!
        pass

    def selectAvailableGadget(self):
        prd_img = self.driver.find_element(*GadgetsCatalogLocators.IMG)
        prd_name = self.driver.find_element(*GadgetsCatalogLocators.NAME)
        prd_price = self.driver.find_element(*GadgetsCatalogLocators.PRICE)
        buyNow = self.driver.find_element(*GadgetsCatalogLocators.CTA)

        # CHECK PRODUCT UI
        assert prd_img.is_displayed()
        assert prd_name.is_displayed()
        assert prd_price.is_displayed()
        buyNow.click()