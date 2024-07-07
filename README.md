# db-connect

db-connect is a Python package that provides operations for creating connections and performing CRUD operations on MongoDB and MySQL databases.

## Features

- Connect to MongoDB and MySQL databases
- Insert single or multiple records
- Find records
- Delete records
- Update records
- Bulk insert from CSV or Excel files

## Installation

You can install the package via pip:

pip install db-connect

## Usage

from db_connect import MongoDBOperation

# Initialize the MongoDBOperation object
client_uri = "your_mongodb_uri"
database_name = "your_database_name"
collection_name = "your_collection_name"

mongodb_op = MongoDBOperation(client_uri, database_name, collection_name)

# Insert a single record
record = {"name": "John", "age": 30, "sex": "male", "class": "level 300"}
mongodb_op.insert_record(record)

# Insert multiple records
records = [
    {"name": "Jane", "age": 25, "sex": "female", "class": "level 400"},
    {"name": "Doe", "age": 22, "sex": "female", "class": "level 200"}
]
mongodb_op.insert_record(records)


# Find all records
all_records = mongodb_op.find()
print(all_records)

# Find records with a query
query = {"name": "John"}
records = mongodb_op.find(query)
print(records)

# Delete records with a query
query = {"name": "John"}
mongodb_op.delete(query)

# Delete all records
mongodb_op.delete()

# Update records with a query
query = {"name": "Jane"}
update_values = {"age": 26}
mongodb_op.update(query, update_values)

# Bulk insert with cvs
datafile = "path/to/your/file.csv"
mongodb_op.bulk_insert(datafile)

# MySQL Operations
from db_connect import MySQLDBOperation

# Initialize the MySQLDBOperation object
host = "your_mysql_host"
user = "your_mysql_user"
password = "your_mysql_password"
database = "your_database_name"

mysql_op = MySQLDBOperation(host, user, password, database)

# Insert a single record
record = {"name": "John", "age": 30, "sex": "male", "class": "level 300"}
mysql_op.insert_record("students", record)

# Insert multiple records
records = [
    {"name": "Jane", "age": 25, "sex": "female", "class": "level 400"},
    {"name": "Doe", "age": 22, "sex": "female", "class": "level 200"}
]
mysql_op.insert_record("students", records)

# Insert a single record
record = {"name": "John", "age": 30, "sex": "male", "class": "level 300"}
mysql_op.insert_record("students", record)

# Insert multiple records
records = [
    {"name": "Jane", "age": 25, "sex": "female", "class": "level 400"},
    {"name": "Doe", "age": 22, "sex": "female", "class": "level 200"}
]
mysql_op.insert_record("students", records)

# Find records with a query
query = "SELECT * FROM students WHERE name = 'John'"
records = mysql_op.find(query)
print(records)

# Find all records
query = "SELECT * FROM students"
all_records = mysql_op.find(query)
print(all_records)

# Delete records with a condition
condition = "name = 'John'"
mysql_op.delete("students", condition)

# Delete all records
mysql_op.delete("students")

# Update records with a condition
updates = {"age": 26}
condition = "name = 'Jane'"
mysql_op.update("students", updates, condition)

# Bulk insert
datafile = "path/to/your/file.csv"
mysql_op.bulk_insert("students", datafile)

