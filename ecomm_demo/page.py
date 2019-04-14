import datetime
from locators import *
from re import sub
from decimal import Decimal


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    def is_title_matches(self):
        # TODO - Make this a re-usable class - keep it DRY
        today = '{:%m-%d-%y %H:%M:%S}'.format(datetime.datetime.now())
        name = 'HomePage'
        self.driver.save_screenshot('./results/'+name+'_'+today+'.png')
        #
        return "Welcome to 5ElementsLearning" in self.driver.title

    def select_product(self):
        prod1 = self.driver.find_element(*HomePageLocators.PROD1)
        prod1.click()


class ProductDetailsPage(BasePage):
    def product_title_is_visible(self):
        product_title = self.driver.find_element(*PDPLocators.PDP_TITLE)
        today = '{:%m-%d-%y %H:%M:%S}'.format(datetime.datetime.now())
        name = 'ProductDetailsPage'
        self.driver.save_screenshot('./results/'+name+'_'+today+'.png')
        
        assert product_title.is_displayed()

    def select_options_and_add_to_cart(self):
        # SELECTING THE MEMORY
        ddl_memory = self.driver.find_element(*PDPLocators.MEMORY_LIST)
        ddl_memory.click()

        o_8mb = self.driver.find_element(*PDPLocators.MEMORY_VALUE)
        o_8mb.click()

        # SELECTING THE MODEL
        ddl_model = self.driver.find_element(*PDPLocators.MODEL_LIST)
        ddl_model.click()

        o_premium = self.driver.find_element(*PDPLocators.MODEL_VALUE)
        o_premium.click()

        # ADD TO CART
        add_to_cart = self.driver.find_element(*PDPLocators.CTA)
        add_to_cart.click()


class ShoppingCartPage(BasePage):
    def check_all_ui(self):
        today = '{:%m-%d-%y %H:%M:%S}'.format(datetime.datetime.now())
        name = 'ShoppingCartPage'
        self.driver.save_screenshot('./results/'+name+'_'+today+'.png')

        cart_page_title = self.driver.find_element(*MyCartPageLocators.CART_TITLE)
        assert cart_page_title.is_displayed()

        cart_prod_title = self.driver.find_element(*MyCartPageLocators.CART_SUBTITLE)
        assert cart_prod_title.is_displayed()

        cart_item_image = self.driver.find_element(*MyCartPageLocators.PROD_IMG)
        assert cart_item_image.is_displayed()

    def click_checkout(self):
        checkout_cta = self.driver.find_element(*MyCartPageLocators.CTA)
        checkout_cta.click()


class SignInPage(BasePage):
    def title_is_visible(self):
        today = '{:%m-%d-%y %H:%M:%S}'.format(datetime.datetime.now())
        name = 'SignInPage'
        self.driver.save_screenshot('./results/'+name+'_'+today+'.png')

        sign_in_title = self.driver.find_element(*SignInPageLocators.TITLE)
        assert sign_in_title.is_displayed()

    def continue_as_returning_customer(self):
        customer_email='testerA@domain.com'
        email_input = self.driver.find_element(*SignInPageLocators.USN)
        email_input.send_keys(customer_email)

        customer_password = 'password1'
        pwd_input = self.driver.find_element(*SignInPageLocators.PWD)
        pwd_input.send_keys(customer_password)

        sign_in_cta = self.driver.find_element(*SignInPageLocators.CTA)
        sign_in_cta.click()


class ShippingPage(BasePage):
    def title_is_visible(self):
        today = '{:%m-%d-%y %H:%M:%S}'.format(datetime.datetime.now())
        name = 'ShippingPage'
        self.driver.save_screenshot('./results/'+name+'_'+today+'.png')

        shipping_page_title = self.driver.find_element(*ShippingPageLocators.TITLE)
        assert shipping_page_title.is_displayed()

    def confirm_shipping_method(self):
        shipping_method_title = self.driver.find_element(*ShippingPageLocators.SHIPPING_SUBTITLE)
        assert shipping_method_title.is_displayed()

        shipping_option = self.driver.find_element(*ShippingPageLocators.SHIPPING_OPTION)
        assert shipping_option.is_displayed()

        shipping_method = self.driver.find_element(*ShippingPageLocators.SHIPPING_METHOD)
        assert shipping_method.is_displayed()

    def confirm_shipping_address(self):
        shipping_address = self.driver.find_element(*ShippingPageLocators.SHIPPING_ADDRESS)
        shipping_address.is_displayed()

    def proceed_to_billing(self):
        continue_cta = self.driver.find_element(*ShippingPageLocators.CTA)
        continue_cta.click()


class PaymentInfoPage(BasePage):
    def title_is_visible(self):
        today = '{:%m-%d-%y %H:%M:%S}'.format(datetime.datetime.now())
        name = 'PaymentInfoPage'
        self.driver.save_screenshot('./results/'+name+'_'+today+'.png')

        billing_page_title = self.driver.find_element(*PaymentInfoPageLocators.TITLE)
        assert billing_page_title.is_displayed()

    def billing_address_is_visible(self):
        billing_address = self.driver.find_element(*PaymentInfoPageLocators.BILLING_ADDR)
        assert billing_address.is_displayed()

    def select_payment_method(self):
        pymt_cod = self.driver.find_element(*PaymentInfoPageLocators.PAYMENT_METHOD_1)
        pymt_cod.click()

        continue_cta = self.driver.find_element(*PaymentInfoPageLocators.CTA)
        continue_cta.click()


class ConfirmationPage(BasePage):
    def title_is_visible(self):
        today = '{:%m-%d-%y %H:%M:%S}'.format(datetime.datetime.now())
        name = 'ConfirmationPage'
        self.driver.save_screenshot('./results/'+name+'_'+today+'.png')

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


class SuccessPage(BasePage):
    def order_is_successful(self):
        today = '{:%m-%d-%y %H:%M:%S}'.format(datetime.datetime.now())
        name = 'SuccessPage'
        self.driver.save_screenshot('./results/'+name+'_'+today+'.png')

        success_page_title = self.driver.find_element(*SuccessPageLocators.TITLE)
        assert success_page_title.is_displayed()

        success_msg = 'Your order has been successfully processed!'
        shipping_msg = 'Your products will arrive at their destination within 2-5 working days.'
        thanks_msg = 'Thanks for shopping with us online!'

        assert success_msg in self.driver.page_source
        assert shipping_msg in self.driver.page_source
        assert thanks_msg in self.driver.page_source

    def continue_shopping(self):
        continue_cta = self.driver.find_element(*SuccessPageLocators.CTA)
        continue_cta.click()
