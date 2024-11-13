import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.search_page import SearchPage
from catalog_page import CatalogPage
from pages.cart_page import CartPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@allure.title("Тестирование поиска книг на сайте")
@allure.description("Этот тест проверяет, что пользователь может искать книги и получать корректные результаты.")
@allure.feature("Поиск книг")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_and_update_results(browser, base_url):
    search_page = SearchPage(browser)
    browser.get(base_url)

    with allure.step("Поиск книги 'Гарри Поттер'"):
        search_page.search_for_book("Гарри Поттер")
        assert search_page.is_book_in_results("Гарри Поттер"), "Книга 'Гарри Поттер' не найдена в результатах поиска."

@allure.title("Тестирование управления корзиной")
@allure.description("Этот тест проверяет, что пользователь может добавлять, изменять количество и удалять товары из корзины.")
@allure.feature("Управление корзиной")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_book(browser, base_url):
    cart_page = CartPage(browser)
    browser.get(base_url)

    with allure.step("Добавление книги в корзину"):
        search_page = SearchPage(browser)
        search_page.search_for_book("Гарри Поттер")
        cart_page.add_to_cart()
        cart_page.open_cart()
        assert "Корзина" in browser.page_source, "Корзина не открылась."


@allure.title("Тестирование управления корзиной")
@allure.description("Этот тест проверяет, что пользователь может добавлять, изменять количество ")
@allure.feature("Управление корзиной")
@allure.severity(allure.severity_level.CRITICAL)
def test_quantity_book(browser, base_url):
    cart_page = CartPage(browser)
    browser.get(base_url)

    with allure.step("Изменение количества товара в корзине"):
        # cart_page.add_to_cart()
        cart_page.open_cart()
        cart_page.increase_quantity(2)
        assert "2" in browser.page_source, "Количество товара в корзине не увеличилось."


@allure.title("Тестирование управления корзиной")
@allure.description("Этот тест проверяет, что пользователь может добавлять, изменять количество ")
@allure.feature("Управление корзиной")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_book(browser, base_url):
    cart_page = CartPage(browser)
    browser.get(base_url)

    with allure.step("Удаление товара из корзины"):
        cart_page.add_to_cart()
        cart_page.open_cart()
        cart_page.remove_item()
        assert cart_page.is_cart_empty(), "Корзина не пуста."



@allure.title("Тестирование добавления книги 'Гарри Поттер и философский камень' в список желаемого")
@allure.description("Этот тест проверяет, что пользователь не может добавить книгу 'Гарри Поттер и философский камень' в список желаемого без регистрации.")
@allure.feature("Список желаемого")
@allure.severity(allure.severity_level.NORMAL)
def test_add_harry_potter_to_wishlist(browser, base_url):
    search_page = SearchPage(browser)
    browser.get(base_url)

    with allure.step("Добавление книги 'Гарри Поттер и философский камень' в список желаемого"):
        assert search_page.add_to_favorites