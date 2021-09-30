#soje.py

from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/')
@app.route('/<int_num>')
def inputTest(num=None):
    return render_template('form.html', num=numj)

@app.route('/calculate', mehods=['POST'])
def calculate(num=None):
    if request.method == 'POST':
        temp = request.form['num']
        if is_number(temp):
            pass
        else:
            temp = None
    else:
        temp = None
    return redirect(url_for('inputTest', num=temp))

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

@app.route('/mongo', methods=['POST'])
def mongoTest():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.newDatabase
    collection = db.mongoTest
    results = collection.find()
    client.close()
    return render_template('index.html', data=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=True)
