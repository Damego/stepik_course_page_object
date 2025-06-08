from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, browser: WebDriver, url: str, wait_timeout: float = 10) -> None:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(wait_timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by: str, value: str):
        try:
            self.browser.find_element(by, value)
        except NoSuchElementException:
            return False
        return True
