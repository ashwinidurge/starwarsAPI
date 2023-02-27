"""
user: root
password: qwerty
host: 127.0.0.1
port: 3306
database: starwarsdb
"""

import pymysql

# Connect to the database
connection = pymysql.connect(
    host="127.0.0.1",
    user="root",
    port=3306,
    password="@shU2212",
    database="starwarsdb",
    cursorclass=pymysql.cursors.DictCursor,
)

breakpoint()


cursor = connection.cursor()
cursor.execute("SHOW DATABASES")
results = cursor.fetchall()
for result in results:
    print(result)