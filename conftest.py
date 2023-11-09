import pytest
from selenium import webdriver
from settings import *
import colorama
from selenium.webdriver.chrome.options import Options
from datetime import *


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
    """Pytest-фикстура(декоратор) для запуска авто-тестов с определенными в ней настройками (setup). Инициализирует
    настройки запуска браузера Chrome через веб-драйвер Selenium, а также выполняет авторизацию на сайте
    https://petfriends.skillfactory.ru (посредством передачи заранее полученных cookies). Предварительная авторизация
    на сайте перед началом тестовой функции позволяет:1) реализовать паттерн проектирования Page Object Model, 2)
    осуществлять в авто-тестах запрос url-адресов страниц сайта и переходить на них без необходимости каждый раз
    прописывать в тестовой функции скрипт авторизации на сайте, что существенно увеличивает восприятие тестов и снижает
    объем кода."""

    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    url = os.getenv("LOGIN_URL") or "https://petfriends.skillfactory.ru/login"
    driver.get(url)
    driver.add_cookie({"name": "session", "value": cookie_value})
    colorama.init()
    yield driver
    driver.quit()
