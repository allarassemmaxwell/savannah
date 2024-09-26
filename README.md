# MainApp

## Overview

MainApp is a Django application designed for managing customers and orders, including features for user registration and SMS notifications upon order creation. The app is built using Django REST Framework and leverages PostgreSQL as its database. It also uses Africa's Talking SDK for SMS functionality.

## Features

- User registration with JWT authentication.
- Create and manage customer data.
- Place orders and send SMS notifications to customers.
- Static and media file handling.

## Technologies Used

- Django
- Django REST Framework
- PostgreSQL
- Gunicorn
- Nginx
- Docker
- Africa's Talking API

## Getting Started

### Prerequisites

Make sure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)
- Python 3.12 or higher
- PostgreSQL
- Africa's Talking account (for SMS functionality)

### Clone the Repository

Set Up Environment Variables
Create a .env file in the root directory of your project and define the following environment variables:
SECRET_KEY=your_secret_key
POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
AFRICAS_TALKING_USERNAME=your_africas_talking_username
AFRICAS_TALKING_API_KEY=your_africas_talking_api_key

Build and Run the Application
Build the Docker containers:
docker-compose build
