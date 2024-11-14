import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.search_page import SearchPage
from pages.cart_page import CartPage

base_url = " https://www.chitai-gorod.ru/ "


@pytest.fixture
def browser():
    driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.title("Тестирование поиска книг на сайте")
@allure.description("Этот тест проверяет, что пользователь может искать книги и получать корректные результаты.")
@allure.feature("Поиск книг")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_and_update_results(browser: WebDriver):
    search_page = SearchPage(browser)
    browser.get(base_url)
    with allure.step("Поиск книги 'Гарри Поттер'"):
        search_page.search_for_book("Гарри Поттер")
        assert search_page.is_book_in_results(
            "Гарри Поттер"), "Книга 'Гарри Поттер' не найдена в результатах поиска."


@allure.title("Тест на поиск несуществующей книги")
@allure.description("Проверка, что при поиске несуществующей книги выводится сообщение об отсутствии результатов.")
@allure.feature("Поиск книг")
@allure.severity(allure.severity_level.MINOR)
def test_search_non_existent_book(browser: WebDriver):
    search_page = SearchPage(browser)
    browser.get(base_url)
    with allure.step("Поиск несуществующей книги 'Книга, которой нет'"):
        assert search_page.return_empty_result(
            "fjvjnfjkvn") == "Похоже, у нас такого нет", "Найдены результаты для несуществующей книги."


@allure.title("Тестирование управления корзиной")
@allure.description("Этот тест проверяет, что пользователь может открыть корзину.")
@allure.feature("Управление корзиной")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_book(browser: WebDriver):
    cart_page = CartPage(browser)
    browser.get(base_url)
    with allure.step("Открыть корзину"):
        cart_page.open_cart()
        assert "Корзина" in browser.page_source, "Корзина не открылась."


@allure.title("Тестирование управления корзиной")
@allure.description("Этот тест проверяет, что пользователь открывает корзину, а там ничего нет ")
@allure.feature("Управление корзиной")
@allure.severity(allure.severity_level.NORMAL)
def test_delete_book(browser: WebDriver):
    cart_page = CartPage(browser)
    browser.get(base_url)
    with allure.step("Проверка пустой корзины"):
        assert cart_page.open_cart().strip() == "В корзине ничего нет"


@allure.title("Тестирование добавления книги 'Гарри Поттер и философский камень' в список желаемого")
@allure.description("Этот тест проверяет, что пользователь может добавить книгу 'Гарри Поттер и философский камень' в список желаемого без регистрации.")
@allure.feature("Список желаемого")
@allure.severity(allure.severity_level.NORMAL)
def test_add_harry_potter_to_wishlist(browser: WebDriver):
    search_page = SearchPage(browser)
    browser.get(base_url)
    with allure.step("Добавление книги 'Гарри Поттер и философский камень' в список желаемого"):
        assert search_page.add_to_favorites