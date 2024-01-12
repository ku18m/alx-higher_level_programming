#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        database=dbName
    )
    cursor = db.cursor()
    cursor.execute("""select cities.id, cities.name, states.name from states
                    inner join cities on cities.state_id = states.id
                    order by cities.id asc""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
