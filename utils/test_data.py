import faker.providers.date_time
import faker.providers.person
from faker import Faker

"""TEST DATA"""

# ENVIRONMENT
base_url = 'https://5elementslearning.dev/demosite/index.php'

# TEST DATA
cust_email = 'jsnow@got.com'
cust_pwd = 'password123'

# PRODUCT
keyword = 'Matrox G200 MMS'

# NEW CUSTOMER TEST DATA
# fake = faker.providers.person.Provider
Faker.seed(0)
job = faker.providers
f = faker.providers.person.Provider
date = faker.providers.date_time.Provider

month = date.month()
day = date.day_of_week()
year = date.year()

cust_first_name = f.first_name()
cust_last_name = f.last_name()
cust_birthday = month+'/'+day+'/'+year
cust_email_address = #todo add fake email
cust_job = #todo add fake job
cust_address = '45 Dragon Glass Rd'
cust_suburb = 'South'
cust_zip = '10300'
cust_city = 'Westeros'
cust_state = 'NY'
cust_telephone = '302-122-3394'
cust_password = 'daeny123'
cust_confirm_pwd = 'daeny123'