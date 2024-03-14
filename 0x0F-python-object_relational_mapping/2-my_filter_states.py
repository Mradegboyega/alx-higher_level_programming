#!/usr/bin/python3
"""
A script that displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
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

    # Construct the SQL query
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    # Execute the query
    cur.execute(query)

    # Fetch all the results
    states = cur.fetchall()

    # Print the states
    for state in states:
        print(state)

    # Close all connections
    cur.close()
    db.close()

