import mysql.connector

con = mysql.connector.connect(
    host = "sql12.freesqldatabase.com",
    username = "sql12790788",
    password = "P9KQjG1LFF",
    database = "sql12790788"
)

zx = con.cursor()

q = "show databases"

zx.execute(q)

print(zx.fetchall())