#!/usr/bin/python3
"""
connects to a database and lists all states.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, password=password,
        database=dbName
    )
    cursor = db.cursor()
    cursor.execute("select * from states order by states.id asc")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
