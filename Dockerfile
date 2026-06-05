FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Hugging Face Spaces run on port 7860 by default
EXPOSE 7860

ENV PORT=7860
ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
