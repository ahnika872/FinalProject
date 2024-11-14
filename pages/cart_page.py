import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Открыть корзину")
    def open_cart(self) -> str:
        """Открывает корзину."""

        cart_icon = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/cart']"))
        )
        cart_icon.click()
        return self.driver.find_element(By.CSS_SELECTOR, ".empty-title").text

    @allure.step("Проверить, что корзина пуста")
    def is_cart_empty(self) -> bool:
        """Проверяет, что корзина пуста.

        :return: True, если корзина пуста, иначе False
        """
        try:
            # Проверяем наличие элемента с сообщением о пустой корзине
            empty_message = self.driver.find_element(
                By.CSS_SELECTOR, "div.empty-title")
            return empty_message.is_displayed()
        except BaseException:
            return False
