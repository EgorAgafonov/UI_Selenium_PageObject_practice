from selenium.webdriver.common.by import By
from selenium import webdriver
import colorama
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from settings import cookie_value
import time


class AuthLocators:
    AUTH_EMAIL = (By.ID, "email")
    AUTH_PASS = (By.ID, "pass")
    AUTH_BTN = (By.CLASS_NAME, "btn-success")


class MyPetsLocators:
    MY_PETS_NEW_PET_BTN = (By.CSS_SELECTOR, "button.btn.btn-outline-success")
    MY_PETS_SUBMIT_PET_BTN = (By.XPATH, "//button[@onclick='add_pet();']")
    MY_PETS_DELETE_PET_BTN = (By.XPATH, "//*[@id='all_my_pets'']/table[1]/tbody[1]/tr[1]/td[4]/a[1]/div[1]")
    MY_PETS_CARDS_QUANTITY = (By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")
    MY_PETS_PHOTO = (By.ID, "photo")
    MY_PETS_NAME = (By.ID, "name")
    MY_PETS_BREED = (By.ID, "animal_type")
    MY_PETS_AGE = (By.ID, "age")

