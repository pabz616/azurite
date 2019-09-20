import pytest
from utils import environment as env
from pages import confirmationPage as cp
from pages import homePage as hp
from pages import paymentInfoPage as pip
from pages import productDetailsPage as pdp
from pages import shippingPage as shp
from pages import shoppingCartPage as scp
from pages import signInPage as sip
from pages import successPage as sp


@pytest.mark.usefixtures("test_setup")
class TestCheckout():
    def test_checkout(self):
        # LAUNCH SITE
        self.driver.get(env.page_url)

        # PAGES BEING TESTED
        driver = self.driver

        on_landing_page = hp.HomePage(driver)
        on_pdp = pdp.ProductDetailsPage(driver)
        on_shopping_cart = scp.ShoppingCartPage(driver)
        on_sign_in_page = sip.SignInPage(driver)
        on_shipping_page = shp.ShippingPage(driver)
        on_payment_info_page = pip.PaymentInfoPage(driver)
        on_confirmation_page = cp.ConfirmationPage(driver)
        on_order_completion_page = sp.SuccessPage(driver)

        # TEST STEPS
        on_landing_page.is_title_matches()
        on_landing_page.select_product()
        #
        on_pdp.product_title_is_visible()
        on_pdp.select_options_and_add_to_cart()
        #
        on_shopping_cart.check_all_ui()
        on_shopping_cart.click_checkout()
        #
        on_sign_in_page.title_is_visible()
        on_sign_in_page.continue_as_returning_customer()
        #
        on_shipping_page.title_is_visible()
        on_shipping_page.confirm_shipping_address()
        on_shipping_page.confirm_shipping_method()
        on_shipping_page.proceed_to_billing()
        #
        on_payment_info_page.title_is_visible()
        on_payment_info_page.billing_address_is_visible()
        on_payment_info_page.select_payment_method()
        #
        on_confirmation_page.title_is_visible()
        on_confirmation_page.shipping_information_is_visible()
        on_confirmation_page.billing_information_is_visible()
        on_confirmation_page.payment_information_is_visible()
        on_confirmation_page.product_ordered_is_visible()
        on_confirmation_page.confirm_total()
        on_confirmation_page.submit_order()
        #
        on_order_completion_page.order_is_successful()
        on_order_completion_page.continue_shopping()
