#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""

import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]

    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC", (search,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
