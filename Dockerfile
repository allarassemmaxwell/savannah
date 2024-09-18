# Use the official Python image from the Docker Hub
# FROM python:3.13.0b4-slim
FROM python:3.12-slim


# Set the working directory in the container
WORKDIR /app

# Install PostgreSQL development files and other required packages
RUN apt-get update && \
    apt-get install -y postgresql-server-dev-all gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Expose port 8000 for Gunicorn
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]
