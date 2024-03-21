import pytest
from pages.my_pets_page import MyPetsPage
from settings import *
from colorama import Fore, Style
import allure
from allure_commons.types import LabelType


@allure.epic("UI-PetFriends")
@allure.feature("Функциональное тестирование UI (негативные тесты)")
@allure.story("Создание карточек питомцев (негативные тесты).")
@allure.label("Агафонов Е.А.", "владелец")
@allure.label(LabelType.LANGUAGE, "Python")
@allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
class TestMyPetsPageNegative:

    # @pytest.mark.skip(reason="Тест генерирует 16 тест-кейсов, выполнять по необходимости!")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Параметризация создания простой карточки питомца (без фото) с не верифицированными значениями.")
    @allure.testcase("https://petfriends.skillfactory.ru/my_pets", "TC-CPS-01-NEG-PARAM")
    @allure.link("https://petfriends.skillfactory.ru/my_pets", name="https://petfriends.skillfactory.ru/my_pets")
    @pytest.mark.create_pet_negative
    @pytest.mark.parametrize("photo", [photo_3_bmp, photo_4_gif], ids=["photo .bmp", "photo .gif"])
    @pytest.mark.parametrize("name", [digits(), special_chars()], ids=["name digits", "name special_chars"])
    @pytest.mark.parametrize("breed", [digits(), special_chars()], ids=["breed digits", "breed special_chars"])
    @pytest.mark.parametrize("age", [-3, 1000], ids=["negative num", "unreal num"])
    def test_create_pet_params_negative(self, driver, photo, name, breed, age):
        """Негативный тест проверки создания карточек питомцев с не верифицированными параметрами значений согласно
        спецификации. Реализована техника попарного тестирования Pairwise. Валидация каждого негативного теста выполнена
        успешно в случае, если после ввода недопустимых значений в форму карточки, система отказывает в размещении
        карточки на сайте, а количество карточек до начала теста равно количеству карточек после теста (т.е. карточка
        не создана)."""

        page = MyPetsPage(driver)
        page.wait_page_loaded()
        cards_before_create = page.get_pets_quantity(driver)
        page.add_pet_btn_click()
        page.wait_page_loaded()
        page.enter_photo(photo)
        page.wait_page_loaded()
        page.enter_name(name)
        page.wait_page_loaded()
        page.enter_breed(breed)
        page.wait_page_loaded()
        page.enter_age(age)
        page.wait_page_loaded()
        page.submit_pet_btn_click()
        page.wait_page_loaded()
        page.refresh_page()
        page.wait_page_loaded()
        cards_after_create = page.get_pets_quantity(driver)

        if cards_before_create == cards_after_create:
            page.save_screenshot()
            print(f"\nКол-во карточек до момента выполнения теста: {cards_before_create}\nКол-во карточек после "
                  f"выполнения теста: {cards_after_create}")
            print(Style.DIM + Fore.GREEN + f"\nКарточка не создана, в воде недопустимых значений отказано, валидация"
                                           f" негативного теста прошла успешно!")
        else:
            print(f"\nКол-во карточек до момента выполнения теста: {cards_before_create}\nКол-во карточек после "
                  f"выполнения теста: {cards_after_create}")
            raise Exception(Style.DIM + Fore.RED + f"\nОшибка! Создана карточка с некорректным типом данных. Создать"
                                                   f" баг-репорт и отразить ошибку в системе отслеживания.")

