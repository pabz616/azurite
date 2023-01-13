import pytest
from utils.test_data import base_url
from utils.environment import Pages as on
import urllib.request


@pytest.mark.usefixtures("test_setup")
class CreateAccount:

    def test_create_new_user(self):
        siteUrl = urllib.request.urlopen(base_url)
        site_status = siteUrl.getcode()
        status_ok = 200

        if site_status != status_ok:
            pytest.xfail("Site is down")
        else:
            self.driver.get(base_url)

            on.GlobalHeader.click_my_account(self)
            on.SignInPage.continue_as_new_customer(self)
            on.AccountInfoPage.submit_account_information(self)
