from pages.auth_page import AuthPage
from settings import *
from selenium.webdriver.common.by import By
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
        time.sleep(1)
        allert_msg = auth_driver.find_element(By.XPATH, "//div[@role='alert']").text

        assert allert_msg == "The combination of user name and password is incorrect"
        assert page.get_relative_link() != "/all_pets"


