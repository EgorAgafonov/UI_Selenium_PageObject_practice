import urllib
from urllib.parse import urlparse
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urlparse
import urllib.request
import os

url = "https://petfriends.skillfactory.ru/my_pets"
parsed_url = urlparse(url).path
print(parsed_url)