#!/usr/bin/python3
"""
 the takes in the name of a state as an argument
and lists all cities of that state
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host='localhost',
                         port=3306)

    cur = db.cursor()
    sql = """
        SELECT cities.name
        FROM states
        INNER JOIN cities ON states.id=cities.state_id
        WHERE states.name = %s
        ORDER BY cities.id ASC"""

    cur.execute(sql, (argv[4],))

    cities = cur.fetchall()

    print(", ".join([city[0] for city in cities]))

    cur.close()
    db.close()
