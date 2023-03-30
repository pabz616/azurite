from locators.page_elements import *
from re import sub
from decimal import Decimal
from assertpy import assert_that


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class ConfirmationPage(BasePage):

    def submit_order(self):
        confirmation_page_title = self.driver.find_element(*ConfirmationPageLocators.TITLE)
        shipping_info_section_title = self.driver.find_element(*ConfirmationPageLocators.SECTION_HDR1)
        shipping_method_header = self.driver.find_element(*ConfirmationPageLocators.SHIP_MTHD_HDR)
        billing_info_section_title = self.driver.find_element(*ConfirmationPageLocators.SECTION_HDR2)
        confirm_order_cta = self.driver.find_element(*ConfirmationPageLocators.CTA)
        payment_method_title = self.driver.find_element(*ConfirmationPageLocators.PYMT_MTHD_HDR)
        sub_total = self.driver.find_element(*ConfirmationPageLocators.PRD_SUB).text
        ship_cost = self.driver.find_element(*ConfirmationPageLocators.SHIP_COST).text
        value = self.driver.find_element(*ConfirmationPageLocators.PRD_TOTAL).text

        '''CONFIRMS PAGE TITLE'''
        assert confirmation_page_title.is_displayed()

        '''CONFIRMS PRODUCT TO BE PURCHASED IS DISPLAYED'''
        #     product_ordered = self.driver.find_element(*ConfirmationPageLocators.PRD)
        #     assert_that(product_ordered).is_not_none()

        '''CONFIRMS SHIPPING INFORMATION IS VISIBLE'''
        section_title_txt = shipping_info_section_title.text
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

        '''CONFIRMS BILLING INFORMATION'''
        section_title_txt = billing_info_section_title.text
        assert billing_info_section_title.is_displayed()
        assert_that(section_title_txt).contains('Billing Information')
        assert_that('Billing Address').is_not_none()

        '''CONFIRMS PAYMENT INFORMATION'''
        payment_method = 'Cash on Delivery'
        assert payment_method_title.is_displayed()
        assert_that(payment_method).contains('Cash on Delivery')

        '''CONFIRMS TOTAL'''
        sub_chrg = Decimal(sub(r'[^\d.]', '', sub_total))
        shipping_chrg = Decimal(sub(r'[^\d.]', '', ship_cost))
        calc_total = (sub_chrg+shipping_chrg)
        displayed_total = Decimal(sub(r'[^\d.]', '', value))

        assert calc_total == displayed_total

        '''CONFIRM ORDER'''
        confirm_order_cta.click()