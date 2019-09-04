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
        class_info = request.form

        subject = class_info['subject']
        if subject == '':
            print('yikes')
            subject = '*'
        class_number = class_info['class number']
        status = class_info['???']
        credits = class_info['credits']

        query = 'SELECT * FROM classes WHERE subject=%s, class_number=%s, status=%s, credits=%s'
        vals = (subject, class_number, status, credits)
        db.execute(query, vals)
        results = db.fetchall()

        if class_info['search'] == 'Show all classes':
            print('Asking to show all classes')
        elif class_info['search'] == 'Search':
            print('Asking for search')

        return redirect('/results', classes=class_info)

        #escaping to prevent XSS attack
        # status = str(utils.escape(userDetails['name']))
        # subject = str(utils.escape(userDetails['email']))
        # class_number = str(utils.escape(userDetails['email']))
        # credits = str(utils.escape(userDetails['email']))
        # sql_command = 'INSERT INTO users(name,email) VALUES (%s, %s)'
        # db.execute(sql_command, (escape(name), escape(email)))
        # mydb.commit()
        # return redirect('/results')
    return render_template('index.html')

# status, subject, class number, credits

# @app.route('/results')
# def results():
#     sql_command = 'SELECT * FROM classes WHERE '
#     db.execute('SELECT * FROM users')
#     classDetails = db.fetchall()
#     if classDetails:
#         return render_template('users.html', userDetails=userDetails)
#     else:
#         return 'There\'s no users yet!'
#     # if submit button clicked:
#     #     return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
