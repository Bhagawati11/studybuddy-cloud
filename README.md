# StudyBuddy – Cloud Deployed Django Learning Platform

## Overview

StudyBuddy is a web-based collaborative learning platform where users can create study rooms, share resources, write blogs, and interact with other learners.

This project demonstrates a **full-stack web application deployed on AWS cloud infrastructure**, integrating Django, Nginx, Gunicorn, AWS EC2, and Amazon S3.

The system allows users to:

* Register and authenticate
* Join or create study rooms
* Upload and share resources
* Write and view blogs
* Upload profile avatars
* Store media files in cloud storage (AWS S3)

The goal of this project is to demonstrate **modern backend deployment architecture and cloud integration**.

---

# Project Features

### User Authentication

* User registration
* Login / logout
* User profile management
* Avatar upload

### Study Rooms

* Create rooms for discussion
* Join existing rooms
* Real-time conversation threads

### Blog System

* Create blogs
* View blog posts
* Upload blog images
* Rich content support

### Resource Sharing

* Upload study materials
* Share external links
* Download files

### Cloud Media Storage

* All uploaded files stored in **Amazon S3**
* Scalable and secure file storage

---

# Technology Stack

## Frontend

* HTML
* CSS
* JavaScript
* Django Template Engine

Static assets are served via **Nginx** in production.

---

## Backend

* Python
* Django 3.2
* Django ORM
* Django Authentication System

Django handles:

* Routing
* Authentication
* Form validation
* Business logic
* Template rendering
* Database interaction

---

## Database

SQLite (development + deployment)

Database file:

```
db.sqlite3
```

Tables include:

* Users
* Blogs
* Rooms
* Messages
* Resources

---

## Cloud Infrastructure

### AWS EC2

The application is hosted on an **AWS EC2 Ubuntu server**.

Server responsibilities:

* Running Django application
* Running Gunicorn application server
* Hosting Nginx web server

Instance type used:

```
t3.micro
```

---

### Amazon S3

All uploaded files are stored in **Amazon S3 object storage**.

Examples:

* User avatars
* Blog images
* Uploaded resources

Benefits:

* Highly scalable
* Reliable storage
* Accessible from anywhere

Libraries used:

```
boto3
django-storages
```

---

## Deployment Stack

Production architecture:

```
User Browser
     ↓
Internet
     ↓
AWS EC2 Server
     ↓
Nginx (Web Server / Reverse Proxy)
     ↓
Gunicorn (WSGI Application Server)
     ↓
Django Application
     ↓
SQLite Database
     ↓
AWS S3 (Media Storage)
```

---

# Request Flow

Example request:

User opens website:

```
http://13.233.224.139
```

Flow:

```
Browser
   ↓
Internet
   ↓
AWS EC2 instance
   ↓
Nginx receives request
   ↓
Nginx forwards request to Gunicorn
   ↓
Gunicorn sends request to Django
   ↓
Django processes view logic
   ↓
Django queries database
   ↓
Template rendered
   ↓
HTML returned to browser
```

---

# Project Structure

```
studybuddy-cloud/
│
├── base/                # Main Django application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│
├── static/              # Static assets
│
├── templates/           # Global templates
│
├── studybud/            # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── staticfiles/         # Collected static files
│
├── manage.py
├── requirements.txt
└── db.sqlite3
```

---

# Installation (Local Development)

Clone the repository:

```
git clone https://github.com/Bhagawati11/studybuddy-cloud.git
cd studybuddy-cloud
```

Create virtual environment:

```
python -m venv venv
```

Activate virtual environment:

Linux / Mac:

```
source venv/bin/activate
```

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run migrations:

```
python manage.py migrate
```

Start development server:

```
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000
```

---

# Deployment Setup

The application is deployed using:

* AWS EC2
* Nginx
* Gunicorn
* Systemd services

---

# EC2 Connection Command

To connect to the server:

```
ssh -i studybuddy-ec2.pem ubuntu@13.233.224.139
```

---

# Important Server Commands

Navigate to project directory:

```
cd ~/studybuddy-cloud
```

Activate environment:

```
source venv/bin/activate
```

Restart application server:

```
sudo systemctl restart studybuddy
```

Restart web server:

```
sudo systemctl restart nginx
```

Check Gunicorn status:

```
sudo systemctl status studybuddy
```

Check Nginx status:

```
sudo systemctl status nginx
```

View application logs:

```
sudo journalctl -u studybuddy -n 50
```

View Nginx error logs:

```
sudo tail -n 50 /var/log/nginx/error.log
```

---

# Static File Collection

Run:

```
python manage.py collectstatic
```

This moves all static assets into the **staticfiles directory**, which is served by Nginx.

---

# Environment Variables

Sensitive credentials are stored using environment variables.

Example:

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME
AWS_S3_REGION_NAME
```

These are injected via the **systemd service configuration**.

---

# Security

Security mechanisms implemented:

* AWS IAM access control
* S3 bucket permissions
* Environment variable based secrets
* Nginx reverse proxy
* Django CSRF protection
