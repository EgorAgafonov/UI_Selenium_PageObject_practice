import pytest
import allure
from allure_commons.types import LabelType
from pages.my_pets_page import MyPetsPage
from settings import *
from colorama import Fore, Style
from conftest import *


@allure.epic("UI-PetFriends")
@allure.feature("Функциональное тестирование UI (позитивные тесты)")
@allure.label("Агафонов Е.А.", "владелец")
@allure.label(LabelType.LANGUAGE, "Python")
@allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
class TestMyPetsPagePositive:

    @pytest.mark.one
    @pytest.mark.create_simple
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Создание карточек питомцев (позитивные тесты).")
    @allure.title("Создание простой карточки питомца (без фото)")
    @allure.testcase("https://petfriends.skillfactory.ru/my_pets", "TC-CPS-01-POS")
    @allure.link("https://petfriends.skillfactory.ru/my_pets", name="https://petfriends.skillfactory.ru/my_pets")
    def test_create_pet_simple_positive(self, driver):
        """Позитивный тест проверки создания карточки питомца без фото. Валидация теста выполнена успешно в случае,
        если после ввода всех необходимых данных в форму карточки, пользователь остается на страницы path = "/my_pets",
        а карточка отображается в стеке питомцев пользователя со всеми переданными данными (без фото соответственно)."""

        with allure.step("Шаг 1: Ввод данных и создание карточки питомца без фото."):
            page = MyPetsPage(driver)
            page.add_pet_btn_click()
            page.enter_name("Tusya")
            page.enter_breed("abyssinian")
            page.enter_age(1.6)
            page.submit_pet_btn_click()
        with allure.step("Шаг 2: Перезагрузка страницы с созданной карточкой питомца."):
            page.refresh_page()
            page.wait_page_loaded()
        with allure.step("Шаг 3: Assert-проверка успешной валидации теста."):
            if page.get_relative_link() != "/my_pets":
                allure.attach(page.get_page_screenshot_PNG(),
                              name="create_pet_simple_FAILED",
                              attachment_type=allure.attachment_type.PNG)
                print(Style.DIM + Fore.RED + f"\nКарточка питомца не создана!")
            else:
                assert page.get_relative_link() == "/my_pets"
                allure.attach(page.get_page_screenshot_PNG(),
                              name="create_pet_simple_SUCCESS",
                              attachment_type=allure.attachment_type.PNG)
                print(Style.DIM + Fore.GREEN + f"\nКарточка питомца успешно создана!")

    @pytest.mark.two
    @pytest.mark.create_wth_photo
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Создание карточек питомцев (позитивные тесты).")
    @allure.title("Создание карточки питомца с фото")
    @allure.testcase("https://petfriends.skillfactory.ru/my_pets", "TC-CPwPH-02-POS")
    @allure.link("https://petfriends.skillfactory.ru/my_pets", name="https://petfriends.skillfactory.ru/my_pets")
    def test_create_pet_wth_photo_positive(self, driver):
        """Позитивный тест проверки создания карточки питомца с фото. Валидация теста выполнена успешно в случае, если
         после ввода всех необходимых данных в форму карточки, пользователь остается на страницы с эндпоинтом
         "/my_pets", а карточка отображается в стеке питомцев пользователя со всеми указанными данными."""

        with allure.step("Шаг 1: Ввод данных и создание карточки питомца c фото."):
            page = MyPetsPage(driver)
            page.add_pet_btn_click()
            page.enter_photo(photo_2_jpg)
            page.enter_name("Чарльз")
            page.enter_breed("британская вислоухая")
            page.enter_age(9)
            page.submit_pet_btn_click()
        with allure.step("Шаг 2: Перезагрузка страницы с созданной карточкой питомца."):
            page.refresh_page()
            page.wait_page_loaded()
        with allure.step("Шаг 3: Assert-проверка успешной валидации теста."):
            if page.get_relative_link() != "/my_pets":
                allure.attach(page.get_page_screenshot_PNG(),
                              name="create_pet_wth_photo_FAILED",
                              attachment_type=allure.attachment_type.PNG)
                print(Style.DIM + Fore.RED + f"\nКарточка питомца не создана!")
            else:
                assert page.get_relative_link() == "/my_pets"
                allure.attach(page.get_page_screenshot_PNG(),
                              name="create_pet_wth_photo_PASSED",
                              attachment_type=allure.attachment_type.PNG)
                print(Style.DIM + Fore.GREEN + f"\nКарточка питомца успешно создана!")

    # @pytest.mark.skip(reason="Тест генерирует 16 тест-кейсов, выполнять по необходимости!")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Создание карточек питомцев (позитивные тесты).")
    @allure.title("Создание(генерация) карточек питомцев с параметризацией верифицированных данных:\n"
                  "'photo', 'name', breed, 'age'.")
    @allure.testcase("https://petfriends.skillfactory.ru/my_pets", "TC-CPwPARAM-03-POS")
    @allure.link("https://petfriends.skillfactory.ru/my_pets", name="https://petfriends.skillfactory.ru/my_pets")
    @pytest.mark.create_pairwise
    @pytest.mark.parametrize("photo", [photo_1_jpg, photo_2_jpg], ids=["photo_jpeg_>100kb", "photo_jpeg_<100kb"])
    @pytest.mark.parametrize("name", [russian_chars(), latin_chars()], ids=["cyrillic chars", "latin chars"])
    @pytest.mark.parametrize("breed", [russian_chars(), latin_chars()], ids=["cyrillic chars", "latin chars"])
    @pytest.mark.parametrize("age", [3, 0.9], ids=["integer num", "float num"])
    def test_create_pet_params_positive(self, driver, photo, name, breed, age):
        """Позитивный тест проверки создания карточек питомцев с верифицированными параметрами значений согласно
        спецификации. Реализована техника попарного тестирования Pairwise. Валидация каждого теста выполнена успешно в
        случае, если после ввода всех необходимых данных в форму карточки, пользователь остается на страницы с
        эндпоинтом "/my_pets", а каждая сгенерированная карточка отображается в стеке питомцев пользователя со всеми
        переданными через фикстуру данными."""

        with allure.step("Шаг 1: Создание карточки питомца с вериф. знач. photo, name, breed, age"):
            page = MyPetsPage(driver)
            page.add_pet_btn_click()
            page.enter_photo(photo)
            page.enter_name(name)
            page.enter_breed(breed)
            page.enter_age(age)
            page.submit_pet_btn_click()
        with allure.step("Шаг 2: Перезагрузка страницы после создания карточки."):
            page.refresh_page()
            page.wait_page_loaded()
        with allure.step("Шаг 3: Assert-проверка успешной валидации теста."):
            if page.get_relative_link() != "/my_pets":
                allure.attach(page.get_page_screenshot_PNG(),
                              name="create_pet_params_FAILED",
                              attachment_type=allure.attachment_type.PNG)
                print(Style.DIM + Fore.RED + f"\nКарточка питомца не создана!")
            else:
                assert page.get_relative_link() == "/my_pets"
                allure.attach(page.get_page_screenshot_PNG(),
                              name="create_pet_params_PASSED",
                              attachment_type=allure.attachment_type.PNG)
                print(Style.DIM + Fore.GREEN + f"\nКарточка питомца успешно создана!")

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Удаление карточки питомца (позитивные тесты).")
    @allure.title("Удаление карточки питомца из профиля пользователя")
    @allure.testcase("https://petfriends.skillfactory.ru/my_pets", "TC-DEL-05-POS")
    @allure.link("https://petfriends.skillfactory.ru/my_pets", name="https://petfriends.skillfactory.ru/my_pets")
    @pytest.mark.three
    @pytest.mark.delete_pet
    def test_delete_pet_positive(self, driver):
        """Позитивный тест проверки удаления пользователем ранее созданной им карточки питомца. Валидация теста
        выполнена успешно в случае, если после нажатия на элемент "Удалить питомца" в карточке питомца, указанная
        карточка пропадает из стека питомцев пользователя. Тест предусматривает проверку количества карточек до и после
        удаления."""

        with allure.step("Шаг 1: Проверка количества карточек питомцев в профиле (если нет ни одной -> Exception)."):
            page = MyPetsPage(driver)
            pets_quantity = page.get_pets_quantity(driver)
            if pets_quantity == 0:
                raise Exception("Добавленные(ый) пользователем питомцы(ец) отсутствуют(ет), нет ни одной карточки для "
                                "удаления!")
        with allure.step("Шаг 2: Удаление карточки питомца"):
            cards_before_delete = page.get_pets_quantity(driver)
            page.delete_pet_btn_click(driver)
            page.refresh_page()
            page.wait_page_loaded()
            cards_after_delete = page.get_pets_quantity(driver)
        with allure.step("Шаг 3: Assert-проверка количества карточек до/после удаления."):
            if cards_before_delete == cards_after_delete:
                allure.attach(page.get_page_screenshot_PNG(),
                              name="delete_pet_FAILED",
                              attachment_type=allure.attachment_type.PNG)
                raise Exception("Ошибка! Карточка питомца не удалена из профиля пользователя.")
            else:
                assert cards_before_delete != cards_after_delete
                allure.attach(page.get_page_screenshot_PNG(),
                              name="delete_pet_PASSED",
                              attachment_type=allure.attachment_type.PNG)
                print(f"\nКол-во карточек до удаления: {cards_before_delete} \nКол-во карточек после удаления: "
                      f"{cards_after_delete}")

    # @pytest.mark.skip(reason="Тест полностью 'чистит' профиль от всех карточек, выполнять по необходимости!")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Удаление карточки питомца (позитивные тесты).")
    @allure.title("Последовательное удаление всех карточек питомцев пользователя (очистка профиля)")
    @allure.testcase("https://petfriends.skillfactory.ru/my_pets", "TC-DEL-06-POS")
    @allure.link("https://petfriends.skillfactory.ru/my_pets", name="https://petfriends.skillfactory.ru/my_pets")
    @pytest.mark.four
    @pytest.mark.delete_all_pets
    def test_delete_all_pets_positive(self, driver):
        """Позитивный тест проверки удаления пользователем всех созданных им карточек питомцев. Валидация теста
        выполнена успешно в случае, если после последовательного воздействия на элемент "Удалить питомца" в каждой
        карточке питомца, все карточки будут удалены из стека пользователя. Тест предусматривает проверку количества
        карточек до и после удаления.
        P.S. По большей части тест создан для очистки профиля пользователя от ранее созданных карточек."""

        with allure.step("Шаг 1: Проверка количества карточек питомцев в профиле (если нет ни одной -> Exception)."):
            page = MyPetsPage(driver)
            page.wait_page_loaded()
            cards_before_delete = page.get_pets_quantity(driver)
            pets_quantity = page.get_pets_quantity(driver)
            if pets_quantity == 0:
                allure.attach(page.get_page_screenshot_PNG(),
                              name="delete_all_pets_FAILED",
                              attachment_type=allure.attachment_type.PNG)
                raise Exception("Добавленные(ый) пользователем питомцы(ец) отсутствуют(ет), нет ни одной карточки для "
                                "удаления!")
        with allure.step("Шаг 2: Удаление всех карточек питомцев из профиля"):
            while pets_quantity != 0:
                page.delete_pet_btn_click(driver)
                page.refresh_page()
                pets_quantity = page.get_pets_quantity(driver)
            cards_after_delete = page.get_pets_quantity(driver)
        with allure.step("Шаг 3: Assert-проверка количества карточек до/после удаления."):
            assert cards_after_delete == 0, "Ошибка, не все карточки удалены!"
            allure.attach(page.get_page_screenshot_PNG(),
                          name="delete_all_pets_PASSED",
                          attachment_type=allure.attachment_type.PNG)
            print(f"\nКол-во карточек до удаления: {cards_before_delete} \nКол-во карточек после удаления: "
                  f"{cards_after_delete}")
