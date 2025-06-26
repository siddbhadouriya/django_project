Django Project with DRF, Celery, and Telegram Bot

This project showcases backend development skills using Django Rest Framework (DRF), Celery, and Telegram Bot integration.
✅ Features

Django REST API with Token Authentication

Public and Protected endpoints

User Registration with Background Email (via Celery & Redis)

Telegram Bot Integration to collect usernames

Production-ready configuration using .env variables
Tech Stack

Python 3.10+

Django 5.x

Django REST Framework

Redis + Celery

PostgreSQL (or SQLite for dev)

Telegram Bot API

python-decouple

2. Create a Virtual Environment
3. python -m venv env
source env/bin/activate  # or env\Scripts\activate for Windows

4. Create and Configure .env file

Create a file named .env in the root folder and add the following:
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

REDIS_URL=redis://localhost:6379/0
TELEGRAM_TOKEN=your-telegram-bot-token
