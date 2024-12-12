# Event Manager

## Опис

Event Manager — це API для керування заходами. З його допомогою можна створювати, оновлювати, видаляти події та реєструвати користувачів на заходи.

## Старт

1. Клонуйте репозиторій:
    ```bash
    git clone https://github.com/your-username/event-manager.git
    cd event-manager
    ```

2. Встановить залежності:
    ```bash
    pip install -r requirements.txt
    ```

3. Запустіть сервер:
    ```bash
    python manage.py runserver
    ```

## API

- `POST /api/register/` — Реєстрація нового користувача
- `POST /api/events/` — Створення нової події
- `GET /api/events/` — Отримати список подій
- `POST /api/register_event/` — Зареєструватись на подію

## Docker

1. Для запуску Docker
    ```bash
    docker-compose up --build
    ```

2. Після цього сервер буде доступний за адресою `http://localhost:8000/api/events`.
3. Фільтрацію можна робити за id 'http://localhost:8000/api/events,title/1or2', title, location, date http://localhost:8000/api/events?title=
4. Для того, щоб працювала розсилка повідомлень, потрібно в settings.py вказати пошту та пароль з якої буде надіслано лист