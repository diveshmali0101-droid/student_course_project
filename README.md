# Student Course Management System (Django)

A basic Django web application built using **Python, Django, and SQLite**.  
This project allows users to view courses, sign up, enroll in courses, and view their enrolled courses.  
It also includes the Django Admin panel for managing data.

---

## Features

- User Signup
- User Login (Django Authentication)
- View all courses
- Enroll in courses
- View enrolled courses
- Update username
- Admin panel for managing users, courses, and enrollments
- SQLite database

---

## Tech Stack

- Python
- Django
- SQLite
- HTML (Django Templates)

---

## Project Structure

student_course_project/
│
├── courses/
│ ├── migrations/
│ ├── templates/
│ │ └── courses/
│ │ ├── course_list.html
│ │ ├── my_courses.html
│ │ ├── signup.html
│ │ └── update_username.html
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
│
├── config/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── db.sqlite3
├── manage.py
├── .gitignore
└── README.md


---

## How to Run the Project

### 1. Activate Virtual Environment
```bash
.\.venv\Scripts\activate

2. Apply Migrations
python manage.py migrate

3. Create Superuser (Admin)
python manage.py createsuperuser

4. Run Server
python manage.py runserver

URLs

Home (Courses):
http://127.0.0.1:8000/

Signup:
http://127.0.0.1:8000/signup/

My Courses (Login required):
http://127.0.0.1:8000/my-courses/

Admin Panel:
http://127.0.0.1:8000/admin/

Notes

This project is created for learning and practice purposes

Django Admin is used for managing backend data

Suitable for freshers / beginners learning Django

Author

Divesh Mali


---

### ✅ After this
1. Save the file (`Ctrl + S`)
2. Your README is **complete and professional**
3. Ready to upload to **GitHub**

If you want next:
- GitHub upload steps  
- Resume project description  
- Screenshot checklist for recruiters