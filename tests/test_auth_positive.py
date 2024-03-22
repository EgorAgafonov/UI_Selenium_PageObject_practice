from pages.auth_page import AuthPage
from settings import *
import time
import allure
from allure_commons.types import LabelType


@allure.epic("UI-PetFriends")
@allure.feature("Функциональное тестирование UI (позитивные тесты)")
@allure.label("Агафонов Е.А.", "владелец")
@allure.label(LabelType.LANGUAGE, "Python")
@allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
class TestsAuthPagePositive:
    """Класс с коллекцией UI-тестов для проверки модуля авторизации пользователя на платформе
    petfriends.skillfactory.ru, спроектированных с использованием паттерна PageObjectModel."""

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story(" Авторизации пользователя на сайте (позитивные тесты).")
    @allure.title("Проверка стандартной авторизации пользователя с валидными значениями email и password")
    @allure.testcase("https://petfriends.skillfactory.ru/my_pets", "TC-AUTH-01-POS")
    @allure.link("https://petfriends.skillfactory.ru/login", name="https://petfriends.skillfactory.ru/login")
    def test_auth_page(self, auth_driver):
        """Позитивный тест проверки авторизации пользователя на сайте. Валидация теста выполнена успешно в случае, если
        после ввода корректных адреса и пароля пользователя в форму авторизации, система авторизует пользователя на
        сайте и осуществляет его перевод на страницу path = "/all_pets"."""

        page = AuthPage(auth_driver)
        page.enter_email(email)
        page.enter_pass(password)
        page.wait_page_loaded()
        page.btn_click()
        page.wait_page_loaded()

        assert page.get_relative_link() == "/all_pets"


