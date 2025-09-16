# Базовый образ с Python и системными зависимостями
FROM python:3.11-slim

# Устанавливаем системные зависимости для Selenium и браузеров
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libx11-6 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    xdg-utils \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем браузеры и драйверы
RUN apt-get update && apt-get install -y \
    # Для ARM64 используем Chromium, для x86_64 - Google Chrome
    chromium \
    chromium-driver \
    firefox-esr \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем geckodriver для Firefox
RUN apt-get update && apt-get install -y wget && \
    GECKODRIVER_VERSION=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep -Po '"tag_name": "\K.*?(?=")') && \
    wget -O /tmp/geckodriver.tar.gz "https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VERSION}/geckodriver-${GECKODRIVER_VERSION}-linux-aarch64.tar.gz" && \
    tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin/ && \
    chmod +x /usr/local/bin/geckodriver && \
    rm /tmp/geckodriver.tar.gz && \
    rm -rf /var/lib/apt/lists/*

# Создаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем Python зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Создаем директории для отчетов
RUN mkdir -p /app/allure_results /app/pytest_reports

# Устанавливаем переменные окружения
ENV PYTHONPATH=/app
ENV DISPLAY=:99

# Создаем скрипт для запуска тестов с Xvfb
RUN echo '#!/bin/bash\n\
set -e\n\
\n\
# Запускаем виртуальный дисплей\n\
Xvfb :99 -screen 0 1920x1080x24 &\n\
XVFB_PID=$!\n\
\n\
# Ждем запуска Xvfb\n\
sleep 2\n\
\n\
# Функция для остановки Xvfb при выходе\n\
cleanup() {\n\
    kill $XVFB_PID 2>/dev/null || true\n\
}\n\
trap cleanup EXIT\n\
\n\
# Запускаем тесты\n\
exec "$@"\n\
' > /app/run_tests.sh && chmod +x /app/run_tests.sh

# Команда по умолчанию для запуска тестов
CMD ["/app/run_tests.sh", "pytest", "--browser=chrome", "--headless", "--env=dev", "-v", "--alluredir=/app/allure_results"]
