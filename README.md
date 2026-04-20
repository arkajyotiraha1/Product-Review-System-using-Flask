# Product Reviews Web App

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-green)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

A web application built using Flask and MySQL that enables users to add, view, update, and delete product reviews.

---

## Features

* Add product reviews (rating and comment)
* View all submitted reviews
* Edit existing reviews
* Delete reviews
* Simple and clean user interface

---

## Technology Stack

* Backend: Flask (Python)
* Database: MySQL
* Frontend: HTML, CSS

---

## Project Structure

```bash
project/
│
├── app.py
├── templates/
│   ├── mainpage.html
│   ├── reviews.html
│   └── edit.html
└── README.md
```

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/product-reviews-app.git
cd product-reviews-app
```

---

### 2. Install Dependencies

```bash
pip install flask mysql-connector-python
```

---

### 3. Configure MySQL Database

Run the following SQL commands:

```sql
CREATE DATABASE product_reviews;

USE product_reviews;

CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rating INT NULL,
    comment TEXT NULL
);
```

---

### 4. Update Database Configuration

Modify the database connection in `app.py`:

```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="product_reviews"
)
```

---

### 5. Run the Application

```bash
python app.py
```

---

### 6. Access the Application

Open a browser and navigate to:

```bash
http://127.0.0.1:5000/
```

---

## CRUD Operations

| Operation | Description                  |
| --------- | ---------------------------- |
| Create    | Add a new review             |
| Read      | Retrieve and display reviews |
| Update    | Modify an existing review    |
| Delete    | Remove a review              |

---

## Notes

* Rating and comment fields are optional
* Parameterized queries are used to prevent SQL injection
* Suitable for academic and learning purposes

---

## Future Enhancements

* Improve user interface design
* Add rating visualization (stars)
* Implement authentication system
* Add search and filtering functionality

---

## License

This project is for educational purposes.
