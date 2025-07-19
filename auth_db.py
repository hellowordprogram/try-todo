import mysql.connector

conn = mysql.connector.connect(
    host = "sql12.freesqldatabase.com",
    username = "sql12790788",
    password = "P9KQjG1LFF",
    database = "sql12790788"
)

csr = conn.cursor()