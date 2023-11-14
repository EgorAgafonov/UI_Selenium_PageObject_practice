from urllib.parse import urlparse
from settings import screenshots_folder


class BasePage(object):

    driver = None

    def __init__(self, driver, url, timeout=15):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def refresh_page(self):
        self.driver.refresh()

    def make_screenshot(self, file_path=screenshots_folder):
        self.driver.save_screenshot(file_path)

