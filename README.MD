# 📝 Django Task Manager

A simple **Task Manager Web Application** built using Django.
This project supports both:

*  Web Interface (HTML Templates)
*  API Endpoints (JSON for Postman)

---

## Features

* Add Task
* View Tasks
* Update Task
* Delete Task
* API support (Create, Read, Update, Delete)
* Admin panel for database management

---

##  Project Structure

```
taskproject/
│
├── manage.py
├── db.sqlite3
│
├── taskproject/
│   ├── settings.py
│   ├── urls.py
│
└── tasks/
    ├── admin.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── templates/
        └── tasks/
            ├── task_list.html
            ├── add_task.html
            └── update_task.html
```

---

##  Requirements

* Python 3.x
* Django

Install Django:

```
pip install django
```

---

## ▶ How to Run the Project

### 1. Clone the Repository

```
git clone <your-repo-url>
cd taskproject
```

---

### 2. Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

### 3. Create Superuser (for Admin Panel, Optional)

```
python manage.py createsuperuser
```

---

### 4. Run Server

```
python manage.py runserver
```

---

### 5. Open in Browser

* Home Page:
  http://127.0.0.1:8000/

* Admin Panel:
  http://127.0.0.1:8000/admin/

---

##  Web Interface Routes

| Action      | URL             |
| ----------- | --------------- |
| View Tasks  | `/`             |
| Add Task    | `/add/`         |
| Update Task | `/update/<id>/` |
| Delete Task | `/delete/<id>/` |

---

##  API Endpoints (Postman)

---

###  Get All Tasks

```
GET /
```

Header:

```
Accept: application/json
```

---

###  Create Task

```
POST /add/
```

Header:

```
Content-Type: application/json
```

Body:

```json
{
  "title": "Task",
  "description": "Sample",
  "due_date": "2026-04-20",
  "status": "Pending"
}
```

---

###  Update Task

```
PUT /update/<id>/
```

Header:

```
Content-Type: application/json
```

Body:

```json
{
  "title": "Updated Task",
  "description": "Updated",
  "due_date": "2026-04-25",
  "status": "Completed"
}
```

---

###  Delete Task

```
DELETE /delete/<id>/
```

---

##  Admin Panel

* URL: `/admin/`
* Login using superuser credentials
* Manage tasks directly (add, edit, delete)

---

##  Tech Stack

* Django
* SQLite (default database)
* HTML Templates

---

##  Notes

* UI uses HTML forms (POST requests)
* API uses JSON (POST/PUT/DELETE)
* Same views handle both UI and API using conditions

---

##  Author

* Yash Tripathi

----