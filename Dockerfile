# Use a lightweight Python base image
FROM python:3.10-slim

# Install OS dependencies
RUN apt-get update && apt-get install -y \
    libgl1 libglib2.0-0 \
    poppler-utils tesseract-ocr \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
