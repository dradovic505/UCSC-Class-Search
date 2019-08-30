#Python3
#Set up MySQL database
import mysql.connector

#first comment out lines 12 and 18-22 and run this file, then uncomment them
#and comment out lines 15 and 16 and run this file again. The database is set up.

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='class_search'
)

db = mydb.cursor()
# db.execute('CREATE DATABASE class_search')

db.execute('CREATE TABLE IF NOT EXISTS classes (id INT AUTO_INCREMENT PRIMARY KEY,            \
            subject VARCHAR(500), class_number INT, career VARCHAR(500),        \
            status VARCHAR(500), available_seats INT,                           \
            wait_list_total INT, ge VARCHAR(500), credits INT,                  \
            meeting_times VARCHAR(500), room VARCHAR(500), instructor VARCHAR(500))')

db.execute('SELECT id, subject FROM classes')
myresult = db.fetchall()
for x in myresult:
    print(x)
