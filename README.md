# Savannah


### Build Status
![Build Status](https://github.com/allarassemmaxwell/savannah/actions/workflows/ci_cd.yml/badge.svg)


## Overview

Savannah is a Django application designed for managing customers and orders, including features for user registration and SMS notifications upon order creation. The app is built using Django REST Framework and leverages PostgreSQL as its database. It also uses Africa's Talking SDK for SMS functionality.

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

- Docker
- Docker Compose
- Python 3.12 or higher
- PostgreSQL
- Africa's Talking account (for SMS functionality)

### Clone the Repository

```bash
git clone https://github.com/allarassemmaxwell/savannah.git
cd savannah
```

## Set Up Environment Variables

Create a `.env` file in the root directory of your project and define the following environment variables:

```bash
SECRET_KEY=your_secret_key
POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
AFRICAS_TALKING_USERNAME=your_africas_talking_username
AFRICAS_TALKING_API_KEY=your_africas_talking_api_key
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_APPLICATION_NAME=your_application_name
AWS_ENVIRONMENT_NAME=your_environment_name
AWS_REGION=your_aws_region
```

## Build and Run the Application

Build the Docker containers:

```bash
docker compose build
docker compose up
```

## Create a Superuser

To create an admin user, run the following command:

```bash
docker compose exec web python manage.py createsuperuser
```

## API Endpoints

- `POST /api/signup/` - User registration.
- `POST /api/token/` - Obtain JWT token.
- `POST /api/token/refresh/` - Refresh JWT token.
- `POST /api/customers/` - Create a new customer.
- `POST /api/orders/` - Place a new order.

## Running Tests With Coverage

To run the tests with coverage, use the following command:

```bash
docker compose exec web coverage run manage.py test
```

## CI/CD with GitHub Actions

This project includes a CI/CD setup using GitHub Actions. Linting and testing are performed on every push and pull request to the main branch. Additionally, the application is automatically deployed to AWS Elastic Beanstalk upon successful tests. Ensure that your `.github/workflows/ci_cd.yml` file is configured to include your linting, testing, and deployment steps.

The application can be accessed at the following URL: [http://savanah.us-east-1.elasticbeanstalk.com](http://savanah.us-east-1.elasticbeanstalk.com).


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django
- Django REST Framework
- Africa's Talking


## Deployment

The application is deployed on AWS Elastic Beanstalk and can be accessed at the following URL: http://savanah.us-east-1.elasticbeanstalk.com.
