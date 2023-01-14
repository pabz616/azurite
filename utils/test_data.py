import random

"""TEST DATA"""

# ENVIRONMENT
base_url = 'https://5elementslearning.dev/demosite/index.php'

# TEST DATA
cust_email = 'jsnow@got.com'
cust_pwd = 'password123'

# PRODUCT
keyword = 'Matrox G200 MMS'

rand_id = str(random.randint(1, 9999))

# NEW CUSTOMER TEST DATA
cust_first_name = f"AWESOME{rand_id}"
cust_last_name = f"TESTER{rand_id}"
cust_birthday = "01/01/1979"
cust_email_address = cust_first_name+"@mail.com"
cust_job = "QA TESTER"
cust_address = "123 MAIN STREET"
cust_suburb = 'QA'
cust_zip = "10010"
cust_city = "NEW YORK"
cust_state = 'NY'
cust_telephone = "21233334455"
cust_password = 'password123'
cust_confirm_pwd = 'password123'