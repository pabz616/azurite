"""
Unit tests for: 5 Elements Learning: Products Catalog (home page)
"""

import pytest
from utils.test_data import base_url
from utils.environment import Pages as on

@pytest.mark.usefixtures("test_setup")
class TestProductsCatalog:
    
    def test_homepage_loads(self):
        self.driver.get(base_url)
        on.HomePage.is_page_loaded(self, base_url)
 
    def test_homepage_title(self):
        self.driver.get(base_url)
        on.HomePage.is_title_matches(self)
        
    def test_homepage_copytext(self):
        self.driver.get(base_url)
        on.HomePage.is_copy_text_visible(self)
        
    def test_homepage_section_text(self):
        self.driver.get(base_url)
        on.HomePage.is_section_text_visible(self)
    
    def test_homepage_products_grid(self):
        self.driver.get(base_url)
        on.HomePage.is_product_catalog_visible(self)
        
    def test_homepage_product_selection(self):
        self.driver.get(base_url)
        on.HomePage.select_product(self)
        
    def test_select_by_categories_section(self):
        self.driver.get(base_url)
        on.HomePage.is_categories_section_visible(self)
        on.HomePage.select_hardware_category(self)
        on.HomePage.select_software_category(self)
        on.HomePage.select_DVDs_category(self)
                
    def test_select_by_manufacturer(self):
        self.driver.get(base_url)
        on.HomePage.is_manufacturers_section_visible(self)
        
    def test_search_by_manufacturer(self):
        self.driver.get(base_url)
        on.HomePage.is_quick_finds_section_visible(self)
        
    def test_select_promotion(self):
        self.driver.get(base_url)
        on.HomePage.is_promotion_section_visible(self)
        
    def test_shopping_cart_section(self):
        self.driver.get(base_url)
        on.HomePage.is_shopping_cart_section_visible(self)
        
    def test_order_history_section(self):
        self.driver.get(base_url)
        on.HomePage.is_order_history_section_visible(self)
        
    def test_select_bestseller(self):
        self.driver.get(base_url)
        on.HomePage.is_best_sellers_section_visible(self)
        
    def test_select_specials(self):
        self.driver.get(base_url)
        on.HomePage.is_specials_section_visible(self)
        
    def test_reviews_section(self):
        self.driver.get(base_url)
        on.HomePage.is_reviews_section_visible(self)
        
    def test_account_information_section(self):
        self.driver.get(base_url)
        on.HomePage.is_additional_information_section_visible(self)
        
    def test_change_currency(self):
        self.driver.get(base_url)
        on.HomePage.is_currency_selection_visible(self)