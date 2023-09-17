#!/usr/bin/python3
""""
Takes in the  arguments & displays all values
in the states table of hbtn_0e_0_usa
(safe from MySQL injections!)
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
    sql = """SELECT * FROM states
            WHERE name = %s
            ORDER BY id ASC"""

    cur.execute(sql, (argv[4],))
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
