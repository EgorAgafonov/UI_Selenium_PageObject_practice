from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from tests.settings import cookie_value
import time

# url = "https://petfriends.skillfactory.ru/my_pets"
# parsed_url = urlparse(url).path
# colorama.init()
# print(Style.DIM + Fore.BLACK + Back.BLUE + f"Эндпоинт(path) url-адреса: {parsed_url}")


options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
url = os.getenv("LOGIN_URL") or "https://petfriends.skillfactory.ru/login"
driver.get(url)
driver.add_cookie({"name": "session", "value": cookie_value})
url = os.getenv("MY_PETS_URL") or "https://petfriends.skillfactory.ru/my_pets"
driver.get(url)
time.sleep(1)
cards_before = driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")
time.sleep(1)
driver.find_element(By.XPATH, "//a[@title='Удалить питомца']").click()
time.sleep(1)
driver.refresh()
time.sleep(1)
cards_after = driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")
time.sleep(1)
# driver.quit()
print(len(cards_before))
print(len(cards_after))





