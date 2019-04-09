from selenium import webdriver


class Browser(object):

    # driver = webdriver.Firefox()
    driver = webdriver.Chrome(executable_path='../features/drivers/chromedriver')
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(self, context):
        context.driver.close()