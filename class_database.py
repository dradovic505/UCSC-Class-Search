#Python3
#Set up MySQL database
import mysql.connector
import yaml

my_credentials = yaml.safe_load(open('db.yaml'))
mydb = mysql.connector.connect(
    host=my_credentials['mysql_host'],
    user=my_credentials['mysql_user'],
    password=my_credentials['mysql_password'],
    database=my_credentials['mysql_db']
)
db = mydb.cursor(prepared=True)

db.execute('CREATE DATABASE IF NOT EXISTS class_search')

db.execute('CREATE TABLE IF NOT EXISTS classes (id INT AUTO_INCREMENT PRIMARY KEY, \
            subject VARCHAR(500), class_number INT, career VARCHAR(500),           \
            status VARCHAR(500), available_seats INT,                              \
            wait_list_total INT, ge VARCHAR(500), credits INT,                     \
            meeting_times VARCHAR(500), room VARCHAR(500), instructor VARCHAR(500))')
