#soje.py

from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/')
@app.route('/<int_num>')
def inputTest(num=None):
    return render_template('index.html', num=numj)

@app.route('/calculate', mehods=['POST'])
def calculate(num=None):
    if request.method == 'POST':
        temp = request.form['num']
        if is_number(temp):
            pss
