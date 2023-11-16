import pytest
from pages.my_pets_page import MyPetsPage
from settings import *
from colorama import Fore, Style
import time


class TestMyPetsPageNegative:

    @pytest.mark.create_pet_negative
    @pytest.mark.skip(reason="Тест генерирует 16 тест-кейсов, выполнять по необходимости!")
    @pytest.mark.create_pairwise
    @pytest.mark.parametrize("photo", [photo_1_jpg, photo_2_jpg], ids=["photo_jpeg_>100kb", "photo_jpeg_<100kb"])
    @pytest.mark.parametrize("name", [russian_chars(), latin_chars()], ids=["cyrillic chars", "latin chars"])
    @pytest.mark.parametrize("breed", [latin_chars(), russian_chars()], ids=["latin chars", "cyrillic chars"])
    @pytest.mark.parametrize("age", [3, 0.9], ids=["integer num", "float num"])
    def test_create_pet_params_positive(self, driver, photo, name, breed, age):
        """Позитивный тест проверки создания карточек питомцев с верифицированными параметрами значений согласно
        спецификации. Реализована техника попарного тестирования Pairwise. Валидация каждого теста выполнена успешно в
        случае, если после ввода всех необходимых данных в форму карточки, пользователь остается на страницы с
        эндпоинтом "/my_pets", а каждая сгенерированная карточка отображается в стеке питомцев пользователя со всеми
        переданными через фикстуру данными."""

        page = MyPetsPage(driver)
        page.add_pet_btn_click()
        page.enter_photo(photo)
        page.enter_name(name)
        page.enter_breed(breed)
        page.enter_age(age)
        page.submit_pet_btn_click()
        page.scroll_down()

        if page.get_relative_link() != "/my_pets":
            print(Style.DIM + Fore.RED + f"\nКарточка питомца не создана!")
        else:
            assert page.get_relative_link() == "/my_pets"
            print(Style.DIM + Fore.GREEN + f"\nКарточка питомца успешно создана!")





