#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cur = db.cursor()

    # Execute the query
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    # Fetch all the results
    cities = cur.fetchall()

    # Print the cities
    for city in cities:
        print(city)

    # Close all connections
    cur.close()
    db.close()

