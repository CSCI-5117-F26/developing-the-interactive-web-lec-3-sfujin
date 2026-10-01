from flask import Flask, render_template, request

import os

app = Flask(__name__)

names = []

@app.route('/')
def home():
  global names
  return render_template("main.html", names=names)

@app.route('/hi', methods=['POST'])
def hi():
  global names
  if request.form.get("name"):
    names.append(request.form.get("name"))
  return render_template('main.html', names=names)
