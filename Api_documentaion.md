📘 TASK MANAGER API DOCUMENTATION

🔹 Base URL
http://127.0.0.1:8000/


🧾 1. Get All Tasks

📌 Endpoint
GET /

📤 Headers (IMPORTANT)
Accept: application/json


📥 Response (200 OK)

[
  {
    "id": 1,
    "title": "Test Task",
    "description": "Testing",
    "due_date": "2026-04-11",
    "status": "Pending"
  }
]


❌ Possible Errors

Status	Meaning
500	Server error


➕ 2. Create Task

📌 Endpoint
POST /add/


📤 Headers
Content-Type: application/json


📤 Request Body
{
  "title": "New Task",
  "description": "Created via API",
  "due_date": "2026-04-20",
  "status": "Pending"
}
📥 Response (200 OK)
{
  "message": "Task created via API",
  "id": 2
}


❌ Possible Errors


Status	Meaning
400	Invalid JSON
500	Missing fields


✏️ 3. Update Task

📌 Endpoint
PUT /update/<id>/

👉 Example:

PUT /update/1/
📤 Headers
Content-Type: application/json


📤 Request Body
{
  "title": "Updated Task",
  "description": "Updated via API",
  "due_date": "2026-04-25",
  "status": "Completed"
}
📥 Response (200 OK)
{
  "message": "Task updated via API",
  "id": 1
}


❌ Possible Errors
Status	Meaning
404	Task not found
400	Invalid data
500	Server error


❌ 4. Delete Task


📌 Endpoint
DELETE /delete/<id>/

👉 Example:

DELETE /delete/1/
📤 Headers

(No body required)

📥 Response (200 OK)
{
  "message": "Task deleted via API",
  "id": 1
}


❌ Possible Errors


Status	Meaning
404	Task not found
500	Server error


🔄 Alternative Delete (Fallback)

If DELETE method not supported:

POST /delete/<id>/

Headers:

Content-Type: application/json


📊 Status Code Summary


Code	Meaning
200	Success
201	Created (optional improvement)
400	Bad request
404	Not found
500	Server error


🔁 Full API Flow


Create Task
POST /add/


Get Tasks
GET /
(With Accept: application/json)


Update Task
PUT /update/1/


Delete Task
DELETE /delete/1/


⚠️ Important Notes

✔ Always set headers correctly in Postman
✔ Use correct HTTP methods (GET, POST, PUT, DELETE)
✔ Use valid JSON format
