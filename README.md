## Дипломный проект. Задание 3: UI-тесты
<hr>

## Студент: Комиссарова Надежда

## <h>Когорта: #27</h>
<hr>

## <h>Project: Stellar Burgers</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты:</h>

> pytest tests

### <h>3. Посмотреть отчет по прогону allure</h>

> allure serve allure_results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла             | Содержание файла                            |
|----------------------------|---------------------------------------------|
| Tests dir                  | Директория с тестами                        |
| test_main_functionality.py | Тесты на проверку основной функциональности |
| test_order_feed.py         | Тесты на раздел "Лента заказов"             |
| conftest.py                | Фикстуры                                    |
| helpers.py                 | Хэлпер для тела запросов                    |
| data.py                    | Файл с данными пользователя                 |
| curl.py                    | Файл с URL и body запросов                  |
| Locators dir               | Директория с локаторами                     |
| Page_objects dir           | Директория с классами страниц               |
| requirements.txt           | Файл с зависимостями                        |
| allure_results.dir         | Папка с отчетами Allure                     |