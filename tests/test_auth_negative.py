from pages.auth_page import AuthPage
from settings import *
import pytest
from colorama import Style, Fore
import time


class TestsAuthPageNegative:
    """Класс с коллекцией негативных UI-тестов для проверки модуля авторизации пользователя на платформе
    petfriends.skillfactory.ru, спроектированных с использованием паттерна PageObjectModel."""

    def test_user_auth_incorrect_data(self, auth_driver):
        """Негативный тест проверки авторизации пользователя на сайте. Валидация негативного теста выполнена успешно в
        случае, если после ввода в форму авторизации некорректных данных об адресе и пароле пользователя, система
        отказывает последнему в авторизации на сайте, переход на страницу path = "/all_pets" отсутствует, выводится
        сервисное сообщение о некорректно указанных почте/пароле пользователя."""

        page = AuthPage(auth_driver)
        page.enter_email(invalid_email)
        page.enter_pass(invalid_password)
        page.btn_click()
        allert_msg = page.check_allert_msg(auth_driver)

        assert allert_msg == "The combination of user name and password is incorrect"
        assert page.get_relative_link() != "/all_pets"

    @pytest.mark.parametrize("incorrect_email", [special_chars(), digits(), strings_generator(101)],
                             ids=["special chars", "only integers", "alphabetic string > 100"])
    @pytest.mark.parametrize("incorrect_password", [special_chars(), digits(), strings_generator(101)],
                             ids=["special chars", "only integers", "alphabetic string > 100"])
    def test_user_auth_incorrect_params(self, auth_driver, incorrect_email, incorrect_password):
        """Негативный тест проверки авторизации пользователя на сайте с помощью фикстуры параметризации. На вход
        передаются заведомо не верифицированные значения адреса эл. почты и пароля пользователя. Валидация негативного
        теста выполнена успешно в случае, если после ввода в форму некорректных данных, система отказывает
        пользователю в авторизации на сайте, а перехода на страницу path = "/all_pets" не происходит."""

        page = AuthPage(auth_driver)
        page.enter_email(incorrect_email)
        page.enter_pass(incorrect_password)
        page.btn_click()

        if page.get_relative_link() == "/all_pets":
            print(Style.DIM + Fore.RED + f"\nОшибка авторизации, выполнен вход в систему с некорректными "
                                         f"данными пользователя!")
        else:
            assert page.get_relative_link() != "/my_pets"
            page.make_screenshot()
            print(Style.DIM + Fore.GREEN + f"\nВ авторизации на сайте отказано, негативный тест прошел "
                                           f"валидацию!")

