from selenium.webdriver.common.by import By


class HomePageLocators(object):
    pass


class GlobalHeaderLocators(object):
    LOGO = (By.XPATH, '[//img[@title="Demosite"]]')
    CTA1 = (By.ID, 'tdb1')
    CTA2 = (By.ID, 'tdb2')
    CTA3 = (By.ID, 'tdb3')
    CTA4 = (By.ID, 'tdb4')


class HardwareCatalogLocators(object):
    # SUBCATEGORIES LIST
    cdROMDRIVES = (By.XPATH, '(//a[contains(., "CDROM Drives")])[2]')
    GRAPHIC_CARDS = (By.XPATH, '(//a[contains(., "Graphics Cards")])[2]')
    KEYBOARDS = (By.XPATH, '(//a[contains(., "Keyboards")])[2]')
    MEMORY = (By.XPATH, '(//a[contains(., "Memory")])[2]')
    MICE = (By.XPATH, '(//a[contains(., "Mice")])[2]')
    MONITORS = (By.XPATH, '(//a[contains(., "Monitors")])[2]')
    PRINTERS = (By.XPATH, '(//a[contains(., "Printers")])[2]')
    SPEAKERS = (By.XPATH, '(//a[contains(., "Speakers")])[2]')

    # HARDWARE CATALOG
    o_cdROMDrives = (By.XPATH, '//a[contains(., "CDROM Drives")]')
    o_graphicCards = (By.XPATH, '//a[contains(., "Graphics Cards")]')
    o_keyboards = (By.XPATH, '//a[contains(., "Keyboards")]')
    o_memory = (By.XPATH, '//a[contains(., "Memory")]')
    o_mice = (By.XPATH, '//a[contains(., "Mice")]')
    o_monitors = (By.XPATH, '//a[contains(., "Monitors")]')
    o_printers = (By.XPATH, '//a[contains(., "Printers")]')
    o_speakers = (By.XPATH, '//a[contains(., "Speakers")]')

    # NEW PRODUCTS
    IMG = (By.XPATH, '//img[contains(@title, "Microsoft IntelliMouse Explorer")]')
    NAME = (By.XPATH, '//a[contains(., "IntelliMouse Explorer")]')
    PRICE = (By.XPATH, '//td[contains(.,"64.95")]')

    # PDP
    CTA = (By.ID, 'tdb4')


class SoftwareCatalogLocators(object):
    # SUBCATEGORIES LIST
    ACTION = (By.XPATH, '(//a[contains(., "Action")])[2]')
    SIM = (By.XPATH, '(//a[contains(., "Simulation")])[2]')
    STRAT = (By.XPATH, '(//a[contains(., "Strategy")])[2]')

    # SOFTWARE CATALOG
    o_action = (By.XPATH, '//a[contains(., "Action")]')
    o_simulation = (By.XPATH, '//a[contains(., "Simulation")]')
    o_strategy = (By.XPATH, '//a[contains(., "Strategy")]')

    # NEW PRODUCTS
    IMG = (By.XPATH, '//img[contains(@title, "Unreal Tournament")]')
    NAME = (By.XPATH, '(//a[contains(., "Unreal Tournament")])[1]')
    PRICE = (By.XPATH, '//td[contains(.,"89.99")]')

    # PDP
    CTA = (By.ID, 'tdb4')


class DVDMoviesCatalogLocators(object):
    # SUBCATEGORIES LIST
    action = (By.XPATH, '(//a[contains(., "Action")])[2]')
    cartoons = (By.XPATH, '(//a[contains(., "Cartoons")])[2]')
    comedy = (By.XPATH, '(//a[contains(., "Comedy")])[2]')
    drama = (By.XPATH, '(//a[contains(., "Drama")])[2]')
    science_fiction = (By.XPATH, '(//a[contains(., "Science Fiction")])[2]')
    thriller = (By.XPATH, '(//a[contains(., "Thriller")])[2]')

    # DVD MOVIE CATALOG
    o_action = (By.XPATH, '//a[contains(., "Action")]')
    o_cartoons = (By.XPATH, '//a[contains(., "Cartoons")]')
    o_comedy = (By.XPATH, '//a[contains(., "Comedy")]')
    o_drama = (By.XPATH, '//a[contains(., "Drama"]')
    o_science_fiction = (By.XPATH, '//a[contains(., "Science Fiction")]')
    o_thriller = (By.XPATH, '//a[contains(., "Thriller")]')

    # NEW PRODUCTS
    IMG = (By.XPATH, '//img[contains(@title, "Courage Under Fire")]')
    NAME = (By.XPATH, '(//a[contains(., "Courage Under Fire")])[1]')
    PRICE = (By.XPATH, '//td[contains(.,"29.99")]')

    # PDP
    CTA = (By.ID, 'tdb4')


class GadgetsCatalogLocators(object):
    IMG = (By.XPATH, '//img[@title="Samsung Galaxy Tab"]')
    NAME = (By.XPATH, '//a[contains(.,"Samsung Galaxy Tab")]')
    PRICE = (By.XPATH, '//td[contains(.,"$749.99")]')

    # PDP
    CTA = (By.ID, 'tdb4')


class ManufacturersLocator(object):
    LIST = (By.XPATH, '//select[@name="manufacturers_id"]')
    OPTION_HP = (By.XPATH, '//option[@value="9"]')


class QuickFindLocator(object):
    INPUT = (By.XPATH, '//input[@name="keywords"]')


class FeaturedItemLocator(object):
    CELL = (By.XPATH, '(//div[contains(@class, "infoBoxContents")])[4]')


class PLPLocators(object):
    PLP_TITLE = (By.XPATH, '//h1')
    NO_ITEM_MSG = (By.XPATH, '//div[@class="contentText"]/p')
    PROD_DATA = (By.XPATH, '//div[@class="contentContainer"]//table[@class="productListingData"]')
    PROD_NAME = (By.XPATH, '//*[@id="bodyContent"]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]')
    PROD_PRICE = (By.XPATH, '//*[@id="bodyContent"]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[3]')
    PROD_IMG = (By.XPATH, '(//img)[2]')
    CTA = (By.ID, 'tdb4')


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

    CONTINUE_CTA = (By.XPATH, '//a[contains(@id,"tdb4")]')


class AccountInfoPageLocators(object):
    GENDER1 = (By.XPATH, '//input[@value="m"]')
    GENDER2 = (By.XPATH, '//input[@value="f"]')
    FNAME_INPUT = (By.NAME, 'firstname')
    LNAME_INPUT = (By.NAME, 'lastname')
    DOB_INPUT = (By.NAME, 'dob')
    EMAIL_INPUT = (By.NAME, 'email_address')
    COMP_NAME = (By.NAME, 'company')
    STREET_INPUT = (By.NAME, 'street_address')
    BURB_INPUT = (By.NAME, 'suburb')
    ZIP_INPUT = (By.NAME, 'postcode')
    CITY_INPUT = (By.NAME, 'city')
    STATE_INPUT = (By.NAME, 'state')
    CTRY_LIST = (By.NAME, 'country')
    CTRY_OPTION_USA = (By.XPATH, '//option[@value="223"]')
    TEL_INPUT = (By.NAME, 'telephone')
    PWD1_INPUT = (By.NAME, 'password')
    PWD2_INPUT = (By.NAME, 'confirmation')
    CTA = (By.ID, 'tdb4')


class AccountSuccessLocators(object):
    TITLE = (By.XPATH, '//h1[contains(.,"Your Account Has Been Created!")]')
    BODY = (By.XPATH, '//div[@class="contentText"]')
    CTA = (By.ID, 'tdb5')


class ShippingPageLocators(object):
    TITLE = (By.XPATH, '//h1[contains(.,"Delivery Information")]')
    SHIPPING_SUBTITLE = (By.XPATH, '//h2[contains(.,"Shipping")]')
    SHIPPING_OPTION = (By.XPATH, '//strong[contains(.,"Flat Rate")]')
    SHIPPING_METHOD = (By.XPATH, '//td[contains(.,"Best Way")]')
    SHIPPING_ADDRESS = (By.XPATH, '(//div[contains(@class,"infoBoxContents")])[1]')
    CTA = (By.XPATH, '//button[contains(@id,"tdb6")]')


class PaymentInfoPageLocators(object):
    TITLE = (By.XPATH, '//h1[contains(.,"Payment Information")]')
    BILLING_ADDR = (By.XPATH, '(//div[contains(@class,"infoBoxContents")])[1]')
    PAYMENT_METHOD_1 = (By.XPATH, '//input[@value="cod"]')
    PAYMENT_METHOD_2 = (By.XPATH, '//input[@value="paypal_express"]')
    CTA = (By.ID, 'tdb6')


class ConfirmationPageLocators(object):
    TITLE = (By.XPATH, '//h1[contains(.,"Order Confirmation")]')
    SECTION_HDR1 = (By.XPATH, '(//div[@class="contentContainer"]/h2)[1]')
    SECTION_HDR2 = (By.XPATH, '(//div[@class="contentContainer"]/h2)[2]')
    DEL_ADDR_HDR = (By.XPATH, '//strong[contains(.,"Delivery Address")]')
    SHIP_MTHD_HDR = (By.XPATH, '//strong[contains(.,"Shipping Method")]')
    BILL_ADDR_HDR = (By.XPATH, '//strong[contains(.,"Billing Address")]')
    PYMT_MTHD_HDR = (By.XPATH, '//strong[contains(.,"Payment Method")]')
    PRD_SUB = (By.XPATH, '(//td[contains(@class,"main")])[2]')
    PRD = (By.XPATH,
           '#bodyContent > form > div > div:nth-child(2) > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(2)')
    SHIP_COST = (By.XPATH, '(//td[contains(@class,"main")])[4]')
    PRD_TOTAL = (By.XPATH, '(//td[contains(@class,"main")])[6]')
    CTA = (By.ID, 'tdb5')


class SuccessPageLocators(object):
    TITLE = (By.XPATH, '//h1[contains(.,"Your Order Has Been Processed!")]')
    CTA = (By.ID, 'tdb5')
