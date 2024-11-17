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

    @allure.step("Добавление первой книги в корзину")
    def add_first_book_to_cart(self):
        driver = self.driver
        driver.set_window_size(1200, 800)
        driver.get("https://www.chitai-gorod.ru/")
    
        try:
            # Закрытие кнопки "Нет, спасибо" в всплывающем окне
            no_thanks_button = driver.find_element(By.CSS_SELECTOR, ".button.push-notification__no-button.white")
            no_thanks_button.click()
        except:
            pass  # Если кнопка не найдена, продолжаем

        try:
            # Закрытие центрального окна
            central_popup = driver.find_element(By.CSS_SELECTOR, ".popup-close-button-selector")
            central_popup.click()
        except:
            pass  # Если центрального окна нет, продолжаем

            #Находим первую книгу
        first_book = driver.find_element(By.CSS_SELECTOR, "article.product-card.slider__item-card")
        # Прокручиваем страницу до элемента, чтобы кнопка была видна
        driver.execute_script("arguments[0].scrollIntoView();", first_book)
        try:
            buy_button = first_book.find_element(By.CSS_SELECTOR, "button.product-card__button")
            buy_button.click()
        except Exception as e:
            # Если кнопка не найдена, делаем скриншот и выбрасываем ошибку
            driver.save_screenshot("screenshot.png")
            raise AssertionError("Кнопка 'Купить' не найдена или недоступна") from e
         # Получаем кнопку "Оформить"
        oformit_button = driver.find_element(By.CSS_SELECTOR, "div.bookmarks-catalog article:nth-child(3) .product-buttons .buttons span")
        oformit_button.click()

    @allure.step("Проверка, что книга добавлена в корзину")    
    def is_book_added_to_cart(self):
        cart_count = self.driver.find_element(By.CSS_SELECTOR, ".badge-notice.header-cart__badge")
        return cart_count.text == "1"
    
    @allure.step("Обновление количества книг в корзине")
    def update_quantity_in_cart(self, quantity):
        driver = self.driver
        driver.set_window_size(1200, 800)
        driver.get("https://www.chitai-gorod.ru/")
        quantity_button = self.driver.find_element(By.CSS_SELECTOR, ".button.product-quantity__button--right")
        quantity_button.click()

    @allure.step("Получение количества книг в корзине")
    def get_book_quantity(self):
        quantity_element = self.driver.find_element(By.CSS_SELECTOR, ".cart-item__counter .product-quantity")
        # Получаем значение количества
        return int(quantity_element.get_attribute("value"))
    
    @allure.step("Удаление книги из корзины")
    def remove_book_from_cart(self):
        #нажимаем на корзину 
        cart_icon = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/cart']"))
        )
        cart_icon.click()
        
        # кнопка "Удалить" нажата
        remove_button = self.driver.find_element(By.CSS_SELECTOR, ".button.cart-item__actions-button--delete")
        remove_button.click()

    def is_cart_empty(self):
        # Проверяем, что появилось сообщение об удалении товара
        success_message = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,".item-removed__description-title"))
        )
        # Проверяем текст сообщения
        return "Удалили товар из корзины." in success_message.text