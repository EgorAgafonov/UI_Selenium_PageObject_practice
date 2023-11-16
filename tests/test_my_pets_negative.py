import pytest
from pages.my_pets_page import MyPetsPage
from settings import *
from colorama import Fore, Style
from selenium.webdriver.common.by import By
import time


class TestMyPetsPageNegative:

    # @pytest.mark.skip(reason="Тест генерирует 16 тест-кейсов, выполнять по необходимости!")
    @pytest.mark.create_pet_negative
    @pytest.mark.parametrize("photo", [photo_3_bmp, photo_4_gif], ids=["photo .bmp", "photo .gif"])
    @pytest.mark.parametrize("name", [digits(), special_chars()], ids=["name digits", "name special_chars"])
    @pytest.mark.parametrize("breed", [digits(), special_chars()], ids=["breed digits", "breed special_chars"])
    @pytest.mark.parametrize("age", [-3, 1000], ids=["negative num", "unreal num"])
    def test_create_pet_params_negative(self, driver, photo, name, breed, age):
        """Позитивный тест проверки создания карточек питомцев с верифицированными параметрами значений согласно
        спецификации. Реализована техника попарного тестирования Pairwise. Валидация каждого теста выполнена успешно в
        случае, если после ввода всех необходимых данных в форму карточки, пользователь остается на страницы с
        эндпоинтом "/my_pets", а каждая сгенерированная карточка отображается в стеке питомцев пользователя со всеми
        переданными через фикстуру данными."""

        page = MyPetsPage(driver)
        cards_before_create = page.get_pets_quantity(driver)
        page.add_pet_btn_click()
        page.enter_photo(photo)
        page.enter_name(name)
        page.enter_breed(breed)
        page.enter_age(age)
        page.submit_pet_btn_click()
        page.refresh_page()
        page.scroll_up()
        cards_after_create = page.get_pets_quantity(driver)

        if cards_before_create == cards_after_create:
            page.make_screenshot()
            print(f"\nКол-во карточек до момента выполнения теста: {cards_before_create}\nКол-во карточек после "
                  f"выполнения теста: {cards_after_create}")
            print(Style.DIM + Fore.GREEN + f"\nКарточка не создана, в воде недопустимых значений отказано, валидация"
                                           f" негативного теста прошла успешно!")
        else:
            print(f"\nКол-во карточек до момента выполнения теста: {cards_before_create}\nКол-во карточек после "
                  f"выполнения теста: {cards_after_create}")
            raise Exception(Style.DIM + Fore.RED + f"\nОшибка! Создана карточка с некорректным типом данных. Создать"
                                                   f" баг-репорт и отразить ошибку в системе отслеживания.")

