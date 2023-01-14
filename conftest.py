""" MODULARIZED PYTEST FIXTURE TO RE-USE ON THE TESTS """

import pytest


# BROWSER SELECTION
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome-headless", help="Please select the browser you wish to use.")


@pytest.fixture(scope="class")
def test_setup(request):
    global driver

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager

    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        # RUNNING NORMAL
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser == 'chrome-headless':
        # RUNNING HEADLESS
        options = Options()
        options.headless = True
        options.add_argument('--disable-gpu')
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    driver.implicitly_wait(30)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()
    driver.quit()
    print('Test is finished.')