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
db.execute('CREATE DATABASE class_search')

db.execute('CREATE TABLE classes (id INT AUTO_INCREMENT PRIMARY KEY,           \
            subject VARCHAR(255), class_number MEDIUMINT, career VARCHAR(255), \
            status VARCHAR(255), available_seats MEDIUMINT,                    \
            wait_list_total MEDIUMINT, ge VARCHAR(255), credits MEDIUMINT,     \
            meeting_times VARCHAR(255), room VARCHAR(255), instructor VARCHAR(255))')
