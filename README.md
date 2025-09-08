# Stelars Burgers: Автотесты

## Описание

Этот проект содержит автотесты для сайта Stellar Burgers с поддержкой разных окружений (DEV, STAGE)
и браузеров (chrome, firefox). В проекте реализовано минимум два тестовых пользователя для каждого окружения.

---

## Структура окружений и пользователей

- Окружения настраиваются в файле `config/environments.py`.
- Для каждого окружения определены пользователи (логин, пароль, email).
- Пример получения пользователя и окружения:

```python
from config.environments import get_env_config, get_user

env = get_env_config("DEV")
user = get_user(env.default_user)
```

---

## Запуск тестов

### 1. Выбор окружения

По умолчанию тесты используют DEV-окружение. Для смены окружения используйте опцию `--env`:

```bash
pytest --env=DEV
pytest --env=STAGE
```

### 2. Запуск в разных браузерах

По умолчанию используется Chrome. Для запуска в Firefox:

```bash
pytest --browser=chrome
pytest --browser=firefox
```

Можно комбинировать:

```bash
pytest --env=STAGE --browser=firefox
```

### 3. Пример запуска всех тестов

```bash
pytest
```

### 4. Запуск одного теста

```bash
pytest tests/test_registration.py::TestRegistration::test_registration
```

---

---

## 🐳 Запуск тестов в Docker

### Сборка образа
```bash
docker-compose build
```

### Основные команды запуска

#### 1. Запуск всех тестов на DEV в Chrome
```bash
docker-compose up stelars-tests
```

#### 2. Запуск тестов на STAGE
```bash
docker-compose up stelars-tests-stage
```

#### 3. Запуск тестов в Firefox
```bash
docker-compose up stelars-tests-firefox
```

#### 4. Запуск только smoke тестов
```bash
docker-compose up stelars-tests-smoke
```

#### 5. Запуск Allure сервера для отчетов
```bash
docker-compose up allure-server
```
Allure отчеты будут доступны по адресу: http://localhost:5050

### Кастомные команды

Для запуска тестов с кастомными параметрами:
```bash
docker-compose run --rm stelars-tests /app/run_tests.sh pytest -m regression --browser=chrome --env=dev -v
```

### Очистка ресурсов
```bash
# Остановить все контейнеры
docker-compose down

# Удалить образы
docker-compose down --rmi all

# Удалить volumes
docker-compose down -v
```

---

## 💻 Локальный запуск (без Docker)

### Требования
- Python 3.11+
- Google Chrome и/или Mozilla Firefox
- Все зависимости из requirements.txt

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Запуск тестов

#### 1. Выбор окружения
```bash
pytest --env=DEV
pytest --env=STAGE
```

#### 2. Запуск в разных браузерах
```bash
pytest --browser=chrome
pytest --browser=firefox
```

#### 3. Комбинированный запуск
```bash
pytest --env=STAGE --browser=firefox --headless
```

#### 4. Запуск конкретного теста
```bash
pytest tests/test_registration.py::TestRegistration::test_registration
```

#### 5. Запуск с маркерами
```bash
pytest -m smoke
pytest -m regression
```

---

## 📊 Отчеты

### Allure отчеты
```bash
# Генерация отчетов
pytest --alluredir=allure_results

# Просмотр отчетов
allure serve allure_results
```

### HTML отчеты
```bash
pytest --html=reports/report.html --self-contained-html
```

---

## 📁 Структура проекта

```
Stelars_burgers/
├── config/                 # Конфигурация окружений и пользователей
│   └── environments.py
├── data/                   # Данные для тестов
│   └── credentials.py
├── pages/                  # Page Object классы
│   ├── base_page.py
│   ├── registration.py
│   └── login_pages/
├── tests/                  # Тестовые сценарии
│   ├── test_registration.py
│   ├── test_sign_in.py
│   └── test_navigation.py
├── allure_results/         # Результаты Allure (создается автоматически)
├── pytest_reports/        # HTML отчеты (создается автоматически)
├── Dockerfile             # Docker образ для тестов
├── docker-compose.yml     # Оркестрация контейнеров
├── requirements.txt       # Python зависимости
└── conftest.py            # Pytest конфигурация и фикстуры
```

---

## ⚙️ Конфигурация

### Переменные окружения в Docker
- `PYTHONPATH=/app` - путь к модулям Python
- `DISPLAY=:99` - виртуальный дисплей для headless режима

### Настройка пользователей
Пользователи настраиваются в `config/environments.py`:
```python
USERS = {
    "dev_user1": UserCredentials("username", "password", "email@example.com"),
    "stage_user1": UserCredentials("username", "password", "email@example.com"),
}
```

---

## 🚀 Быстрый старт

1. **Клонируйте репозиторий**
2. **Docker подход (рекомендуется):**
   ```bash
   docker-compose up stelars-tests
   ```
3. **Локальный подход:**
   ```bash
   pip install -r requirements.txt
   pytest
   ```

---

## Примечания
- Для корректной работы параметров окружения и браузера убедитесь, что они поддерживаются в вашем conftest.py.
- Пользователи для тестов задаются в `config/environments.py`.
- Docker образ включает Chrome, Firefox и все необходимые зависимости.
- Виртуальный дисплей (Xvfb) используется для запуска браузеров в headless режиме в контейнере. 