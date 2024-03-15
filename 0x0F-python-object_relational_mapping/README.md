# Object-Relational Mapping with SQLAlchemy

This repository contains Python scripts that demonstrate Object-Relational Mapping (ORM) concepts using SQLAlchemy, a powerful SQL toolkit and Object-Relational Mapper for Python. Each script interacts with a MySQL database and performs various operations such as creating tables, querying data, defining relationships between tables, and executing CRUD (Create, Read, Update, Delete) operations.

## Requirements
- Python 3.x
- MySQL server
- SQLAlchemy library (`pip install sqlalchemy`)
- MySQL connector for Python (`pip install mysql-connector-python`)

## Task List

1. **Create Database**: A script to create a MySQL database named `hbtn_0e_6_usa`.

2. **All States via SQLAlchemy**: Script to list all State objects from the database `hbtn_0e_6_usa`.

3. **First State**: Script to print the first State object from the database.

4. **Contains 'a'**: List all State objects containing the letter 'a' from the database.

5. **Get a State**: Print the State object with the name passed as an argument from the database.

6. **Add a New State**: Script to add the State object "Louisiana" to the database.

7. **Update a State**: Change the name of a State object with id=2 to "New Mexico".

8. **Delete States**: Delete all State objects with a name containing the letter 'a' from the database.

9. **Cities in State**: Define City class and script to list all City objects from the database along with their corresponding State objects.

10. **City Relationship**: Improve City and State classes with a relationship between them. Script to create the State "California" with the City "San Francisco" in the database.

11. **List Relationship**: Script to list all State objects along with corresponding City objects from the database.

12. **From City**: Script to list all City objects along with their corresponding State objects from the database.

13. **Readme**: README file summarizing all tasks.

14. **Cities in State**: Script to list all City objects from the database `hbtn_0e_101_usa`.

15. **List Relationship**: Script to list all State objects along with corresponding City objects from the database `hbtn_0e_101_usa`.

16. **From City**: Script to list all City objects along with their corresponding State objects from the database `hbtn_0e_101_usa`.

## Usage
- Clone the repository.
- Navigate to the directory containing the Python scripts.
- Execute each script with appropriate arguments as described in the task descriptions.

## Contributors
