FROM python:3.11-slim


WORKDIR /app/test_project_docker


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


ENV PYTHONPATH=/app/test_project_docker


ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=1
ENV POSTGRES_DB=apple_store
ENV POSTGRES_HOST=apple_store
ENV POSTGRES_PORT=5432


CMD ["pytest", "app/tests"]
