import pytest
from pages.my_pets_page import MyPetsPage
from settings import *
from colorama import Fore, Style
import time


class TestMyPetsPage:
    @pytest.mark.one
    @pytest.mark.create_simple
    def test_create_pet_simple_positive(self, driver):

        page = MyPetsPage(driver)
        page.add_pet_btn_click()
        page.enter_name("Kristi")
        page.enter_breed("abyssinian")
        page.enter_age(4)
        page.submit_pet_btn_click()
        page.scroll_down()

        if page.get_relative_link() != "/my_pets":
            print(Style.DIM + Fore.RED + f"\nКарточка питомца не создана!")
        else:
            assert page.get_relative_link() == "/my_pets"
            time.sleep(2)
            page.make_screenshot()
            print(Style.DIM + Fore.GREEN + f"\nКарточка питомца успешно создана!")

    @pytest.mark.two
    @pytest.mark.create_wth_photo
    def test_create_pet_wth_photo_positive(self, driver):
        """Позитивный тест проверки создания карточки питомца с фото. Валидация теста выполнена успешно в случае, если
         после ввода всех необходимых данных в форму карточки, пользователь остается на страницы с эндпоинтом
         "/my_pets", а карточка отображается в стеке питомцев пользователя со всеми указанными данными."""

        page = MyPetsPage(driver)
        page.add_pet_btn_click()
        page.enter_photo(photo_1_jpg)
        page.enter_name("Чарльз")
        page.enter_breed("британская вислоухая")
        page.enter_age(9)
        page.submit_pet_btn_click()
        page.scroll_down()

        if page.get_relative_link() != "/my_pets":
            print(Style.DIM + Fore.RED + f"\nКарточка питомца не создана!")
        else:
            assert page.get_relative_link() == "/my_pets"
            print(Style.DIM + Fore.GREEN + f"\nКарточка питомца успешно создана!")

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

    @pytest.mark.three
    @pytest.mark.delete_pet
    def test_delete_pet_positive(self, driver):
        """Позитивный тест проверки удаления пользователем ранее созданной им карточки питомца. Валидация теста
        выполнена успешно в случае, если после нажатия на элемент "Удалить питомца" в карточке питомца, указанная
        карточка пропадает из стека питомцев пользователя. Тест предусматривает проверку количества карточек до и после
        удаления."""

        page = MyPetsPage(driver)
        cards_before_delete = page.get_pets_quantity
        page.delete_pet_btn_click()
        page.refresh_page()
        page.scroll_down()
        cards_after_delete = page.get_pets_quantity - 1

        assert cards_before_delete != cards_after_delete, "Ошибка! Проверьте наличие хотя бы 1-ой карточки питомца в" \
                                                          "профиле и/или корректность пути локатора элемента."
        print(f"\nКол-во карточек до удаления: {cards_before_delete} \nКол-во карточек после удаления: "
              f"{cards_after_delete}")




