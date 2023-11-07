from selenium.webdriver.common.by import By


class AuthLocators:
    AUTH_EMAIL = (By.ID, "email")
    AUTH_PASS = (By.ID, "pass")
    AUTH_BTN = (By.CLASS_NAME, "btn-success")
    MY_PETS_NEW_PET_BTN = (By.CSS_SELECTOR, "button.btn.btn-outline-success")
    MY_PETS_PHOTO = (By.ID, "photo")
    MY_PETS_NAME = (By.ID, "name")
    MY_PETS_BREED = (By.ID, "animal_type")
    MY_PETS_AGE = (By.ID, "age")
    MY_PETS_SUBMIT_PET_BTN = (By.XPATH, "//button[@onclick='add_pet();']")
