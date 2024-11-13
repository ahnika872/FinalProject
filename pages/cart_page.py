import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Добавить товар в корзину")
    def add_to_cart(self) -> None:

        """Добавляет товар в корзину."""

        buy_button = self.driver.find_element(By.CSS_SELECTOR, "div.button.action-button.blue") 
        buy_button.click()

    @allure.step("Открыть корзину")
    def open_cart(self) -> None:

        """Открывает корзину."""

        cart_icon =  WebDriverWait(self.driver, 20).until( 
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/cart']")) 
        ) 
        cart_icon.click()
  
    @allure.step("Увеличить количество товара до {quantity}")
    def increase_quantity(self, target_quantity: int = 2) -> None:

        """Увеличивает количество товара до заданного значения.
        
        :param quantity: Целевое количество товара
        """

        current_quantity = int(self.driver.find_element(By.CSS_SELECTOR, "input.product-quantity__input").get_attribute("value"))
        for _ in range(target_quantity - current_quantity):
            increase_button = self.driver.find_element(By.CSS_SELECTOR, "button.product-quantity__button--right")
            increase_button.click()

    @allure.step("Удалить товар из корзины")
    def remove_item(self) -> None:

        """Удаляет товар из корзины."""

        delete_button = self.driver.find_element(By.CSS_SELECTOR, "button.cart-item__actions-button--delete")
        delete_button.click()

    @allure.step("Проверить, что корзина пуста")
    def is_cart_empty(self) -> bool:
        
        """Проверяет, что корзина пуста.
        
        :return: True, если корзина пуста, иначе False
        """
        try:
            # Проверяем наличие элемента с сообщением о пустой корзине
            empty_message = self.driver.find_element(By.CSS_SELECTOR, "div.empty-title")
            return empty_message.is_displayed()
        except:
            return False
