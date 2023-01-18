import pytest
from utils.test_data import base_url
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestCheckout:

    def test_checkout(self):
        self.driver.get(base_url)

        # TEST STEPS
        on.HomePage.select_product(self)
        on.PDP.add_to_cart(self)
        on.ShoppingCart.click_checkout(self)
        #
        on.SignInPage.continue_as_returning_customer(self)
        #
        on.ShippingPage.confirm_shipping_address(self)
        on.ShippingPage.confirm_shipping_method(self)
        on.ShippingPage.proceed_to_billing(self)
        #
        on.PaymentInfoPage.select_payment_method(self)
        #
        on.ConfirmationPage.shipping_information_is_visible(self)
        on.ConfirmationPage.billing_information_is_visible(self)
        on.ConfirmationPage.payment_information_is_visible(self)
        on.ConfirmationPage.confirm_total(self)
        on.ConfirmationPage.submit_order(self)
        #
        on.OrderCompletionPage.order_is_successful(self)
        on.OrderCompletionPage.continue_shopping(self)
        #
        on.GlobalHeader.click_logout(self)

    def test_checkout_as_guest(self):
        self.driver.get(base_url)
        on.HomePage.select_product(self)
        on.PDP.add_to_cart(self)
        on.ShoppingCart.click_checkout(self)
        on.SignInPage.continue_as_new_customer(self)
        on.AccountInfoPage.submit_account_information(self)
        on.AccountSuccessPage.proceed_to_next_step(self)
        #
        on.ShippingPage.confirm_shipping_address(self)
        on.ShippingPage.confirm_shipping_method(self)
        on.ShippingPage.proceed_to_billing(self)
        #
        on.PaymentInfoPage.select_payment_method(self)
        #
        on.ConfirmationPage.shipping_information_is_visible(self)
        on.ConfirmationPage.billing_information_is_visible(self)
        on.ConfirmationPage.payment_information_is_visible(self)
        on.ConfirmationPage.confirm_total(self)
        on.ConfirmationPage.submit_order(self)
        #
        on.OrderCompletionPage.order_is_successful(self)
        on.OrderCompletionPage.continue_shopping(self)
        #
        on.GlobalHeader.click_logout(self)



