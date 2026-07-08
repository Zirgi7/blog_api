# Blog API

RESTful API для управления блогами (FastAPI + SQLAlchemy + SQLite).

---

## Требования

- Python 3.10+
- pip

---

## Установка и запуск

1. **Клонируйте/скопируйте** файлы проекта в папку `blog_api`.

2. **Создайте виртуальное окружение:**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt

4. **Запустите сервер:**
   ```bash
   uvicorn main:app --reload

Сервер будет доступен по адресу http://127.0.0.1:8000.

---

## Структура проекта

   ```
   blog_api/
   ├── main.py          # Точка входа
   ├── database.py      # Подключение к БД
   ├── models.py        # SQLAlchemy-модель
   ├── schemas.py       # Pydantic-схемы
   ├── routers/
   │   └── blogs.py     # Эндпоинты
   ├── requirements.txt
   └── README.md
   ```

---

## Эндпоинты

| Метод  | Эндпоинт            | Описание                               |
|--------|:--------------------|:---------------------------------------|
| GET    | /blogs              | Список блогов (фильтр ?published=true) |
| GET    | /blogs/{id}         | Получить блог по ID                    |
| POST   | /blogs              | Создать блог                           |
| PUT    | /blogs/{id}         | Обновить заголовок/описание            |
| PATCH  | /blogs/{id}/publish | Переключить статус публикации          |
| DELETE | /blogs/{id}         | Удалить блог (204 No Content)          |

