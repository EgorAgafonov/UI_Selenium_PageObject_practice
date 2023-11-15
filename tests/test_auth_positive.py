from pages.auth_page import AuthPage
from selenium import webdriver
from settings import *
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)


class TestPetFriendsPages:

    def test_auth_page(self):
        page = AuthPage(driver)
        page.enter_email(email)
        page.enter_pass(password)
        page.btn_click()
        time.sleep(3)

        assert page.get_relative_link() == "/all_pets"


