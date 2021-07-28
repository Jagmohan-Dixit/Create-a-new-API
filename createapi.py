from flask import Flask,render_template, request, jsonify
import mysql.connector
from mysql.connector import Error



mydb = mysql.connector.connect(host="localhost",user="jagmohan",password="mySQLjagmohan@5252",database="jaggudb")


cursor = mydb.cursor()

cursor.execute("select * from customers")
data = cursor.fetchall()

print(data)