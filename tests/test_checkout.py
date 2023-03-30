import time

import pytest
from utils.test_data import base_url
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestCheckout:

    def test_purchase_from_catalog_as_return_customer(self):
        """PURCHASE ITEM AS A RETURN CUSTOMER"""
        self.driver.get(base_url)

        # TEST STEPS
        on.HomePage.select_product(self)
        on.PDP.add_to_cart(self)
        on.ShoppingCart.click_checkout(self)
        on.SignInPage.continue_as_returning_customer(self)
        on.ShippingPage.proceed_to_billing(self)
        on.PaymentInfoPage.select_payment_method(self)
        on.ConfirmationPage.submit_order(self)
        on.OrderCompletionPage.confirm_order_is_successful_and_continue(self)
        on.GlobalHeader.click_logout(self)

    def test_purchase_from_catalog_as_guest(self):
        """PURCHASE ITEM AS A NEW CUSTOMER"""
        self.driver.get(base_url)
        on.HomePage.select_product(self)
        on.PDP.add_to_cart(self)
        on.ShoppingCart.click_checkout(self)
        on.SignInPage.continue_as_new_customer(self)
        on.AccountInfoPage.submit_account_information(self)
        on.AccountSuccessPage.proceed_to_next_step(self)
        on.ShippingPage.proceed_to_billing(self)
        on.PaymentInfoPage.select_payment_method(self)
        on.ConfirmationPage.submit_order(self)
        on.OrderCompletionPage.confirm_order_is_successful_and_continue(self)
        on.GlobalHeader.click_logout(self)

    @pytest.mark.skip(reason="FIX ME - Some randomly selected categories have no items causing this test to fail")
    def test_purchase_from_hardware_catalog(self):
        """PURCHASE ITEM FROM CATEGORY SECTION: HARDWARE"""
        self.driver.get(base_url+'?cPath=1')
        on.HomePage.select_from_hardware_catalog(self)
        on.PLP.select_available_product(self)
        on.PDP.add_to_cart(self)
        on.ShoppingCart.click_checkout(self)
        on.SignInPage.continue_as_returning_customer(self)
        on.ShippingPage.proceed_to_billing(self)
        on.PaymentInfoPage.select_payment_method(self)
        on.ConfirmationPage.submit_order(self)
        on.OrderCompletionPage.confirm_order_is_successful_and_continue(self)
        on.GlobalHeader.click_logout(self)

    def test_purchase_monthly_hardware_special(self):
        """PURCHASE FROM CATEGORIES SECTION - HARDWARE CATALOG: MONTHLY SPECIAL"""
        self.driver.get(base_url+'?cPath=1')
        on.HardwareCatalogPage.selectMonthlyFeaturedProduct(self)
        on.PDP.add_to_cart(self)
        on.ShoppingCart.click_checkout(self)
        on.SignInPage.continue_as_returning_customer(self)
        on.ShippingPage.proceed_to_billing(self)
        on.PaymentInfoPage.select_payment_method(self)
        on.ConfirmationPage.submit_order(self)
        on.OrderCompletionPage.confirm_order_is_successful_and_continue(self)
        on.GlobalHeader.click_logout(self)

    def test_purchase_from_software_catalog(self):
        """PURCHASE ITEM FROM CATEGORY SECTION: SOFTWARE"""
        self.driver.get(base_url+'?cPath=2')
        on.SoftwareCatalogPage.selectAction(self)
        on.PDP.add_to_cart(self)
        on.ShoppingCart.click_checkout(self)
        on.SignInPage.continue_as_returning_customer(self)
        on.ShippingPage.proceed_to_billing(self)
        on.PaymentInfoPage.select_payment_method(self)
        on.ConfirmationPage.submit_order(self)
        on.OrderCompletionPage.confirm_order_is_successful_and_continue(self)
        on.GlobalHeader.click_logout(self)

    def test_purchase_monthly_software_special(self):
        """PURCHASE FROM CATEGORIES SECTION - SOFTWARE CATALOG: MONTHLY SPECIAL"""
        self.driver.get(base_url + '?cPath=2')
        on.SoftwareCatalogPage.selectMonthlyFeaturedProduct(self)
        on.PDP.add_to_cart(self)
        on.ShoppingCart.click_checkout(self)
        on.SignInPage.continue_as_returning_customer(self)
        on.ShippingPage.proceed_to_billing(self)
        on.PaymentInfoPage.select_payment_method(self)
        on.ConfirmationPage.submit_order(self)
        on.OrderCompletionPage.confirm_order_is_successful_and_continue(self)
        on.GlobalHeader.click_logout(self)

    def test_purchase_from_dvd_movies_catalog(self):
        """PURCHASE ITEM FROM CATEGORY SECTION: DVDs"""
        self.driver.get(base_url+'?cPath=3')

    def test_purchase_monthly_dvd_special(self):
        """PURCHASE FROM CATEGORIES SECTION - DVD CATALOG: MONTHLY SPECIAL"""
        pass

    def test_purchase_from_gadgets_catalog(self):
        """PURCHASE ITEM FROM CATEGORY SECTION: GADGET"""
        self.driver.get(base_url+'?cPath=21')

    def test_purchase_from_manufacturers_products_selection(self):
        """PURCHASE FROM MANUFACTURERS - PRODUCT SELECTION"""
        pass

    def test_purchase_from_quick_finds(self):
        """PURCHASE FROM QUICK FIND - SEARCH"""
        pass

    def test_purchase_from_whats_new(self):
        """PURCHASE FROM WHAT'S NEW SECTION - FEATURED ITEM"""
        pass

    def test_purchase_from_bestsellers(self):
        """PURCHASE FROM BEST SELLERS SECTION - FEATURED ITEM"""
        pass

    def test_purchase_from_specials(self):
        """PURCHASE FROM SPECIALS SECTION - FEATURED ITEM"""
        pass

    def test_purchase_from_reviews(self):
        """PURCHASE FROM PRODUCT REVIEWS SECTION"""
        pass

    def test_purchase_with_euros(self):
        """PURCHASE FROM PRODUCTS, CONVERTING THE SITE TO EUROS"""
        pass

    def test_get_information_shipping_returns(self):
        """GET INFORMATION - SHIPPING & RETURNS"""
        pass

    def test_get_information_privacy_notice(self):
        """GET INFORMATION - PRIVACY NOTICE"""
        pass

    def test_get_information_conditions_of_use(self):
        """GET INFORMATION - CONDITIONS OF USE"""
        pass

    def test_get_information_contact_us(self):
        """GET INFORMATION - CONTACT US"""
        pass

    def test_my_account_access_account_information(self):
        """MY ACCOUNT - ACCESS ACCOUNT INFORMATION"""
        pass

    def test_my_account_access_address_book(self):
        """MY ACCOUNT - ACCESS ADDRESS BOOK"""
        pass

    def test_my_account_access_account_password(self):
        """MY ACCOUNT - ACCESS ACCOUNT PASSWORD"""
        pass

    def test_order_history_view_orders_made(self):
        """MY ORDERS - VIEW ALL PLACED ORDERS"""
        pass

    def test_email_notifications_subscribe_to_newsletters(self):
        """MY NOTIFICATIONS - SUBSCRIBE TO NEWSLETTERS"""
        pass

    def test_email_notifications_view_notifications_list(self):
        """MY NOTIFICATIONS - VIEW NOTIFICATIONS LIST"""
        pass