# SQL Introduction Project

This project contains SQL scripts for various tasks related to MySQL server operations. The tasks cover database creation, deletion, table creation, data manipulation, and querying.

## Project Structure

The project is organized into individual SQL script files, each corresponding to a specific task. The tasks are numbered, and the script files follow the naming convention:

- `0-list_databases.sql`: List all databases on the MySQL server.
- `1-create_database_if_missing.sql`: Create the database `hbtn_0c_0` if it doesn't already exist.
- `2-remove_database.sql`: Delete the database `hbtn_0c_0` if it exists.
- `3-list_tables.sql`: List all tables in a specified database.
- `4-first_table.sql`: Create a table called `first_table` with specified columns.
- `5-full_table.sql`: Display the full description of the table `first_table`.
- `6-list_values.sql`: List all rows of the table `first_table`.
- `7-insert_value.sql`: Insert a new row into the table `first_table`.
- `8-count_89.sql`: Display the number of records with id = 89 in `first_table`.
- `9-full_creation.sql`: Create a table `second_table` and add multiple rows.
- `10-top_score.sql`: List all records of `second_table` ordered by score (top first).
- `11-best_score.sql`: List records with a score >= 10 in `second_table`.
- `12-no_cheating.sql`: Update the score of Bob to 10 in `second_table`.
- `13-change_class.sql`: Remove all records with a score <= 5 in `second_table`.
- `14-average.sql`: Compute the score average of all records in `second_table`.
- `15-groups.sql`: List the number of records with the same score in `second_table`.
- `16-no_link.sql`: List all records of `second_table` without rows without a name value.
- `101-avg_temperatures.sql`: Display the average temperature (Fahrenheit) by city in `temperatures`.
- `102-top_city.sql`: Display the top 3 cities' temperatures during July and August.
- `103-max_state.sql`: Display the max temperature of each state in `temperatures`.

## Instructions

### Prerequisites

- MySQL 8.0 (version 8.0.25) installed.
- Allowed editors: vi, vim, emacs.

### Execution

To execute a script, use the following command format:

```bash
cat <script_filename> | mysql -hlocalhost -uroot -p hbtn_0c_0
Replace <script_filename> with the actual filename of the script.
Example

bash

cat 0-list_databases.sql | mysql -hlocalhost -uroot -p

This command lists all databases on the MySQL server.
Task-specific Comments

Each script contains comments providing information about the purpose of the task, SQL queries, and any specific instructions.
File Structure

    README.md: This file providing an overview of the project and instructions.
    SQL script files: Individual files for each task.

Feel free to explore and execute the scripts to perform various SQL operations.
