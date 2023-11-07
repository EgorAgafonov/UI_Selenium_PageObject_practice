import pytest

from pages.auth_page import AuthPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import selenium
from settings import *
import time

driver = webdriver.Chrome()


def test_auth_page():

    page = AuthPage(driver)
    page.enter_email(email)
    page.enter_pass(password)
    time.sleep(2)
    page.btn_click()

    assert page.get_relative_link() == "/all_pets"
