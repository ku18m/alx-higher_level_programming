#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
locates in the given state {case sensitive}.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    stateName = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        database=dbName
    )
    cursor = db.cursor()
    cursor.execute("""select cities.name from cities
                    inner join states on states.id = cities.state_id
                    where states.name like binary %s
                    order by cities.id asc""", (stateName,))
    rows = cursor.fetchall()
    cities = list(row[0] for row in rows)
    print(*cities, sep=", ", end="\n")

    cursor.close()
    db.close()
