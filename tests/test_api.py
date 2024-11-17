import requests
import allure
import pytest

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjk2MzM1NiwiaWF0IjoxNzMxNTczNzY1LCJleHAiOjE3MzE1NzczNjUsInR5cGUiOjIwfQ.0gM6PecIS-WUVk4l83Ty1Na7NjpJTH_V6u_12QBYcNg"
BASE_API_URL = "https://web-gate.chitai-gorod.ru/api/v1/cart"

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}


@allure.feature("API Tests")
@pytest.mark.api
def test_add_product_to_cart():
    with allure.step("Добавление товара в корзину"):
        payload = {"id": 2651550}
        response = requests.post(
            f"{BASE_API_URL}/product",
            json=payload,
            headers=HEADERS)
        assert response.status_code == 200


@allure.feature("API Tests")
@pytest.mark.api
def test_update_product_quantity():
    with allure.step("Изменение количества товара в корзине"):
        payload = [{"id": 153459253, "quantity": 2}]
        response = requests.post(
            f"{BASE_API_URL}/product",
            json={
                "id": 2651550},
            headers=HEADERS)
        response = requests.put(
            f"{BASE_API_URL}",
            json=payload,
            headers=HEADERS)
        assert response.status_code == 200, (f"Ошибка: {response.status_code}, ответ: {response.text}")


@allure.feature("API Tests")
@pytest.mark.api
def test_view_cart():
    with allure.step("Просмотр содержимого корзины"):
        response = requests.get(BASE_API_URL, headers=HEADERS)
        assert response.status_code == 200


@allure.feature("API Tests")
@pytest.mark.api
def test_remove_product_from_cart():
    with allure.step("Удаление товара из корзины"):
        response = requests.post(
            f"{BASE_API_URL}/product",
            json={
                "id": 2651550},
            headers=HEADERS)
        response = requests.delete(
            f"{BASE_API_URL}/product/153459253",
            headers=HEADERS)
        print(response.text)
        assert response.status_code == 204


@allure.feature("API Tests")
@pytest.mark.api
def test_get_cart_total():
    with allure.step("Получение общей стоимости товаров в корзине"):
        response = requests.post(
            f"{BASE_API_URL}/product",
            json={
                "id": 2651550},
            headers=HEADERS)
        response = requests.put(f"{BASE_API_URL}", json=[
                                {"id": 153459253, "quantity": 2}], headers=HEADERS)
        response = requests.get(f"{BASE_API_URL}", headers=HEADERS)
        assert response.status_code == 200
        # Извлечение данных о товарах в корзине
        cart_items = response.json().get("products", [])
        # Проверка, что в корзине есть товары
        assert len(cart_items) > 0
        # Подсчет общего количества товаров
        total_quantity = sum(item["quantity"] for item in cart_items)
        assert total_quantity > 0, "Общее количество товаров должно быть больше нуля"
        # Проверка общей стоимости
        total_price = response.json().get("cost")  # Общая стоимость
        assert total_price > 0, "Общая стоимость должна быть больше нуля"
        # Дополнительные проверки на структуру данных
        for item in cart_items:
            assert "id" in item, "Отсутствует ID товара"
            assert "quantity" in item, "Отсутствует количество товара"
            assert item["quantity"] > 0, "Количество товара должно быть больше нуля"
