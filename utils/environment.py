""" SITE CONSTANTS GO HERE """

from pages import homePage as hp, \
    confirmationPage as cp, \
    paymentInfoPage as pip, \
    productDetailsPage as pdp, \
    shippingPage as shp, \
    shoppingCartPage as scp, \
    signInPage as sip, \
    successPage as sp, \
    accountInfoPage as ap


# PAGES
class Pages(object):
    HomePage = hp.HomePage
    PDP = pdp.ProductDetailsPage
    ShoppingCart = scp.ShoppingCartPage
    SignInPage = sip.SignInPage
    ShippingPage = shp.ShippingPage
    PaymentInfoPage = pip.PaymentInfoPage
    ConfirmationPage = cp.ConfirmationPage
    OrderCompletionPage = sp.SuccessPage
    AccountInfoPage = ap.AccountInfoPage


# ENVIRONMENT
base_url = 'http://5elementslearning.com/demosite/login.php'

# TEST DATA
cust_email = 'testerA@domain.com'
cust_pwd = 'password1'

# NEW CUSTOMER TEST DATA
cust_first_name = 'Daenerys'
cust_last_name = 'Targaryan'
cust_birday = '08/01/1968'
cust_email_address = 'khaleesi247@winterfell.com'
cust_job = 'Dragon Queen'
cust_address = '45 Dragon Glass Rd'
cust_suburb = 'South'
cust_zip = '10300'
cust_city = 'Westeros'
cust_state = 'NY'
cust_telephone = '302-122-3394'
cust_password = 'daeny123'
cust_confirm_pwd = 'daeny123'

# PATH TO REPORTS
# REPORT_NAME.html
# ../reports/REPORT_NAME.html .. use --self-contained-html flag to be able to deliver report + styles

# FOR ALLURE
# create allure_reports directory (if not there)
# in terminal, cd to your tests directory
# run the command: python -m pytest alluredir=reports/allure_reports
# once the test is complete, run the command: allure serve allure_reports ..
# (this should open a temp instance in the browser with the reports)
