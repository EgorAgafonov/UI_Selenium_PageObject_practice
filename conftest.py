import pytest
from selenium import webdriver
from settings import *
from selenium.webdriver.chrome.options import *
from datetime import *
import os


@pytest.fixture(scope='function', autouse=True)
def duration_of_test(request):
    start_time = datetime.now()
    print(f'\n1/3) Начало выполнения тестовой функции: {start_time} сек.')
    yield
    end_time = datetime.now()
    print(f'\n2/3) Окончание выполнения тестовой функции: {end_time} сек.')
    print(f"\n3/3) ВСЕГО продолжительность теста {request.function.__name__}: {end_time - start_time} сек.\n")


@pytest.fixture()
def driver():
    """Pytest-фикстура(декоратор) для запуска UI-тестов, спроектированных с помощью паттерна PageObjectModel и
    фреймворка Selenium. Определяет setup-настройки перед началом выполнения тестовой функции. Инициализирует настройки
    запуска браузера Chrome, выполняет предварительную авторизацию пользователя на сайте (страница с path = /login) c
    помощью ранее сформированного cookie-файла. Настоящая фикстура удобно реализует преимущества паттерна Page Object
    Model, позволяет осуществлять в UI-тестах вызов любых страниц сайта без необходимости каждый раз прописывать
    в тестовой функции скрипт авторизации, универсальна и применима в качестве аргумента к любой тестовой функции в
    рамках тестирования платформы petfriends.skillfactory.ru. Это ощутимо снижает время выполнения тестов, повышает
    восприятие и "читаемость" кода."""

    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    url = os.getenv("LOGIN_URL") or "https://petfriends.skillfactory.ru/login"
    driver.get(url)
    driver.add_cookie({"name": "session", "value": cookie_value})
    yield driver
    driver.quit()


@pytest.fixture()
def auth_driver():
    """Pytest-фикстура(декоратор) для запуска UI-тестов проверки модуля авторизации пользователя на сайте
    www.petfriends.skillfactory.ru.Аналогична setup-фикстуре driver (см. выше), за исключением отсутствия возможности
    предварительной авторизации соответственно."""

    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
