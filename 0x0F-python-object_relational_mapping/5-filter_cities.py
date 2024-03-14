#!/usr/bin/python3
"""
A script that lists all cities of a given state from the database hbtn_0e_4_usa.
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
    query = "SELECT cities.id, cities.name, states.name FROM cities \
             JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"

    # Execute the query with the user-provided state name as a parameter
    cur.execute(query, (state_name,))

    # Fetch all the results
    cities = cur.fetchall()

    # Print the cities
    for city in cities:
        print(city)

    # Close all connections
    cur.close()
    db.close()

