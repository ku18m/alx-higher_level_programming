#!/usr/bin/python3
"""
connects to a database and lists states that starts with N.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    stateName = sys.argv[4]
    query = """select * from states where name = '{}'
                order by id asc""".format(stateName)

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        database=dbName
    )
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
