from selenium.webdriver.common.by import By
from selenium import webdriver
import colorama
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from settings import cookie_value
import time
from urllib.parse import urlparse


class BasePage(object):
    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def refresh_page(self):
        self.driver.refresh()

