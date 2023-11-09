import pytest

from conftest import driver
from pages.my_pets_page import MyPetsPage
from settings import *
from colorama import Fore, Style
import time


class TestPetFriendsPages:
    @pytest.mark.parametrize("photo", [photo_1_jpg, photo_2_jpg], ids=["photo_jpeg_>100kb", "photo_jpeg_<100kb"])
    def test_my_pets_page(self, driver, photo):

        page = MyPetsPage(driver)
        page.add_pet_btn_click()
        page.enter_photo(photo)
        page.enter_name("Boris")
        page.enter_breed("ginger")
        page.enter_age(17)
        page.submit_pet_btn_click()

        if page.get_relative_link() != "/my_pets":
            print(Style.DIM + Fore.RED + f"\nКарточка питомца не создана!")
        else:
            assert page.get_relative_link() == "/my_pets"
            print(Style.DIM + Fore.GREEN + f"\nКарточка питомца успешно создана!")
