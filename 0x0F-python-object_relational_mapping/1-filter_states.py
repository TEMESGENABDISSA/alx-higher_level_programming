#!/usr/bin/python3
"""Module that that lists all states from the database"""


import MySQLdb
import sys


if __name__ == "__main__":

    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=MY_USER,
        passwd=MY_PASS,
        db=MY_DB
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
    ORDER BY states.id ASC")
    table = cur.fetchall()

    for row in table:
        print(row)
    cur.close()
    db.close()
