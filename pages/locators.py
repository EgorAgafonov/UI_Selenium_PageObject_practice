from selenium.webdriver.common.by import By


class AuthLocators:
    AUTH_EMAIL = (By.ID, "email")
    AUTH_PASS = (By.ID, "pass")
    AUTH_BTN = (By.CLASS_NAME, "btn-success")
    MYPETS_NEW_PET_BTN = (By.CSS_SELECTOR, "button.btn.btn-outline-success")
    MYPETS_PHOTO = (By.ID, "photo")
    MYPETS_NAME = (By.ID, "name")
    MYPETS_BREED = (By.ID, "animal_type")
    MYPETS_AGE = (By.ID, "age")
    MYPETS_ADD_PET_BTN = (By.CSS_SELECTOR, "button[onclick='add_pet();']")
