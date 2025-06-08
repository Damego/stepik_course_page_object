from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def added_product_equals_to_product(self):
        page_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        page_product_name = page_product.text.strip()
        
        basket_product = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE)
        basket_product_name = basket_product.text.strip()
        
        assert page_product_name == basket_product_name
        
    def basket_price_equals_to_product_price(self):
        product_price_elem = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price = product_price_elem.text.strip()
        
        basket_price_elem = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE)
        basket_price = basket_price_elem.text.strip()
        
        assert product_price == basket_price
        
        