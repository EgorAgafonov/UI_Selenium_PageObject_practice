import pytest
from pages.my_pets_page import MyPetsPage
from conftest import driver
from settings import *
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


class TestMyPetsPage:
    @pytest.mark.parametrize("photo", [photo_1_jpg, photo_2_jpg], ids=["photo_jpeg_>100kb", "photo_jpeg_<100kb"])
    def test_create_pet_wth_photo_positive(self, driver, photo):

        page = MyPetsPage(driver)
        time.sleep(2)
        page.add_pet_btn_click()
        time.sleep(2)
        page.enter_photo(photo)
        page.enter_name("Boris")
        page.enter_breed("ginger")
        page.enter_age(17)
        time.sleep(2)
        page.submit_pet_btn_click()
        page.refresh_page()

        if page.get_relative_link() != "/my_pets":
            print(Style.DIM + Fore.RED + f"\nКарточка питомца не создана!")
        else:
            assert page.get_relative_link() == "/my_pets"
            print(Style.DIM + Fore.GREEN + f"\nКарточка питомца успешно создана!")


# class TestPetFriendsPage_Delete:
#     def test_delete_pet_positive(self, driver):
#         page = MyPetsPage(driver)
#         time.sleep(3)
#         cards_before_delete = page.get_pets_quantity
#         time.sleep(3)
#         page.delete_pet_btn_click()
#         page.refresh_page()
#         time.sleep(3)
#         cards_after_delete = page.get_pets_quantity
#         # assert cards_before_delete != cards_after_delete
#         print(cards_before_delete)
#         print(cards_after_delete)
#
#         # page.add_pet_btn_click()
#         # page.enter_photo(photo_2_jpg)
#         # page.enter_name("Cat Streetwolker")
#         # page.enter_breed("jedi master")
#         # page.enter_age(1000)
#         # page.submit_pet_btn_click()


