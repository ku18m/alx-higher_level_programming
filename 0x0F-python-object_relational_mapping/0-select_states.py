#!/usr/bin/python3
"""

"""


import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
dbName = sys.argv[3]

db = MySQLdb.connect(
    host="localhost", port=3306, user=username, password=password,
    database=dbName
)
cursor = db.cursor()
cursor.execute("select * from states order by states.id")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
db.close()
