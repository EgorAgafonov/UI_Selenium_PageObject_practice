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
        url = os.getenv("MY_PETS_URL") or "https://petfriends.skillfactory.ru/my_pets"
        driver.get(url)
        self.new_pet_btn = driver.find_element(*AuthLocators.MY_PETS_NEW_PET_BTN)
        self.submit_pet_btn = driver.find_element(*AuthLocators.MY_PETS_SUBMIT_PET_BTN)
        self.photo = driver.find_element(*AuthLocators.MY_PETS_PHOTO)
        self.name = driver.find_element(*AuthLocators.MY_PETS_NAME)
        self.breed = driver.find_element(*AuthLocators.MY_PETS_BREED)
        self.age = driver.find_element(*AuthLocators.MY_PETS_AGE)

    def enter_photo(self, photo):
        self.photo.self.email.send_keys(photo)


