import pytest
import allure
from pages.search_page import SearchPage
from pages.catalog_page import CatalogPage
from pages.cart_page import CartPage

@allure.feature("UI Tests")
@pytest.mark.ui
def test_search_and_update_results(driver, base_url):
    driver.get(base_url)
    search_page = SearchPage(driver)

    with allure.step("Поиск книги по названию"):
        search_page.search_for_book("Гарри Поттер")
        assert search_page.is_book_in_results("Гарри Поттер")

    with allure.step("Обновление результатов поиска"):
        search_page.search_for_book("Властелин Колец")
        assert search_page.is_book_in_results("Властелин Колец")

@allure.feature("UI Tests")
@pytest.mark.ui
def test_catalog_and_select_product(driver, base_url):
    driver.get(base_url)
    catalog_page = CatalogPage(driver)

    with allure.step("Открытие каталога"):
        catalog_page.open_catalog()

    with allure.step("Выбор категории 'Манга'"):
        catalog_page.select_category("Манга")
        assert catalog_page.is_category_opened("Манга")

@pytest.mark.ui
@allure.feature("UI Tests")
def test_add_and_modify_cart(driver, base_url):
    driver.get(base_url)
    cart_page = CartPage(driver)

    with allure.step("Добавление книги в корзину"):
        cart_page.add_to_cart() 
        cart_page.open_cart()
        assert "Корзина" in driver.page_source

    with allure.step("Изменение количества товара в корзине"):
        cart_page.increase_quantity()
        assert "5" in driver.page_source

    with allure.step("Удаление товара из корзины"):
        cart_page.remove_item()
        assert cart_page.is_cart_empty()