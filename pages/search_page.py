from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def search_for_book(self, book_title: str):
        """Выполняет поиск по названию книги и проверяет отображение результатов."""
        # Находим и очищаем поле поиска
        search_box = self.driver.find_element(
            By.CSS_SELECTOR, "input.header-search__input")
        search_box.clear()

        # Вводим название книги и нажимаем кнопку поиска
        search_box.send_keys(book_title)
        search_button = self.driver.find_element(
            By.CSS_SELECTOR, ".header-search__button")
        search_button.click()

        # Ожидание загрузки страницы с результатами
        WebDriverWait(
            self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "p.search-page__found-message")))

    def is_book_in_results(self, book_title: str) -> bool:
        """Проверяет, что книга с указанным названием отображается в результатах поиска."""
        # Ожидаем, что элементы результатов поиска загружены
        WebDriverWait(
            self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div.product-title__head")))

        # Получаем текст заголовков всех найденных книг
        results = self.driver.find_elements(
            By.CSS_SELECTOR, "div.product-title__head")
        result_texts = [result.text for result in results]

        # Выводим найденные результаты для отладки
        print("Найденные книги:", result_texts)

        # Проверяем, что искомая книга есть в списке найденных
        return any(book_title in result.text for result in results)

    def add_to_favorites(self):
        """Находит книгу 'Гарри Поттер и философский камень' и добавляет её в Избранное."""

        # Находим книгу по названию
        book_element = self.driver.find_element(
            By.CSS_SELECTOR,
            'a.product-card__title[title="Гарри Поттер и философский камень"]')
        book_element.click()

        # Находим кнопку 'Добавить в закладки' и кликаем по ней
        add_to_favorites_button = self.driver.find_element(
            By.CSS_SELECTOR, "button.product-offer-favorite")
        add_to_favorites_button.click()

    def is_product_in_favorites(self) -> bool:
        """Проверяет, что книга 'Гарри Поттер и философский камень' находится в Избранном."""
        favorites_page = self.driver.find_element(By.ID, "favorites")
        return "Гарри Поттер и философский камень" in favorites_page.text

    def return_empty_result(self):
        self.driver.find_element(
            By.CLASS_NAME,
            "catalog-empty-result__header").text

    def return_empty_result(self, book_title):
        """Выполняет поиск по названию книги и проверяет отображение результатов."""
        # Находим и очищаем поле поиска
        search_box = self.driver.find_element(By.CSS_SELECTOR, "input.header-search__input")
        search_box.clear()
        # Вводим название книги и нажимаем кнопку поиска
        search_box.send_keys(book_title)
        search_button = self.driver.find_element(By.CSS_SELECTOR, ".header-search__button")
        search_button.click()
        return self.driver.find_element(By.CLASS_NAME, "catalog-empty-result__header").text
