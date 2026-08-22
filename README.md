# 📦 Inventory Management System

A Python-based **Inventory Management System** designed to help businesses manage their products, track stock levels, record sales, and generate useful inventory reports.

This project is built as a **command-line application** and focuses on practicing Object-Oriented Programming, file handling, JSON data persistence, and application design.

---

## 🚀 Features

### 📦 Product Management

Manage the products available in the inventory.

* ➕ Add products
* 👀 View all products
* 🔎 Search for products
* ✏️ Update product information
* 🗑️ Delete products

Each product contains information such as:

* Product ID
* Product name
* Price
* Quantity
* Category

---

### 🛒 Sales Management

Track products sold to customers.

* Sell products
* Automatically decrease available stock
* Calculate the total sale price
* Record the sale
* View previous sales
* Generate sales reports

Each sale records information such as:

* Sale ID
* Product
* Quantity sold
* Total price
* Sale date

---

### 📦 Stock Management

Keep track of the amount of stock available.

* 🔄 Restock products
* ➖ Adjust/remove stock
* ⚠️ Detect low-stock products
* 🚨 Identify out-of-stock products

The system prevents users from selling more products than are currently available.

---

### 📊 Reports & Statistics

The system provides useful information about the inventory and sales.

Examples include:

* Total number of products
* Total units in stock
* Total inventory value
* Number of low-stock products
* Number of out-of-stock products
* Total sales
* Number of sales
* Total units sold

---

## 💾 Data Persistence

The application uses **JSON** to store data permanently.

Instead of losing all information when the program closes, products and sales are saved to a JSON file and loaded again when the program starts.

### Data flow

```text
Python Objects
      ↓
Lists
      ↓
JSON
      ↓
File
```

When the application starts:

```text
JSON File
    ↓
Python Data
    ↓
Product / Sale Objects
    ↓
Application
```

This allows the inventory to remain available between program sessions.

---

## 🧱 Project Structure

```text
inventory_management/
│
├── main.py
├── menu.py
├── database.py
├── file_handler.py
│
├── models/
│   ├── __init__.py
│   ├── product.py
│   └── sale.py
│
├── data/
│   └── inventory.json
│
└── README.md
```

### Main Components

**`main.py`**

Controls the application and main program loop.

**`menu.py`**

Contains the menu interface and user operations.

**`database.py`**

Stores the Product and Sale objects while the application is running.

**`file_handler.py`**

Handles saving and loading application data using JSON.

**`models/product.py`**

Contains the `Product` class.

**`models/sale.py`**

Contains the `Sale` class.

**`data/inventory.json`**

Stores persistent inventory and sales data.

---

## 🧩 Object-Oriented Design

The project uses two main classes.

### Product

Represents an individual product in the inventory.

```text
Product
├── ID
├── Name
├── Price
├── Quantity
└── Category
```

### Sale

Represents a transaction involving a product.

```text
Sale
├── Sale ID
├── Product
├── Quantity
├── Total
└── Sale Date
```

A `Sale` is associated with a `Product` object, allowing the system to connect sales with the products being sold.

---

## 🛠️ Technologies Used

* **Python**
* **Object-Oriented Programming**
* **JSON**
* **File Handling**
* **Datetime**
* **Exception Handling**
* **Python Modules & Packages**

---

## 🎯 Project Goals

This project was created to strengthen practical Python programming and software design skills through a realistic application.

The main learning goals are:

* Practice OOP in a larger application
* Work with multiple Python modules
* Manage collections of objects
* Build relationships between objects
* Implement CRUD operations
* Work with persistent data
* Convert Python objects to JSON-compatible data
* Reconstruct objects from saved data
* Handle invalid user input
* Generate useful reports and statistics

---

## ▶️ How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Navigate into the project:

```bash
cd inventory_management
```

Run the application:

```bash
python main.py
```

---

## 📌 Future Improvements

Possible future improvements include:

* SQLite database
* Customer management
* Supplier management
* Barcode support
* Authentication
* Multiple inventory locations
* Graphical user interface
* Web-based interface
* Advanced sales analytics

---

## 👨‍💻 Author

**Kidus Yonas**

Built as part of my journey toward becoming a professional software developer and AI engineer.
