from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CatalogPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    CATALOG_BUTTON = (By.CSS_SELECTOR, "button.catalog__button")
    CATEGORY_LINK = (By.PARTIAL_LINK_TEXT, "Манга") 
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.product-title__head")

    def open_catalog(self):
        """Открывает каталог."""
        catalog_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CATALOG_BUTTON)
        )
        catalog_button.click()

    def select_category(self, category_name: str = "Манга"):
        """Выбирает категорию товаров по её названию."""
        category_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, category_name))
        )
        category_link.click()

    def is_category_opened(self) -> bool:
        """Проверяет, что после выбора категории появились товары."""
        # Проверяем наличие хотя бы одного товара на странице.
        products = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.PRODUCT_TITLE)
        )
        return len(products) > 0

    def get_product_titles(self) -> list:
        """Возвращает список названий товаров, отображаемых на странице."""
        products = self.driver.find_elements(*self.PRODUCT_TITLE)
        return [product.text for product in products]