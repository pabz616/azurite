"""
SITE CONSTANTS GO HERE
"""
import inspect

# ENVIRONMENT
page_url = 'http://5elementslearning.com/demosite/login.php'

# TEST DATA
cust_email = 'testerA@domain.com'
cust_pwd = 'password1'

# PATH TO REPORTS
# REPORT_NAME.html
# ../reports/REPORT_NAME.html .. use --self-contained-html flag to be able to deliver report + styles

# FOR ALLURE
# create allure_reports directory (if not there)
# in terminal, cd to your tests directory
# run the command: python -m pytest alluredir=reports/allure_reports
# once the test is complete, run the command: allure serve allure_reports ..
# (this should open a temp instance in the browser with the reports)


# GET THE NAME OF THE TEST FUNCTIONS TO USE LATER
def whoami():
    return inspect.stack[1][3]