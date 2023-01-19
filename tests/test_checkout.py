import pytest
from utils.test_data import base_url
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestCheckout:

    def test_checkout(self):
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

    def test_checkout_as_guest(self):
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

    def test_checkout_from_hardware(self):
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

    def test_checkout_from_software(self):
        """PURCHASE ITEM FROM CATEGORY SECTION: SOFTWARE"""
        self.driver.get(base_url+'?cPath=2')

    def test_checkout_from_DVD_movies(self):
        """PURCHASE ITEM FROM CATEGORY SECTION: DVDs"""
        self.driver.get(base_url+'?cPath=3')

    def test_checkout_from_gadgets(self):
        """PURCHASE ITEM FROM CATEGORY SECTION: GADGET"""
        self.driver.get(base_url+'?cPath=21')

