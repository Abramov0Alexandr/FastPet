# Используем официальный базовый образ Python 3.11
FROM python:3.11-slim

# Устанавливаем зависимости для Poetry
RUN apt-get update && apt-get install -y \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Добавляем Poetry в PATH
ENV PATH="/root/.local/bin:${PATH}"

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем pyproject.toml и poetry.lock
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости
RUN poetry install --no-root --no-dev

# Копируем все файлы проекта
COPY . .

# Run the application.
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003", "--reload"]
