from urllib.parse import urlparse
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urlparse
import os

# url = "https://petfriends.skillfactory.ru/my_pets"
# parsed_url = str(urlparse(url).path)
# print(parsed_url)

driver = webdriver.Chrome()


def get_relative_link():
    driver.get("https://petfriends.skillfactory.ru/my_pets")
    url = driver.current_url
    parsed_url = str(urlparse(url).path)
    return parsed_url


print(get_relative_link())
