import mysql.connector

try:
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="blueflags",
        database="tce"
    )

    if conn.is_connected():
        print("Connected to MySQL database")

except mysql.connector.Error as e:
    print("Error connecting to MySQL database: ", e)