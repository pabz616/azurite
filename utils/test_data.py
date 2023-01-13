import faker.providers.date_time as dt
import faker.providers.internet as it
import faker.providers.person as person
import faker.providers.job as company
import faker.providers.address as addr
import faker.providers.phone_number as tel

"""TEST DATA"""

# ENVIRONMENT
base_url = 'https://5elementslearning.dev/demosite/index.php'

# TEST DATA
cust_email = 'jsnow@got.com'
cust_pwd = 'password123'

# PRODUCT
keyword = 'Matrox G200 MMS'

# NEW CUSTOMER TEST DATA
fake_fName = person.Provider.first_name
fake_lName = person.Provider.first_name
month = dt.Provider.month
day = dt.Provider.day_of_week
year = dt.Provider.year
fake_email = it.Provider.ascii_free_email
fake_dob = f'{month}/{day}/{year}'
fake_job = company.Provider.job
fake_address = addr.Provider.street_address
fake_city = addr.Provider.city
fake_zip = addr.Provider.postcode
fake_phone = tel.Provider.phone_number

cust_first_name = fake_fName
cust_last_name = fake_lName
cust_birthday = fake_dob
cust_email_address = fake_email
cust_job = fake_job
cust_address = fake_address
cust_suburb = ''
cust_zip = fake_zip
cust_city = fake_city
cust_state = 'NY'
cust_telephone = fake_phone
cust_password = 'password123'
cust_confirm_pwd = 'password123'
