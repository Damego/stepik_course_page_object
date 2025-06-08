from selenium.webdriver.remote.webdriver import WebDriver

from ..pages import MainPage, LoginPage

MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser: WebDriver):
    page = MainPage(browser, MAIN_PAGE_URL)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

    