# FinalProject
Тут хранится финальное задание по Тестированию 
# Проект тестирования сайта "Читай-город"

## Описание
Проект автоматизирует UI- и API-тесты для сайта "Читай-город". 

Основные сценарии:
**UI-тесты**
## cart_page.py 
1. Открытие корзины
Цель: Убедиться, что пользователь может открыть корзину.
Шаги: 
- Перейти на страницу корзины.
- Проверить, что отображается сообщение о пустой корзине.
Ожидаемый результат: Корзина открыта, и отображается сообщение о пустоте.
2. Проверка, что корзина пуста
Цель: Убедиться, что корзина действительно пуста.
Шаги: 
- Открыть корзину.
- Проверить наличие сообщения о пустой корзине.
Ожидаемый результат: Корзина пуста (отображается соответствующее сообщение).
3. Добавление первой книги в корзину
Цель: Убедиться, что пользователь может добавить книгу в корзину.
Шаги: 
- Перейти на главную страницу.
- Закрыть всплывающее окно (если отображается).
- Найти первую книгу и нажать кнопку «Купить».
- Перейти к оформлению.
Ожидаемый результат: Книга добавлена в корзину.
4. Проверка, что книга добавлена в корзину
Цель: Убедиться, что добавленная книга отображается в корзине.
Шаги: 
- Открыть корзину.
- Проверить количество книг в корзине.
Ожидаемый результат: Количество книг равно 1.
5. Обновление количества книг в корзине
Цель: Убедиться, что пользователь может обновить количество книг в корзине.
Шаги: 
- Открыть корзину.
- Изменить количество книг (например, увеличить).
Ожидаемый результат: Количество книг обновлено.
6. Получение количества книг в корзине
Цель: Убедиться, что пользователь может получить текущее количество книг в корзине.
Шаги:
- Открыть корзину.
- Получить и вернуть количество книг.
Ожидаемый результат: Возвращается корректное количество книг.
7. Удаление книги из корзины
Цель: Убедиться, что пользователь может удалить книгу из корзины.
Шаги:
- Открыть корзину.
- Нажать кнопку «Удалить» для книги.
Ожидаемый результат: Книга удалена из корзины.
8. Проверка, что корзина пуста после удаления
Цель: Убедиться, что корзина пуста после удаления книги.
Шаги:
- Удалить книгу из корзины.
- Проверить наличие сообщения "Удалили товар из корзины."
Ожидаемый результат: Удалили товар из корзины.

## search_page.py
1. Поиск книги по названию
Цель: Убедиться, что пользователь может выполнить поиск книги по её названию.
Шаги:
- Ввести название книги в поле поиска.
- Нажать кнопку поиска.
- Ожидать загрузки страницы с результатами.
Ожидаемый результат: Результаты поиска загружены и отображаются.
2. Проверка наличия книги в результатах поиска
Цель: Убедиться, что искомая книга отображается в результатах поиска.
Шаги:
- Выполнить поиск книги по её названию.
- Проверить, что название книги присутствует в результатах.
Ожидаемый результат: Книга с указанным названием отображается среди найденных результатов.
3. Добавление книги в Избранное
Цель: Убедиться, что пользователь может добавить книгу в Избранное.
Шаги:
- Выполнить поиск книги "Гарри Поттер и философский камень".
- Перейти на страницу книги.
- Нажать кнопку "Добавить в закладки".
Ожидаемый результат: Книга успешно добавлена в Избранное.
4. Проверка наличия книги в Избранном
Цель: Убедиться, что добавленная книга отображается в Избранном.
Шаги:
- Перейти на страницу Избранного.
- Проверить наличие книги "Гарри Поттер и философский камень".
Ожидаемый результат: Книга отображается в списке Избранного.
5. Проверка пустого результата поиска
Цель: Убедиться, что система корректно обрабатывает случаи, когда книга не найдена.
Шаги:
- Выполнить поиск книги с несуществующим названием.
- Проверить сообщение о пустом результате.
Ожидаемый результат: Отображается сообщение о том, что результаты поиска пусты.
6. Проверка обработки пустого результата поиска
Цель: Убедиться, что система корректно обрабатывает запросы на поиск книг, когда они не существуют.
Шаги:
- Выполнить поиск по несуществующему названию книги.
- Проверить, что на странице отображается сообщение о том, что результаты поиска пусты.
Ожидаемый результат: Отображается сообщение о том, что книга не найдена.

**API-тесты**
- Работа корзины.
- Изменение кол-ва товаров.
- Получение общей стоимости.

Тесты разработаны с использованием **Selenium**, **Pytest** и **Allure** для генерации подробных отчетов.

## Структура проекта
├── pages/                  # Локаторы и методы для работы со страницами сайта
│   ├── search_page.py      # Логика взаимодействия со страницей поиска
│   └── cart_page.py        # Логика взаимодействия с корзиной
├── tests/                  # Тесты
│   ├── test_api.py         # API-тесты
│   └── test_ui.py          # UI-тесты
├── requirements.txt        # Список зависимостей
└── README.md               # Документация



## Установка
1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/ahnika872/FinalProject.git
   cd FinalProject

## Установите зависимости
pip install -r requirements.txt

## Запуск UI-тестов
pytest tests/test_ui.py --alluredir=allure-results

## Запуск API-тестов
pytest tests/test_api.py --alluredir=allure-results

## Генерация отчета Allure
allure serve allure-results

## Используемые библиотеки
pytest — фреймворк для тестирования
selenium — для автоматизации UI тестов
requests — для отправки HTTP-запросов
allure-pytest — для создания отчетов
webdriver-manager — для управления драйверами браузеров

## Описание тестов

** API тесты (tests/test_api.py) **

1.	test_add_product_to_cart
Проверяет добавление товара в корзину через API.
2.	test_update_product_quantity
Проверяет изменение количества товара в корзине.
3.	test_view_cart
Проверяет получение содержимого корзины.
4.	test_remove_product_from_cart
Проверяет удаление товара из корзины.
5.	test_get_cart_total
Проверяет расчет общей стоимости товаров в корзине.

** UI тесты (tests/test_ui.py) **

1.	test_search_and_update_results
Проверяет поиск книги “Гарри Поттер” на сайте.
2.	test_search_non_existent_book
Проверяет, что поиск несуществующей книги возвращает сообщение об отсутствии результатов.
3.	test_add_book
Проверяет возможность открыть корзину.
4.	test_delete_book
Проверяет, что корзина пуста.
5.	test_add_harry_potter_to_wishlist
Проверяет добавление книги в список желаемого.
