import time
from .base_page import BasePage
from .locators import AuthLocators
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os


class MyPetsPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://petfriends.skillfactory.ru/my_pets"
        driver.get(url)
        self.btn = driver.find_element(*AuthLocators.MYPETS_BTN)