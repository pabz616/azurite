import pytest
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestCheckout():

    def test_checkout(self):
        # LAUNCH SITE
        self.driver.get(env.base_url)

        # TEST STEPS
        on.HomePage.is_title_matches(self)
        on.HomePage.select_product(self)
        #
        on.PDP.product_title_is_visible(self)
        on.PDP.select_options_and_add_to_cart(self)
        #
        on.ShoppingCart.check_all_ui(self)
        on.ShoppingCart.click_checkout(self)
        #
        on.SignInPage.title_is_visible(self)
        on.SignInPage.continue_as_returning_customer(self)
        #
        on.ShippingPage.title_is_visible(self)
        on.ShippingPage.confirm_shipping_address(self)
        on.ShippingPage.confirm_shipping_method(self)
        on.ShippingPage.proceed_to_billing(self)
        #
        on.PaymentInfoPage.title_is_visible(self)
        on.PaymentInfoPage.billing_address_is_visible(self)
        on.PaymentInfoPage.select_payment_method(self)
        #
        on.ConfirmationPage.title_is_visible(self)
        on.ConfirmationPage.shipping_information_is_visible(self)
        on.ConfirmationPage.billing_information_is_visible(self)
        on.ConfirmationPage.payment_information_is_visible(self)
        on.ConfirmationPage.product_ordered_is_visible(self)
        on.ConfirmationPage.confirm_total(self)
        on.ConfirmationPage.submit_order(self)
        #
        on.OrderCompletionPage.order_is_successful(self)
        on.OrderCompletionPage.continue_shopping(self)