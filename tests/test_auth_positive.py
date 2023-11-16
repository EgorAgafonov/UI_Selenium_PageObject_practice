from pages.auth_page import AuthPage
from settings import *
import time


class TestsAuthPagePositive:
    """Класс с коллекцией UI-тестов для проверки модуля авторизации пользователя на платформе
    petfriends.skillfactory.ru, спроектированных с использованием паттерна PageObjectModel."""

    def test_auth_page(self, auth_driver):
        """Позитивный тест проверки авторизации пользователя на сайте. Валидация теста выполнена успешно в случае, если
        после ввода корректных адреса и пароля пользователя в форму авторизации, система авторизует пользователя на
        сайте и осуществляет его перевод на страницу path = "/all_pets"."""

        page = AuthPage(auth_driver)
        page.enter_email(email)
        page.enter_pass(password)
        page.btn_click()
        page_source = page.get_page_source()

        assert page.get_relative_link() == "/all_pets"
        print(f"\n{page_source}")


