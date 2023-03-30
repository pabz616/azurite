from locators.page_elements import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class DVDMoviesCatalogPage(BasePage):
    def checkUI(self):
        # TODO Future work!
        pass

    def clickBuyNow(self):
        buyNow = self.driver.find_element(*HardwareCatalogLocators.CTA)
        buyNow.click()

    def selectActionMovies(self):
        actionMovies = self.driver.find_element(*DVDMoviesCatalogLocators.o_action)
        actionMovies.click()

    def selectCartoons(self):
        cartoonMovies = self.driver.find_element(*DVDMoviesCatalogLocators.o_cartoons)
        cartoonMovies.click()

    def selectComedy(self):
        comedyMovies = self.driver.find_element(*DVDMoviesCatalogLocators.o_comedy)
        comedyMovies.click()

    def selectDrama(self):
        dramaMovies = self.driver.find_element(*DVDMoviesCatalogLocators.o_drama)
        dramaMovies.click()

    def selectThriller(self):
        thrillerMovies = self.driver.find_element(*DVDMoviesCatalogLocators.o_thriller)
        thrillerMovies.click()

    def selectMonthlyFeaturedProduct(self):
        prd_img = self.driver.find_element(*DVDMoviesCatalogLocators.IMG)
        prd_name = self.driver.find_element(*DVDMoviesCatalogLocators.NAME)
        prd_price = self.driver.find_element(*DVDMoviesCatalogLocators.PRICE)

        # CHECK PRODUCT UI
        assert prd_img.is_displayed()
        assert prd_name.is_displayed()
        assert prd_price.is_displayed()

        # SELECT PRODUCT
        prd_name.click()