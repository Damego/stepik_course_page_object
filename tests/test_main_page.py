from selenium.webdriver.remote.webdriver import WebDriver

from ..pages import MainPage, LoginPage, BasketPage

MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser: WebDriver):
    page = MainPage(browser, MAIN_PAGE_URL)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser: WebDriver):
    page = MainPage(browser, MAIN_PAGE_URL)
    page.open()
    page.go_to_basket_page()
    
    busket_page = BasketPage(browser, browser.current_url)
    busket_page.basket_is_empty()
    busket_page.has_basket_is_empty_text()
