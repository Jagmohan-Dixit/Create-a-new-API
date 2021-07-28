import mysql.connector

conn =mysql.connector.connect(host="localhost",user="*********",password="**********",database="*********")

print("Database Opened Suceessfully")
cur = conn.cursor()
cur.execute("CREATE TABLE students (Name VARCHAR(30), Rollno INT(11), Branch VARCHAR(40), Email CHAR(50), Semester INT(11))")

print("Table Created Successfully")

conn.close()
