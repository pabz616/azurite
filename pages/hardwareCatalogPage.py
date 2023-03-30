from locators.page_elements import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class HardwareCatalogPage(BasePage):
    def checkUI(self):
        # TODO Future work!
        pass

    def clickBuyNow(self):
        buyNow = self.driver.find_element(*HardwareCatalogLocators.CTA)
        buyNow.click()

    def selectCDROMDrives(self):
        cdROMDrives = self.driver.find_element(*HardwareCatalogLocators.o_cdROMDrives)
        cdROMDrives.click()

    def selectGraphicsCards(self):
        graphicsCards = self.driver.find_element(*HardwareCatalogLocators.o_graphicCards)
        graphicsCards.click()

    def selectKeyboards(self):
        keyboard = self.driver.find_element(*HardwareCatalogLocators.o_keyboards)
        keyboard.click()

    def selectMemory(self):
        memory = self.driver.find_element(*HardwareCatalogLocators.o_memory)
        memory.click()

    def selectMice(self):
        mice = self.driver.find_element(*HardwareCatalogLocators.o_mice)
        mice.click()

    def selectMonitors(self):
        monitors = self.driver.find_element(*HardwareCatalogLocators.o_monitors)
        monitors.click()

    def selectPrinters(self):
        printers = self.driver.find_element(*HardwareCatalogLocators.o_printers)
        printers.click()

    def selectSpeakers(self):
        speakers = self.driver.find_element(*HardwareCatalogLocators.o_speakers)
        speakers.click()

    def selectMonthlyFeaturedProduct(self):
        prd_img = self.driver.find_element(*HardwareCatalogLocators.IMG)
        prd_name = self.driver.find_element(*HardwareCatalogLocators.NAME)
        prd_price = self.driver.find_element(*HardwareCatalogLocators.PRICE)

        # CHECK PRODUCT UI
        assert prd_img.is_displayed()
        assert prd_name.is_displayed()
        assert prd_price.is_displayed()

        # SELECT PRODUCT
        prd_name.click()