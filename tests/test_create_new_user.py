import pytest
from utils.test_data import base_url
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestCreateAccount:
    def test_create_new_user(self):
        self.driver.get(base_url)
        on.GlobalHeader.navigate_to_my_account(self)
        on.SignInPage.continue_as_new_customer(self)
        on.AccountInfoPage.submit_account_information(self)
        on.GlobalHeader.click_logout(self)


