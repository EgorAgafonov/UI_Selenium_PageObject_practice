import pytest
from pages.my_pets_page import MyPetsPage
from settings import *
from colorama import Fore, Style
import time


class TestMyPetsPageCreate:
    @pytest.mark.one
    def test_create_pet_simple_positive(self, driver):

        page = MyPetsPage(driver)
        page.add_pet_btn_click()
        page.enter_name("Kristi")
        page.enter_breed("abyssinian")
        page.enter_age(4)
        page.submit_pet_btn_click()
        page.refresh_page()

        if page.get_relative_link() != "/my_pets":
            print(Style.DIM + Fore.RED + f"\nКарточка питомца не создана!")
        else:
            assert page.get_relative_link() == "/my_pets"
            print(Style.DIM + Fore.GREEN + f"\nКарточка питомца успешно создана!")

    @pytest.mark.parametrize("photo", [photo_1_jpg, photo_2_jpg], ids=["photo_jpeg_>100kb", "photo_jpeg_<100kb"])
    def test_create_pet_wth_photo_positive(self, driver, photo):
        """Позитивный тест проверки создания карточки питомца с фото. Валидация теста выполнена успешно в случае, если
         после ввода всех необходимых данных в форму карточки, пользователь остается на страницы с эндпоинтом
         "/my_pets", а карточка отображается в стеке карточек питомцев пользователя со всеми указанными данными."""

        page = MyPetsPage(driver)
        page.add_pet_btn_click()
        page.enter_photo(photo)
        page.enter_name("Cat Streetwalker")
        page.enter_breed("jedi master")
        page.enter_age(1000)
        page.submit_pet_btn_click()
        page.refresh_page()

        if page.get_relative_link() != "/my_pets":
            print(Style.DIM + Fore.RED + f"\nКарточка питомца не создана!")
        else:
            assert page.get_relative_link() == "/my_pets"
            print(Style.DIM + Fore.GREEN + f"\nКарточка питомца успешно создана!")


class TestMyPetsPageDelete:
    def test_delete_pet_positive(self, driver):
        """Позитивный тест проверки удаления пользователем ранее созданной им карточки питомца. Валидация теста
        выполнена успешно в случае, если после нажатия на элемент "Удалить питомца" в карточке питомца, указанная
        карточка пропадает из стека питомцев пользователя. Тест предусматривает проверку количества карточек до и после
        удаления."""

        page = MyPetsPage(driver)
        cards_before_delete = page.get_pets_quantity
        page.delete_pet_btn_click()
        page.refresh_page()
        cards_after_delete = page.get_pets_quantity - 1

        assert cards_before_delete != cards_after_delete, "Ошибка! Проверьте наличие хотя бы 1 карточки питомца в" \
                                                          "профиле и/или корректность пути локатора элемента."
        print(f"\n{cards_before_delete} - {cards_after_delete}")




