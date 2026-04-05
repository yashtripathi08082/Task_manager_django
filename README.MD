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

##  Testing Setup (pytest)

This project uses **pytest** for automated testing of API endpoints and UI.

---

##  Testing Requirements

Install required packages:

pip install pytest pytest-django


---

##  Test Structure

tasks/
│
└── tests/
    ├── __init__.py
    └── test_tasks.py

---

##  pytest Configuration

Create a file in root directory:

📄 `pytest.ini`

```ini

[pytest]
DJANGO_SETTINGS_MODULE = taskproject.settings
python_files = tests.py test_*.py *_tests.py
```

---

##  Running Tests

Run tests using:

```bash
python -m pytest
```

---

## What is Tested

The following functionalities are covered:

* Create Task (API)
* Get Tasks (API)
* Update Task (API)
* Delete Task (API)
* UI Page Load

---

## Example Output

```bash
collected 5 items
.....
5 passed in 1.2s
```

---

## Important Notes

* Do NOT use `pytest` directly if command not recognized
  Use:

  ```bash
  python -m pytest
  ```

* Ensure you are running command from project root (where `manage.py` exists)

* Tests run on a **temporary test database**, so your real data is safe

---

##  Common Issues & Fixes

###  Error: settings not configured

✔ Solution: Ensure `pytest.ini` exists with correct settings module

---

### Error: pytest not recognized

✔ Solution:

```bash
python -m pip install pytest pytest-django
```

---

### Error: import file mismatch

✔ Solution:

* Remove `tasks/tests.py`
* Use only `tasks/tests/` folder

---

## Summary

* pytest is used for automated testing
* Tests simulate API requests using Django test client
* Ensures all CRUD operations work correctly

---


---

## Tech Stack

* Django
* SQLite (default database)
* HTML Templates

---

## Notes

* UI uses HTML forms (POST requests)
* API uses JSON (POST/PUT/DELETE)
* Same views handle both UI and API using conditions

---

## Author

* Yash Tripathi

----