FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy source code
COPY src ./src
COPY docker ./docker

# Install dependencies
RUN pip install --no-cache-dir flask pycryptodome

# Set environment
ENV PYTHONUNBUFFERED=1

# Set PYTHONPATH so Python can find src/
ENV PYTHONPATH=/app

# Run app
CMD ["python", "docker/app.py"]
