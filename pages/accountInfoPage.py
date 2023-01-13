from locators.page_elements import *
from utils.test_data import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class AccountInfoPage(BasePage):
    def submit_account_information(self):
        gender_m = self.driver.find_element(*AccountInfoPageLocators.GENDER1)
        name_first = self.driver.find_element(*AccountInfoPageLocators.FNAME_INPUT)
        name_last = self.driver.find_element(*AccountInfoPageLocators.LNAME_INPUT)
        dob = self.driver.find_element(*AccountInfoPageLocators.DOB_INPUT)
        email = self.driver.find_element(*AccountInfoPageLocators.EMAIL_INPUT)
        company = self.driver.find_element(*AccountInfoPageLocators.COMP_NAME)
        address = self.driver.find_element(*AccountInfoPageLocators.STREET_INPUT)
        suburb = self.driver.find_element(*AccountInfoPageLocators.BURB_INPUT)
        zipcode = self.driver.find_element(*AccountInfoPageLocators.ZIP_INPUT)
        city = self.driver.find_element(*AccountInfoPageLocators.CITY_INPUT)
        state = self.driver.find_element(*AccountInfoPageLocators.STATE_INPUT)
        country_list = self.driver.find_element(*AccountInfoPageLocators.CTRY_LIST)
        o_usa = self.driver.find_element(*AccountInfoPageLocators.CTRY_OPTION_USA)
        telephone = self.driver.find_element(*AccountInfoPageLocators.TEL_INPUT)
        password = self.driver.find_element(*AccountInfoPageLocators.PWD1_INPUT)
        confirm_pwd = self.driver.find_element(*AccountInfoPageLocators.PWD2_INPUT)
        submit_cta = self.driver.find_element(*AccountInfoPageLocators.CTA)
        #
        gender_m.click()
        name_first.send_keys(env.cust_first_name)
        name_last.send_keys(env.cust_last_name)
        dob.send_keys(env.cust_birday)
        email.send_keys(env.cust_email)
        company.send_keys(env.cust_job)
        address.send_keys(env.cust_address)
        suburb.send_keys(env.cust_suburb)
        zipcode.send_keys(env.cust_zip)
        city.send_keys(env.cust_city)
        state.send_keys(env.cust_state)
        country_list.click()
        o_usa.click()
        telephone.send_keys(env.cust_telephone)
        password.send_keys(env.cust_password)
        confirm_pwd.send_keys(env.cust_confirm_pwd)
        submit_cta.click()








