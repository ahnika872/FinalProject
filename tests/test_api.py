import requests
import allure
import pytest

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjk2MzM1NiwiaWF0IjoxNzMxMjczOTYxLCJleHAiOjE3MzEyNzc1NjEsInR5cGUiOjIwfQ.P2I56iE6FePheEJoVVx9I9rTWgaknXbv7ScZU2V5-uM"
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
        response = requests.post(f"{BASE_API_URL}/product", json=payload, headers=HEADERS)
        assert response.status_code == 200

@allure.feature("API Tests")
@pytest.mark.api
def test_update_product_quantity():
    with allure.step("Изменение количества товара в корзине"):
        payload = {"id":153459253, "quantity": 2}
        response = requests.put(f"{BASE_API_URL}", json=payload, headers=HEADERS)
        print(response.text) 
        assert response.status_code == 200

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
        response = requests.delete(f"{BASE_API_URL}/product/153459253", headers=HEADERS)
        print(response.text)
        assert response.status_code == 204

@allure.feature("API Tests")
@pytest.mark.api
def test_get_cart_total():
    with allure.step("Получение общей стоимости товаров в корзине"):
        response = requests.get(f"{BASE_API_URL}/total", headers=HEADERS)
        assert response.status_code == 200
        total_price = response.json().get("total")
        expected_price = 558 
        assert total_price == expected_price, f"Ожидалось: {expected_price}, но получено: {total_price}"