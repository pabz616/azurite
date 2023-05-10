from locators.page_elements import *
import random
import requests
from assertpy import assert_that



class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    
    def is_page_loaded(self, url):
        r = requests.head(url)
        return r.status_code == 200
    
    """HOME PAGE"""
        
    def is_title_matches(self):
        return "Welcome to 5ElementsLearning" in self.driver.title
    
    def is_copy_text_visible(self):
        return  self.driver.find_element(*HomePageLocators.COPY).is_displayed()

    def is_section_text_visible(self):
        return self.driver.find_element(*HomePageLocators.SECTION_HEADER).is_displayed()
    
    def is_product_catalog_visible(self):
        return self.driver.find_element(*HomePageLocators.GRID).is_displayed()

    """CATEGORIES"""
    def is_categories_section_visible(self):
        return self.driver.find_element(*HomePageLocators.sCATEGORIES).is_displayed()
    
    def select_hardware_category(self):
        hware_link = self.driver.find_element(*CategoriesLocators.HWARE)
        hware_link.is_displayed()
        hware_link.is_enabled()
        hware_link.click()
    
    def select_software_category(self):
        sware_link = self.driver.find_element(*CategoriesLocators.SWARE)
        sware_link.is_displayed()
        sware_link.is_enabled()
        sware_link.click()
    
    def select_DVDs_category(self):
        dvd_link = self.driver.find_element(*CategoriesLocators.DVD)
        dvd_link.is_displayed()
        dvd_link.is_enabled()
        dvd_link.click()
    
    def select_gadgets_category(self):
        gadget_link = self.driver.find_element(*CategoriesLocators.GADGETS)
        gadget_link.is_displayed()
        gadget_link.is_enabled()
        gadget_link.click()
    
    
    def is_manufacturers_section_visible(self):
        return self.driver.find_element(*HomePageLocators.sMANUFACTURES).is_displayed()
    
    def is_quick_finds_section_visible(self):
        return self.driver.find_element(*HomePageLocators.sSEARCH).is_displayed()
        
    def is_promotion_section_visible(self):
        return self.driver.find_element(*HomePageLocators.sPROMO).is_displayed()
    
    def is_shopping_cart_section_visible(self):
        return self.driver.find_element(*HomePageLocators.sCART).is_displayed()
    
    def is_order_history_section_visible(self):
        return self.driver.find_element(*HomePageLocators.sORDERS).is_displayed()
    
    def is_best_sellers_section_visible(self):
        return self.driver.find_element(*HomePageLocators.sBESTSELLERS).is_displayed()
    
    def is_specials_section_visible(self):
        return self.driver.find_element(*HomePageLocators.sSPECIALS).is_displayed()
    
    def is_reviews_section_visible(self):
        return self.driver.find_element(*HomePageLocators.sREVIEWS).is_displayed()
    
    def is_additional_information_section_visible(self):
        return self.driver.find_element(*HomePageLocators.sINFO).is_displayed()
    
    def is_currency_selection_visible(self):
        return self.driver.find_element(*HomePageLocators.sCURRENCIES).is_displayed()
    
    def select_currency(self):
        currency_menu = self.driver.find_element(*CurrencyListLocator.MENU)
    
    def select_product(self):
        """Catalog Section"""
        product_catalog = {
            2: 'Matrox G400 32MB',
            21: 'SWAT 3: Close Quarters Battle',
            16: 'Courage Under Fire',
            7: "You've Got Mail",
            8: "A Bug's Life",
            27: 'Hewlett Packard LaserJet 1100Xi',
            28: 'Samsung Galaxy Tab',
            9: 'Under Siege',
            24: 'Disciples: Sacred Lands'
        }
        product_selected = random.choice(list(product_catalog.values()))
        prod1 = self.driver.find_element(By.LINK_TEXT, f'{product_selected}')
        assert prod1.is_displayed()
        prod1.click()

    def select_from_hardware_catalog(self):
        """Categories Section: Hardware"""

        hardware_catalog = {
            1_4: 'Graphics Cards',
            1_5: 'Printers',
            1_6: 'Monitors',
            1_7: 'Speakers',
            1_8: 'Keyboards',
            1_9: 'Mice',
            1_16: 'Memory',
            1_17: 'CDROM Drives',
        }
        item_selected = random.choice(list(hardware_catalog.values()))
        prod1 = self.driver.find_element(By.LINK_TEXT, f'{item_selected}')
        prod1.is_displayed()
        prod1.click()

    def select_from_a_manufacturer(self):
        """Manufacturer's Section"""
        manufacturers_list = self.driver.find_element(*ManufacturersLocator.LIST)
        select_HP = self.driver.find_element(*ManufacturersLocator.OPTION_HP)
        manufacturers_list.click()
        select_HP.is_displayed()
        select_HP.click()

    def search_for_product(self):
        """Quick Find Section"""
        search_input = self.driver.find_element(*QuickFindLocator.INPUT)
        search_input.send_keys("Matrox G200 MMS", '\ue007')

    def select_featured_product(self):
        """What's New Section"""
        featured_item = self.driver.find_element(*FeaturedItemLocator.CELL)
        featured_item.click()

    def select_from_bestseller(self):
        """Best Seller's Section"""
        product_catalog = {
            1: 'Matrox G200 MMS',
            22: 'Unreal Tournament',
            28: 'Samsung Galaxy Tab',
            16: 'Courage Under Fire',
            12: 'Die Hard With A Vengeance',
            26: 'Microsoft IntelliMouse Explorer',
            25: 'Microsoft Internet Keyboard PS/2',
            27: 'Hewlett Packard LaserJet 1100Xi',
            21: 'SWAT 3: Close Quarters Battle',
            19: "There's Something About Mary"
        }
        product_selected = random.choice(list(product_catalog.values()))
        prod1 = self.driver.find_element(By.LINK_TEXT, f'{product_selected}')
        prod1.click()

    def select_from_specials(self):
        """Specials Section"""
        special_item = self.driver.find_element(*SpecialsLocator.CELL)
        special_item.click()

    def select_product_review(self):
        """Product Reviews Section"""
        reviews_item = self.driver.find_element(*ReviewLocator.CELL)
        reviews_item.click()