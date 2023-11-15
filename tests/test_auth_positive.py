from pages.auth_page import AuthPage
from settings import *
import time


class TestPetFriendsPages:
    
    def test_auth_page(self, auth_driver):
        page = AuthPage(auth_driver)
        page.enter_email(email)
        page.enter_pass(password)
        page.btn_click()
        time.sleep(3)

        assert page.get_relative_link() == "/all_pets"


