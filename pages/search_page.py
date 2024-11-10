from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    SEARCH_BOX = (By.CSS_SELECTOR, "input.header-search__input")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "div.products-list") 
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.header-search__button")

    def search_for_book(self, book_title: str):
        """Выполняет поиск по названию книги."""
        search_box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        )
        search_box.clear()
        search_box.send_keys(book_title)

        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )
        search_button.click()

    def is_book_in_results(self, book_title: str) -> bool:
        """Проверяет, что искомая книга есть в результатах поиска."""
        results = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.SEARCH_RESULTS)
        )
        return any(book_title in result.text for result in results)