import pytest
from datetime import time
from selenium import webdriver
from settings import email, password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os.path
import random
from urllib.parse import urlparse


class BasePage(object):

    def __init__(self, url, driver, timeout=10):
        self.driver = driver
        self.url = url

    def get_relative_link(self):
        url = self.driver.current_url
        parsed_url = str(urlparse(url).path)
        return parsed_url




