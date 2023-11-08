import pytest
from pages.auth_page import AuthPage
from pages.my_pets_page import MyPetsPage
from selenium import webdriver
from settings import *
import time

driver = webdriver.Chrome()


class TestPetFriendsPages:

    def test_my_pets_page(self):
        page = AuthPage(driver)
        page.enter_email(email)
        page.enter_pass(password)
        page.btn_click()

        page = MyPetsPage(driver)
        page.add_pet_btn_click()
        page.enter_photo(photo=photo_1_jpg)
        page.enter_name("Boris")
        page.enter_breed("ginger")
        page.enter_age(17)
        page.submit_pet_btn_click()
        assert page.get_relative_link() == "/my_pets"