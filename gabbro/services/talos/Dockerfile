# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy script to container
COPY app.py .

# Install dependencies
RUN pip install --no-cache-dir flask

# Expose port for Flask
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
