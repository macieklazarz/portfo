from flask import Flask, render_template, url_for, request, redirect
import csv
import datetime
app = Flask(__name__)
# print(__name__)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        database.write(f'\n{data["mail"]}, {data["subject"]}, {data["message"]}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        mail = data["mail"]
        subject=data["subject"]
        message=data["message"]
        timestamp=datetime.datetime.now()
        csv_writer = csv.writer(database2, delimiter=',',quotechar='"',  quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([mail,subject,message,timestamp])


@app.route('/')
def my_home():
    # print(url_for('static', filename='bolt.ico'))
    return render_template('index.html')

@app.route('/<name>')
def my_home2(name=None):
    # print(url_for('static', filename='bolt.ico'))
    return render_template(name)

@app.route('/submit_form', methods = ['POST','GET'])
def submit_form():
    if request.method=='POST':
        data = request.form.to_dict()
        print(data)
        write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'sth is wrong'