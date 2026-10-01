# Smart Employee Leave Management API

A RESTful API for managing employees and their leave requests using **Python, Django, and Django REST Framework**.

## Features

- Employee management
- Create, view, update, and delete employees
- Employee leave balance management
- Apply for leave
- Calculate leave duration
- Validate leave dates
- Validate available leave balance
- Approve or reject leave requests
- Deduct leave balance after approval
- Prevent processing already processed leave requests
- View employee leave history
- REST API endpoints

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- Django ORM
- REST APIs
- Git & GitHub

## Project Structure

```text
smart-employee-leave-management-api/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── employees/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── leaves/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```
## Database Design
### Employee
The Employee model contains:
- Name
- Email
- Department
- Designation
- Leave balance
### Leave
The Leave model contains:
- Employee
- Start date
- End date
- Reason
- Status
- Created date
 An employee can have multiple leave requests using a ForeignKey relationship.
## API Endpoints
### Employee APIs
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/employees/` | Get all employees |
| POST | `/api/employees/` | Create employee |
| GET | `/api/employees/<id>/` | Get employee |
| PUT | `/api/employees/<id>/` | Update employee |
| DELETE | `/api/employees/<id>/` | Delete employee |
| GET | `/api/employees/<id>/leaves/` | Get employee leave history |
### Leave APIs
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/leaves/` | Get all leave requests |
| POST | `/api/leaves/` | Apply for leave |
| PATCH | `/api/leaves/<id>/` | Approve or reject leave |
### Leave Workflow
```
Employee
   ↓
Apply for Leave
   ↓
Validate Dates
   ↓
Calculate Leave Duration
   ↓
Validate Leave Balance
   ↓
Pending
   ↓
Manager Processes Request
   ↓
 ┌───────────────┐
 │               │
Approved       Rejected
 │               │
 ↓               ↓
Deduct        No deduction
Balance
```
## Validation
The API validates:
- End date must be greater than or equal to start date
- Requested leave duration must not exceed available leave balance
- Only pending leave requests can be processed
- Invalid leave status is rejected
- Non-existent employees return 404
- Non-existent leave requests return 404
### Example: Create Employee
```
{
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "department": "IT",
    "designation": "Software Engineer"
}
```
### Example: Apply for Leave
```
{
    "employee": 2,
    "start_date": "2026-10-10",
    "end_date": "2026-10-12",
    "reason": "Personal work"
}
```
The leave duration is calculated as:
```
3 days
```
### Example: Approve Leave
```
{
    "status": "Approved"
}
```
When the leave is approved, the corresponding number of days is deducted from the employee's leave balance.
### Example: Reject Leave
```
{
    "status": "Rejected"
}
```
Rejected leave requests do not reduce the employee's leave balance.
### HTTP Status Codes
| Status Code | Meaning |
|---|---|
| 200 | Request successful |
| 201 | Resource created |
| 400 | Invalid request |
| 404 | Resource not found |
## How to Run Locally
#### 1. Clone the repository
```
git clone https://github.com/bbnaik2003/smart-employee-leave-management-api.git
```
#### 2. Navigate to the project
```
cd smart-employee-leave-management-api
```
#### 3. Create a virtual environment
```
python -m venv .venv
```
#### 4. Activate the virtual environment
Windows:
```
.venv\Scripts\activate
```
#### 5. Install dependencies
```
pip install -r requirements.txt
```
#### 6. Run migrations
```
python manage.py migrate
```
#### 7. Start the server
```
python manage.py runserver
```
#### The API will be available at:
```
http://127.0.0.1:8000/
```
## Author
#### B B Naik
#### GitHub: https://github.com/bbnaik2003
