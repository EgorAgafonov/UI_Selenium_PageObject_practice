import pytest
from pages.auth_page import AuthPage
from pages.my_pets_page import MyPetsPage
from selenium import webdriver
from settings import *
import colorama
from colorama import Fore, Back, Style
import time

driver = webdriver.Chrome()
colorama.init()


class TestPetFriendsPages:
    @pytest.mark.parametrize("photo", [photo_1_jpg, photo_2_jpg], ids=["photo_jpeg_>100kb", "photo_jpeg_<100kb"])
    def test_my_pets_page(self, photo):
        page = AuthPage(driver)
        page.enter_email(email)
        page.enter_pass(password)
        page.btn_click()

        page = MyPetsPage(driver)
        page.add_pet_btn_click()
        page.enter_photo(photo)
        page.enter_name("Boris")
        page.enter_breed("ginger")
        page.enter_age(17)
        page.submit_pet_btn_click()

        if page.get_relative_link() != "/my_pets":
            print(Style.DIM + Fore.RED + f"\nКарточки питомцев не созданы!")
        else:
            assert page.get_relative_link() == "/my_pets"
            print(Style.DIM + Fore.GREEN + f"\nКарточки питомцев успешно созданы!")
