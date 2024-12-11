# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file (if any)
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the aggregator service code
COPY . /app

# Expose the port (if needed)
EXPOSE 5004

# Command to run the service
CMD ["python", "aggregator_service.py"]
