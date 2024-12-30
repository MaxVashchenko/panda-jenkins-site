# Використовуємо офіційний Python-образ
FROM python:3.10-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файли до контейнера
COPY app.py /app

# Встановлюємо залежності
RUN pip install flask

# Відкриваємо порт
EXPOSE 5000

# Запускаємо додаток
CMD ["python", "app.py"]
