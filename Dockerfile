# Base Image
FROM python:3.11-slim

# Work Directory
WORKDIR /app

# Dependencies Install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Flask API Copy
COPY app/ .

# Flask API Run
CMD ["python", "app.py"]
