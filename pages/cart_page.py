from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    CART = (By.CSS_SELECTOR, "span.header-cart.sticky-header__controls-item")
    QUANTITY_BUTTON = (By.CSS_SELECTOR, "button.product-quantity__button.product-quantity__button--right") 
    DELETE_BUTTON = (By.CSS_SELECTOR, "button.cart-item__actions-button.cart-item__actions-button--delete.light-blue") 
    BUY_BUTTON = (By.CSS_SELECTOR, "div.button.action-button.blue")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "div.button.action-button.blue.action-button--in-cart")

    def open_cart(self):
        """Открывает корзину."""
        cart_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART)
        )
        cart_icon.click()

    def add_to_cart(self):
        """Добавляет товар в корзину."""
        buy_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BUY_BUTTON)
        )
        buy_button.click()

        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_button.click()

    def increase_quantity(self):
        """Увеличивает количество товара."""
        increase_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.QUANTITY_BUTTON)
        )
        increase_button.click()

    def remove_item(self):
        """Удаляет товар из корзины."""
        delete_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.DELETE_BUTTON)
        )
        delete_button.click()

    def is_cart_empty(self) -> bool:
        """Проверяет, что корзина пуста."""
        return "Корзина пуста" in self.driver.page_source
