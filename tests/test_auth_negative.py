from pages.auth_page import AuthPage
from settings import *
from selenium.webdriver.common.by import By
import time


class TestsAuthPageNegative:
    """Класс с коллекцией негативных UI-тестов для проверки модуля авторизации пользователя на платформе
    petfriends.skillfactory.ru, спроектированных с использованием паттерна PageObjectModel."""

    def test_auth_page(self, auth_driver):
        """Негативный тест проверки авторизации пользователя на сайте.  Валидация теста выполнена успешно в случае, если
        после ввода некорректных адреса и пароля в форму авторизации, система отказывает пользователю в авторизации на
        сайте, перехода на страницу path = "/all_pets" не происходит, система выводит сервисное сообщение о
        некорректно указанных почте/пароле пользователя."""

        page = AuthPage(auth_driver)
        page.enter_email(invalid_email)
        page.enter_pass(invalid_password)
        time.sleep(2)
        page.btn_click()
        time.sleep(2)
        allert_msg = auth_driver.find_element(By.XPATH, "//div[@role='alert']").text

        assert allert_msg == "The combination of user name and password is incorrect"
        assert page.get_relative_link() != "/all_pets"


