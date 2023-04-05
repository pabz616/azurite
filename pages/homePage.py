from locators.page_elements import *
import random


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    def is_title_matches(self):
        return "Welcome to 5ElementsLearning" in self.driver.title

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
        prod1.click()

    def select_from_a_manufacturer(self):
        """Manufacturer's Section"""
        manufacturers_list = self.driver.find_element(*ManufacturersLocator.LIST)
        select_HP = self.driver.find_element(*ManufacturersLocator.OPTION_HP)
        manufacturers_list.click()
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