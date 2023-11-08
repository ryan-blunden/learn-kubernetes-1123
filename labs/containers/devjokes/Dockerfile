FROM python:3-alpine

# These are set at build time and still exist at runtime
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --quiet --no-cache-dir --upgrade pip setuptools && \
    pip install --quiet --no-cache-dir -r requirements.txt

COPY src/ .

EXPOSE 8000

CMD ["gunicorn", "app:app", "--bind=0.0.0.0:8000"]