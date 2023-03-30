""" SITE CONSTANTS GO HERE """

from pages import homePage as hp, \
    confirmationPage as cp, \
    paymentInfoPage as pip, \
    productDetailsPage as pdp, \
    productListPage as plp, \
    shippingPage as shp, \
    shoppingCartPage as scp, \
    signInPage as sip, \
    successPage as sp, \
    accountInfoPage as ap, \
    accountSuccessPage as asp, \
    globalHeader as header,\
    hardwareCatalogPage as hc, \
    softwareCatalogPage as sc, \
    dvdCatalogPage as dc, \
    gadgetsCatalogPage as gc


# PAGES
class Pages(object):
    GlobalHeader = header.GlobalHeader
    HomePage = hp.HomePage
    PLP = plp.ProductListPage
    PDP = pdp.ProductDetailsPage
    ShoppingCart = scp.ShoppingCartPage
    SignInPage = sip.SignInPage
    ShippingPage = shp.ShippingPage
    PaymentInfoPage = pip.PaymentInfoPage
    ConfirmationPage = cp.ConfirmationPage
    OrderCompletionPage = sp.SuccessPage
    AccountInfoPage = ap.AccountInfoPage
    AccountSuccessPage = asp.AccountSuccessPage
    HardwareCatalogPage = hc.HardwareCatalogPage
    SoftwareCatalogPage = sc.SoftwareCatalogPage
    DVDMoviesCatalogPage = dc.DVDMoviesCatalogPage
    GadgetsCatalogPage = gc.GadgetsCatalogPage

# PATH TO REPORTS
# REPORT_NAME.html
# ../reports/REPORT_NAME.html .. use --self-contained-html flag to be able to deliver report + styles

# FOR ALLURE
# create allure_reports directory (if not there)
# in terminal, cd to your tests directory
# run the command: python -m pytest alluredir=reports/allure_reports
# once the test is complete, run the command: allure serve allure_reports ..
# (this should open a temp instance in the browser with the reports)
