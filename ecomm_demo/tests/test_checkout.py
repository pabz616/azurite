# SCOPE: E2E DEMO FOR USING PYTEST

from selenium import webdriver
from pages.homePage import HomePage
from pages.confirmationPage import ConfirmationPage
from pages.paymentInfoPage import PaymentInfoPage
from pages.productDetailsPage import ProductDetailsPage
from pages.shippingPage import ShippingPage
from pages.shoppingCartPage import ShoppingCartPage
from pages.signInPage import SignInPage
from pages.successPage import SuccessPage

import pytest
from selenium.webdriver.chrome.options import Options
from utils import environment as env


@pytest.fixture(autouse=True)
def test_setup():
    global driver

    # RUNNING HEADLESS
    options = Options()
    options.headless = True
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options, executable_path='../drivers/chromedriver')

    # RUNNING IN BROWSER
    # driver = webdriver.Chrome(executable_path='../drivers/chromedriver')

    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get(env.page_url)

    yield
    driver.close()
    #driver.quit()


def test_checkout():
    # PAGES BEING TESTED
    on_landing_page = HomePage(driver)
    on_pdp = ProductDetailsPage(driver)
    on_shopping_cart = ShoppingCartPage(driver)
    on_sign_in_page= SignInPage(driver)
    on_shipping_page = ShippingPage(driver)
    on_payment_info_page = PaymentInfoPage(driver)
    on_confirmation_page = ConfirmationPage(driver)
    on_order_completion_page = SuccessPage(driver)

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


if __name__ == "__main__":
    driver.main()