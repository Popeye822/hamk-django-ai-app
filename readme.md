# Django Web Application – HAMK Tekoälyosaaja Course

This project was created as part of the **HAMK Tekoälyosaaja (AI Specialist) course** assignment.

The goal of the assignment was to use **AI tools to help generate code for a Django web application** and to learn the basic structure and workflow of a Django project.

---

# Course Information

**Course:** HAMK Tekoälyosaaja  
**Assignment:** Web Application with Python Django  

**Group:** Hermes  

**Group Members:**

- Marja Junkkari  
- Kalle Sepponen  

---

# Application Description

This project is a simple **Notes web application** built with **Python and Django**.

The application allows users to:

- create and store notes
- add a title and description
- automatically store the creation date
- mark notes as completed
- view notes in a list view
- open a detailed view for each individual note
- manage notes through the Django admin interface

The application demonstrates the most important components of a Django web application.

---

# Django Concepts Demonstrated

The project includes the following Django components:

### Models
Defines the database structure for storing notes.

### Admin Interface
The Django admin interface allows easy management of notes through a web interface.

### Views
Views retrieve data from the database and send it to templates for rendering.

### URL Routing
URLs connect browser requests to the correct Django views.

### Templates
HTML templates render the data to the user in the browser.

---

# Technologies Used

- Python
- Django
- HTML
- Django Template Engine
- Git
- GitHub

---

# Project Structure

```
mysite/
│
├── manage.py
├── mysite/
│   ├── settings.py
│   ├── urls.py
│
└── core/
    ├── models.py
    ├── admin.py
    ├── views.py
    ├── urls.py
    └── templates/
        └── core/
            ├── note_list.html
            └── note_detail.html
```

---

# How to Run the Project

### 1 Install Python
Make sure Python is installed on your system.

### 2 Install Django

pip install django

### 3 Run database migrations

python manage.py migrate

### 4 Create a superuser for admin access

python manage.py createsuperuser

### 5 Start the development server

python manage.py runserver

---

# Open the Application

Main page:
http://127.0.0.1:8000

Admin interface:

http://127.0.0.1:8000/admin


From the admin interface it is possible to create and manage notes.

---

# Using AI in Development

AI tools were used to assist in generating the Django application.

AI helped generate code for:

- Django models
- Admin configuration
- Views
- URL routing
- HTML templates

Using AI significantly sped up the development process and helped understand how the different parts of Django work together.

---

# Learning Outcome

Through this assignment we learned:

- the basic structure of a Django project
- how Django models interact with the database
- how the Django admin interface works
- how views and templates display data in the browser
- how URL routing connects the application
- how AI can assist in coding and learning new technologies

---

# Author Notes

This project was created as a learning exercise for the **HAMK AI Specialist course** to explore how AI can assist with web application development using Python and Django.