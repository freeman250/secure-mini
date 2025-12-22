FROM python:3.12-slim

WORKDIR /app

# Copy only application code into container
COPY application/ /app/

# Install dependencies
RUN pip install --no-cache-dir flask gunicorn

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
