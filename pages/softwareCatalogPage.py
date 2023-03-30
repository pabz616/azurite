from locators.page_elements import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class SoftwareCatalogPage(BasePage):
    def checkUI(self):
        # TODO Future work!
        pass

    def clickBuyNow(self):
        buyNow = self.driver.find_element(*SoftwareCatalogLocators.CTA)
        buyNow.click()

    def selectAction(self):
        action = self.driver.find_element(*SoftwareCatalogLocators.o_action)
        action.click()

        buyNow = self.driver.find_element(*SoftwareCatalogLocators.CTA)
        buyNow.click()

    def selectSimulation(self):
        simulation = self.driver.find_element(*SoftwareCatalogLocators.o_simulation)
        simulation.click()

    def selectStrategy(self):
        strategy = self.driver.find_element(*SoftwareCatalogLocators.o_strategy)
        strategy.click()

    def selectMonthlyFeaturedProduct(self):
        prd_img = self.driver.find_element(*SoftwareCatalogLocators.IMG)
        prd_name = self.driver.find_element(*SoftwareCatalogLocators.NAME)
        prd_price = self.driver.find_element(*SoftwareCatalogLocators.PRICE)

        # CHECK PRODUCT UI
        assert prd_img.is_displayed()
        assert prd_name.is_displayed()
        assert prd_price.is_displayed()

        # SELECT PRODUCT
        prd_name.click()
