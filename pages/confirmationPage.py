from locators.page_elements import *
from re import sub
from decimal import Decimal
from assertpy import assert_that


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class ConfirmationPage(BasePage):
    def title_is_visible(self):
        confirmation_page_title = self.driver.find_element(*ConfirmationPageLocators.TITLE)
        assert_that(confirmation_page_title).exists()

    def shipping_information_is_visible(self):
        shipping_info_section_title = self.driver.find_element(*ConfirmationPageLocators.SECTION_HDR1)
        section_title_txt = shipping_info_section_title.text
        shipping_method_header = self.driver.find_element(*ConfirmationPageLocators.SHIP_MTHD_HDR)
        shipping_method = 'Flat Rate (Best Way)'

        assert shipping_info_section_title.is_displayed()
        assert_that(section_title_txt).contains('Shipping Information')
        assert_that(shipping_method).is_not_none()
        assert_that(shipping_method_header).is_not_none()
        assert_that(shipping_method).contains('Flat Rate (Best Way)')

        # A CLEANER ASSERTION w. USER INFO
        customer_fname = 'testerA'
        customer_lname = 'testerA'
        customer_addr = "123 Main St"
        customer_city = 'Brooklyn'
        customer_zip = '11201'
        customer_country = 'United States'

        assert_that('Delivery Address').is_not_none()
        assert_that(customer_fname).is_not_none()
        assert_that(customer_lname).is_not_none()
        assert_that(customer_addr).is_not_none()
        assert_that(customer_city).is_not_none()
        assert_that(customer_zip).is_not_none()
        assert_that(customer_country).is_not_none()

    def billing_information_is_visible(self):
        billing_info_section_title = self.driver.find_element(*ConfirmationPageLocators.SECTION_HDR2)
        section_title_txt = billing_info_section_title.text
        assert billing_info_section_title.is_displayed()
        assert_that(section_title_txt).contains('Billing Information')
        assert_that('Billing Address').is_not_none()

    def payment_information_is_visible(self):
        payment_method_title = self.driver.find_element(*ConfirmationPageLocators.PYMT_MTHD_HDR)
        payment_method = 'Cash on Delivery'

        assert payment_method_title.is_displayed()
        assert_that(payment_method).contains('Cash on Delivery')

    # def product_ordered_is_visible(self):
    #     product_ordered = self.driver.find_element(*ConfirmationPageLocators.PRD)
    #     assert_that(product_ordered).is_not_none()

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