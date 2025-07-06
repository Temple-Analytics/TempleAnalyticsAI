# Stage 1: install dependencies
FROM python:3.10-slim AS builder

WORKDIR /app

# Копіюємо лише залежності для кешування
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: збірка фінального образу
FROM python:3.10-slim

WORKDIR /app

# Копіюємо інстальовані залежності з builder
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Копіюємо код
COPY src/ /app/src/
COPY .env.example .env

# Відкриваємо порт API
EXPOSE 8000

# Запуск FastAPI через Uvicorn
CMD ["uvicorn", "temple_analytics.api_server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
