from selenium.webdriver.common.by import By


class HomePageLocators(object):
    PROD1 = (By.XPATH, '//a[contains(.,"Matrox G200 MMS")]')


class PDPLocators(object):
    PDP_TITLE = (By.XPATH, '//h1[contains(.,"Matrox G200 MMS")]')
    MEMORY_LIST = (By.XPATH, '//select[contains(@name,"4")]')
    MEMORY_VALUE = (By.XPATH, '//option[@value="2"]')
    MODEL_LIST = (By.XPATH, '//select[contains(@name,"3")]')
    MODEL_VALUE = (By.XPATH, '//option[@value="6"]')
    CTA = (By.ID, 'tdb4')


class MyCartPageLocators(object):
    CART_TITLE = (By.XPATH, '//h1[contains(.,"My Cart")]')
    CART_SUBTITLE = (By.XPATH, '//h2[contains(.,"Product")]')
    PROD_IMG = (By.XPATH, '(//img)[2]')
    CTA = (By.ID, 'tdb5')


class SignInPageLocators(object):
    TITLE = (By.XPATH, '//h1[contains(.,"Sign In")]')
    USN = (By.NAME, 'email_address')
    PWD = (By.NAME, 'password')
    CTA = (By.ID, 'tdb5')


class ShippingPageLocators(object):
    TITLE = (By.XPATH, '//h1[contains(.,"Delivery Information")]')
    SHIPPING_SUBTITLE = (By.XPATH, '//h2[contains(.,"Shipping")]')
    SHIPPING_OPTION = (By.XPATH, '//strong[contains(.,"Flat Rate")]')
    SHIPPING_METHOD = (By.XPATH, '//td[contains(.,"Best Way")]')
    SHIPPING_ADDRESS = (By.XPATH, '(//div[contains(@class,"infoBoxContents")])[1]')
    CTA = (By.ID, 'tdb6')


class PaymentInfoPageLocators(object):
    TITLE = (By.XPATH, '//h1[contains(.,"Payment Information")]')
    BILLING_ADDR = (By.XPATH, '(//div[contains(@class,"infoBoxContents")])[1]')
    PAYMENT_METHOD_1 = (By.XPATH, '//input[@value="cod"]')
    PAYMENT_METHOD_2 = (By.XPATH, '//input[@value="paypal_express"]')
    CTA = (By.ID, 'tdb6')


class ConfirmationPageLocators(object):
    TITLE = (By.XPATH, '//h1[contains(.,"Order Confirmation")]')
    SECTION_HDR1 = (By.XPATH, '//h2[contains(.,"Shipping")]')
    SECTION_HDR2 = (By.XPATH, '//h2[contains(.,"Billing")]')
    DEL_ADDR_HDR = (By.XPATH, '//strong[contains(.,"Delivery Address")]')
    SHIP_MTHD_HDR = (By.XPATH, '//strong[contains(.,"Shipping Method")]')
    BILL_ADDR_HDR = (By.XPATH, '//strong[contains(.,"Billing Address")]')
    PYMT_MTHD_HDR = (By.XPATH, '//strong[contains(.,"Payment Method")]')
    PRD_SUB = (By.XPATH, '(//td[contains(@class,"main")])[2]')
    SHIP_COST = (By.XPATH, '(//td[contains(@class,"main")])[4]')
    PRD_TOTAL = (By.XPATH, '(//td[contains(@class,"main")])[6]')
    CTA = (By.ID, 'tdb5')


class SuccessPageLocators(object):
    TITLE = (By.XPATH, '//h1[contains(.,"Your Order Has Been Processed!")]')
    CTA = (By.ID, 'tdb5')
