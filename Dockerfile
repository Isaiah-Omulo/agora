FROM python:3.10-slim

WORKDIR /app

COPY src ./src
COPY docker ./docker

RUN pip install --no-cache-dir \
    flask \
    pycryptodome

ENV PYTHONUNBUFFERED=1

CMD ["python", "docker/app.py"]
