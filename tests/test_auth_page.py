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
        time.sleep(1)
        page.btn_click()
        time.sleep(1)
        driver.get_cookies()

        assert page.get_relative_link() == "/all_pets"


