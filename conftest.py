import pytest
from selenium import webdriver
from settings import *
import colorama
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    """Фикстура"""
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    url = os.getenv("LOGIN_URL") or "https://petfriends.skillfactory.ru/login"
    driver.get(url)
    driver.add_cookie({"name": "session", "value": cookie_value})
    colorama.init()
    yield driver
    driver.quit()
