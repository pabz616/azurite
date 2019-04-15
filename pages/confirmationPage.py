import moment
from locators.page_elements import *
from re import sub
from decimal import Decimal


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class ConfirmationPage(BasePage):
    def title_is_visible(self):
        #
        timestamp = moment.now().strftime("%m-%d-%y_%H-%M-%S")
        file_loc = '../screenshots/'
        file_name = 'ConfirmationPage'
        file_type = '.png'
        screenshot = file_loc + file_name + '_' + timestamp + file_type

        self.driver.save_screenshot(screenshot)
        #
        confirmation_page_title = self.driver.find_element(*ConfirmationPageLocators.TITLE)
        assert confirmation_page_title.is_displayed()

    def shipping_information_is_visible(self):
        shipping_info_section_title = self.driver.find_element(*ConfirmationPageLocators.SECTION_HDR1)
        section_title_txt = shipping_info_section_title.text
        shipping_method_header = self.driver.find_element(*ConfirmationPageLocators.SHIP_MTHD_HDR)
        shipping_method = 'Flat Rate (Best Way)'

        assert shipping_info_section_title.is_displayed()
        assert section_title_txt == 'Shipping Information'
        assert shipping_method_header.is_displayed()
        assert (shipping_method in self.driver.page_source)

        # A CLEANER ASSERTION w. USER INFO
        customer_fname = 'testerA'
        customer_lname = 'testerA'
        customer_addr = "123 Main St"
        customer_city = 'Brooklyn'
        customer_zip = '11201'
        customer_country = 'United States'

        assert 'Delivery Address' in self.driver.page_source
        assert customer_fname in self.driver.page_source
        assert customer_lname in self.driver.page_source
        assert customer_addr in self.driver.page_source
        assert customer_city in self.driver.page_source
        assert customer_zip in self.driver.page_source
        assert customer_country in self.driver.page_source

    def billing_information_is_visible(self):
        billing_info_section_title = self.driver.find_element(*ConfirmationPageLocators.SECTION_HDR2)
        section_title_txt = billing_info_section_title.text
        assert billing_info_section_title.is_displayed()
        assert section_title_txt == 'Billing Information'
        assert 'Billing Address' in self.driver.page_source

        # CUSTOMER BILLING ADDRESS IS THE SAME A SHIPPING, NO NEED FOR FURTHER ASSERTIONS

    def payment_information_is_visible(self):
        payment_method_title = self.driver.find_element(*ConfirmationPageLocators.PYMT_MTHD_HDR)
        payment_method = 'Cash on Delivery'

        assert payment_method_title.is_displayed()
        assert payment_method in self.driver.page_source

    def product_ordered_is_visible(self):
        assert 'Matrox G200 MMS' in self.driver.page_source

    def confirm_total(self):
        sub_total = self.driver.find_element(*ConfirmationPageLocators.PRD_SUB).text
        sub_chrg = Decimal(sub(r'[^\d.]', '', sub_total))

        ship_cost = self.driver.find_element(*ConfirmationPageLocators.SHIP_COST).text
        shipping_chrg = Decimal(sub(r'[^\d.]', '', ship_cost))

        calc_total = (sub_chrg+shipping_chrg)

        value = self.driver.find_element(*ConfirmationPageLocators.PRD_TOTAL).text
        displayed_total = Decimal(sub(r'[^\d.]', '', value))

        assert calc_total == displayed_total

    def submit_order(self):
        confirm_order_cta = self.driver.find_element(*ConfirmationPageLocators.CTA)
        confirm_order_cta.click()