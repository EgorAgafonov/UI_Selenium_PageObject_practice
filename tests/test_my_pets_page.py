import pytest
from pages.my_pets_page import MyPetsPage
from selenium import webdriver
from settings import *
import time

driver = webdriver.Chrome()


class TestPetFriendsPages:

    def test_my_pets_page(self):

        page = MyPetsPage(driver)
        page.add_pet_btn_click()
        page.enter_photo(photo=photo_1_jpg)
        page.enter_name("Boris")
        page.enter_breed("ginger")
        page.enter_age(17)
        time.sleep(2)
        page.submit_pet_btn()
        time.sleep(2)
    # assert page.get_relative_link() == "/all_pets"