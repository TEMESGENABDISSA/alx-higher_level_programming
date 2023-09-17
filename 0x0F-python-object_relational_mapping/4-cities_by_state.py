#!/usr/bin/python3
"""lists all of the  cities from the database hbtn_0e_4_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host='localhost',
                         port=3306)

    cur = db.cursor()
    sql = """SELECT c.id, c.name, s.name
            FROM states s, cities c
            WHERE c.state_id = s.id
            ORDER BY id ASC"""

    cur.execute(sql)

    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    db.close()
