from .base_page import BasePage
from .locators import MyPetsLocators
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
import colorama
from selenium.webdriver.chrome.options import Options

from settings import cookie_value
import time


class MyPetsPage(BasePage):
    """"""
    def __init__(self, driver, timeout=15):
        super().__init__(driver, timeout)

        self.add_pet_btn = driver.find_element(*MyPetsLocators.MY_PETS_NEW_PET_BTN)
        self.submit_pet_btn = driver.find_element(*MyPetsLocators.MY_PETS_SUBMIT_PET_BTN)
        self.delete_pet_btn = driver.find_element(*MyPetsLocators.MY_PETS_DELETE_PET_BTN)
        self.get_pets_quantity = len(driver.find_elements(*MyPetsLocators.MY_PETS_CARDS_QUANTITY))
        self.photo = driver.find_element(*MyPetsLocators.MY_PETS_PHOTO)
        self.name = driver.find_element(*MyPetsLocators.MY_PETS_NAME)
        self.breed = driver.find_element(*MyPetsLocators.MY_PETS_BREED)
        self.age = driver.find_element(*MyPetsLocators.MY_PETS_AGE)

    def enter_photo(self, photo):
        self.photo.send_keys(photo)

    def enter_name(self, value):
        self.name.send_keys(value)

    def enter_breed(self, value):
        self.breed.send_keys(value)

    def enter_age(self, value):
        self.age.send_keys(value)

    def add_pet_btn_click(self):
        self.add_pet_btn.click()

    def submit_pet_btn_click(self):
        self.submit_pet_btn.click()

    def delete_pet_btn_click(self):
        self.delete_pet_btn.click()

