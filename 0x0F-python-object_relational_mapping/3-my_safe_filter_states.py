#!/usr/bin/python3
"""
A script that displays all values in the states table of hbtn_0e_0_usa where name matches the argument (safe from MySQL injection).
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cur = db.cursor()

    # Construct the SQL query with a parameterized query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query with the user-provided state name as a parameter
    cur.execute(query, (state_name,))

    # Fetch all the results
    states = cur.fetchall()

    # Print the states
    for state in states:
        print(state)

    # Close all connections
    cur.close()
    db.close()

