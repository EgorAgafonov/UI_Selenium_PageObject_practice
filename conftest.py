import pytest
from selenium import webdriver
from settings import *
from selenium.webdriver.chrome.options import *
from datetime import *
import os


@pytest.fixture(scope='function', autouse=True)
def duration_of_test(request):
    start_time = datetime.now()
    print(f'\nНачало выполнения тестовой функции: {start_time} сек.')
    yield
    end_time = datetime.now()
    print(f'Окончание выполнения тестовой функции: {end_time} сек.')
    print(f"ВСЕГО продолжительность теста {request.function.__name__}: {end_time - start_time} сек.\n")


@pytest.fixture()
def driver():
    """Pytest-фикстура(декоратор) для запуска UI-тестов, спроектированных с помощью фреймворка Selenium. Определяет
    setup-настройки перед началом выполнения тестовой функции. Инициализирует настройки запуска браузера Chrome,
    выполняет предварительную авторизацию на сайте (path=/login) посредством передачи cookie-файла, сгенерированного
    после предварительной "ручной" авторизации на указанном сайте. Настоящая фикстура удобно реализует преимущества паттерна Page Object
    Model, а также позволяет осуществлять в UI-тестах вызов любых страниц сайта без необходимости каждый раз прописывать
    в тестовой функции скрипт авторизации. Это ощутимо снижает время выполнения тестов, повышает восприятие и
    "читаемость" кода."""

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
    """Pytest-фикстура(декоратор) для запуска UI-тестов, спроектированных с помощью фреймворка Selenium. Определяет
    setup-настройки перед началом выполнения тестовой функции. Инициализирует настройки запуска браузера Chrome, создает
    объект класса webdriver.Chrome() для взаимодействия с одноименным браузером, а также выполняет авторизацию на сайте
    https://petfriends.skillfactory.ru (посредством передачи cookie-файла, сгенерированного после предварительной
    "ручной" авторизации на указанном сайте). Настоящая фикстура удобно реализует преимущества паттерна Page Object
    Model, а также позволяет осуществлять в UI-тестах вызов любых страниц сайта без необходимости каждый раз прописывать
    в тестовой функции скрипт авторизации. Это ощутимо снижает время выполнения тестов, повышает восприятие и
    "читаемость" кода."""

    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    url = os.getenv("LOGIN_URL") or "https://petfriends.skillfactory.ru/login"
    driver.get(url)
    driver.add_cookie({"name": "session", "value": cookie_value})
    url = os.getenv("MY_PETS_URL") or "https://petfriends.skillfactory.ru/my_pets"
    driver.get(url)
    yield driver
    driver.quit()
