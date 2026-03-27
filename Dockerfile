# Use an official Python environment
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /app

# Force unbuffered Python stdout/stderr so print() appears in Docker logs immediately
ENV PYTHONUNBUFFERED=1

# Copy sensor.py into the container
COPY sensor.py .

# Install Flask
RUN pip install --no-cache-dir flask

# Expose the port that the Flask app will run on
EXPOSE 5000

# Run the sensor.py script when the container starts
CMD ["python", "sensor.py"]