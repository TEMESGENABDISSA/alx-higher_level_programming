#!/usr/bin/python3

'''
select states from db hbtn_0e_0_usa
'''

import MySQLdb
import sys

if __name__ == "__main__":
    HOST = 'localhost'
    DB_USER = sys.argv[1]
    DB_PASS = sys.argv[2]
    DB_NAME = sys.argv[3]

    db = MySQLdb.connect(HOST, DB_USER, DB_PASS, DB_NAME)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")
    states = cur.fetchall()
    for state in states:
        print(state)
