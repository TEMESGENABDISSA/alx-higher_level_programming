#!/usr/bin/python3
'''
get all of the  states module
'''

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host='localhost',
                         port=3306)

    cur = db.cursor()

    sql = """ SELECT * FROM states WHERE
                name LIKE BINARY '{}'
                ORDER BY id ASC """.format(argv[4])

    cur.execute(sql)
    states = cur.fetchall()

    for state in states:
        print(state)
