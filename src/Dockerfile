
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY datacenter_app.py .

CMD ["python", "datacenter_app.py"]
