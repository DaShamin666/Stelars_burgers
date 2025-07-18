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

## Требования
- Python 3.12+
- Google Chrome и/или Mozilla Firefox
- Все зависимости из requirements.txt

---

## Примечания
- Для корректной работы параметров окружения и браузера убедитесь, что они поддерживаются в вашем conftest.py.
- Пользователи для тестов задаются в `config/environments.py`.
- Для Allure-отчёта используйте:
  ```bash
  pytest --alluredir=allure_results
  allure serve allure_results
  ``` 