#Python3
from flask import Flask, render_template, request, redirect, escape, url_for
from jinja2 import utils
import mysql.connector
import yaml

app = Flask(__name__)

my_credentials = yaml.safe_load(open('db.yaml'))
mydb = mysql.connector.connect(
    host=my_credentials['mysql_host'],
    user=my_credentials['mysql_user'],
    password=my_credentials['mysql_password'],
    database=my_credentials['mysql_db']
)
db = mydb.cursor(prepared=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    # url_for('static', filename='style.css')
    if request.method == 'POST':
        print(request.form)
        if request.form['search'] == 'Show all classes':
            print('Asking to show all classes')
        elif request.form['search'] == 'Search':
            print('Asking for search')

    elif request.method == 'GET':
            
        #escaping to prevent XSS attack
        # name = str(utils.escape(userDetails['name']))
        # email = str(utils.escape(userDetails['email']))
        # sql_command = 'INSERT INTO users(name,email) VALUES (%s, %s)'
        # db.execute(sql_command, (escape(name), escape(email)))
        # mydb.commit()
        # return redirect('/results')
    return render_template('index.html')

# @app.route('/results')
# def users():
#     db.execute('SELECT * FROM users')
#     userDetails = db.fetchall()
#     if userDetails:
#         return render_template('users.html', userDetails=userDetails)
#     else:
#         return 'There\'s no users yet!'
#     # if submit button clicked:
#     #     return redirect('/')

if __name__ == '__main__':
    app.run()
