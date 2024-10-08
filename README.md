# Brendwall_TestTask

## Программист Python / Django. Тестовое задание для собеседования в компанию "Brendwall"

Тестовое задание: API для продуктов и работа с фронтендом

Временные адреса доступа:
https://vc.mishazx.ru/
https://brendwall.mishazx.ru/

**Описание**:
Необходимо создать небольшое Django-приложение, которое будет состоять из двух частей:

1. API для работы с продуктами (создание и получение списка).
2. Страница на HTML с использованием JavaScript для отправки данных на API и отображения продуктов.

**Требования**:

1. API (Django):

- [x] Создайте модель продукта с полями: название (строка), описание (текст), цена (десятичное число).
- [x] Реализуйте API с двумя конечными точками:
- [x] POST-запрос для создания продукта (принимает JSON с данными: название, описание, цена).
- [x] GET-запрос для получения списка всех продуктов в формате JSON.
- [x] При создании продукта должны выполняться простые проверки (например, цена должна быть положительным числом, название — не пустым).

2. Фронтенд (HTML + JavaScript):

- [x] Создайте простую HTML-страницу с формой для добавления нового продукта (поля: - название, описание, цена) и кнопкой "Отправить".
- [x] Реализуйте логику с помощью JavaScript, которая отправляет данные формы на API с использованием AJAX (Fetch API).
- [x] После успешного добавления продукта обновите список продуктов на странице, сделав GET-запрос к API для получения всех продуктов и отобразив их в виде таблицы.