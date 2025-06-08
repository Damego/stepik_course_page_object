import math

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser: WebDriver, url: str, wait_timeout: float = 10) -> None:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(wait_timeout)

    def open(self):
        self.browser.get(self.url)
        
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, by: str, value: str):
        try:
            self.browser.find_element(by, value)
        except NoSuchElementException:
            return False
        return True
    
    def is_not_element_present(self, by: str, value: str, timeout: int = 4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((by, value)))
        except TimeoutException:
            return True
        return False
    
    def element_disappeared(self, by: str, value: str, timeout: int = 4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((by, value))) # type: ignore
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")