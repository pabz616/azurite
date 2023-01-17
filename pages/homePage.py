from locators.page_elements import *
import random


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    def is_title_matches(self):
        return "Welcome to 5ElementsLearning" in self.driver.title

    def select_product(self):
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