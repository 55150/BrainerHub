# BrainerHub Employee Data Upload API

## Overview

This project is a Django REST Framework API that allows users to upload an Excel file containing employee data. The API reads the file, extracts data, and inserts it into the database while maintaining a one-to-many relationship between `Company` and `Employee` models.

## Features

- Reads employee data from an Excel (`.xlsx`) file.
- Stores company names in the `Company` table.
- Stores employee details in the `Employee` table.
- Ensures a one-to-many relationship where one company can have multiple employees.
- Prevents duplicate employee records based on `employee_id`.
- Optimized bulk data insertion for performance.

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite (default database, can be changed)
- Pandas
- OpenPyXL

## Project Structure

```
BrainerHub/
│── EmployeeApp/           # Django app containing models and API views
│   ├── migrations/       # Database migrations
│   ├── models.py         # Database models for Employee and Company
│   ├── serializers.py    # Serializers for API data validation
│   ├── views.py          # API views handling file upload and data insertion
│── BrainerHub/           # Main Django project directory
│── db.sqlite3            # SQLite database (default, can be changed)
│── manage.py             # Django project management script
│── Employee_Company.xlsx # Sample Excel file for testing
│── README.md             # Project documentation
```

## Installation

### 1. Clone the Repository

```sh
git clone https://github.com/55150/BrainerHub.git
cd brainerhub
```

### 2. Create and Activate Virtual Environment

```sh
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Apply Migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional, for Django Admin Access)
Use the following credentials:

Username: root
Password: 12345

```sh
python manage.py createsuperuser
```

### 6. Run the Server

```sh
python manage.py runserver
```

## API Usage

### Upload Employee Data

#### Endpoint:

```
POST /upload/
```

#### Request:

- Upload an Excel file (`.xlsx` format) containing employee details.
- Key name for file: `file`

#### Example using cURL:

```sh
curl -X POST http://127.0.0.1:8000/upload/ \
  -F "file=@Employee_Company.xlsx"
```

#### Sample Response (Success):

```json
{
    "message": "Data inserted successfully"
}
```

#### Sample Response (Error):

```json
{
    "error": "No file uploaded"
}
```

## Database Models

### Company Model

| Field | Type            | Description         |
| ----- | --------------- | ------------------- |
| id    | Integer (Auto)  | Primary Key         |
| name  | CharField (255) | Unique Company Name |

### Employee Model

| Field          | Type               | Description              |
| -------------- | ------------------ | ------------------------ |
| employee\_id   | Integer            | Unique Employee ID       |
| first\_name    | CharField (100)    | First Name               |
| last\_name     | CharField (100)    | Last Name                |
| phone\_number  | CharField (15)     | Contact Number           |
| company        | ForeignKey         | Links to `Company` table |
| salary         | Integer            | Employee Salary          |
| manager\_id    | Integer (Nullable) | Manager ID               |
| department\_id | Integer            | Department ID            |

## Notes

- Make sure the column names in the Excel file match the model fields (case-insensitive).
- The `company_name` column in Excel is mapped to the `Company` model.
- The `employee_id` field must be unique; duplicate records will be skipped.

## License

This project is for educational purposes only. Modify and use as needed!

---

Feel free to update this README if you change your project structure or requirements.

but how to create and how to make README.md file ?

