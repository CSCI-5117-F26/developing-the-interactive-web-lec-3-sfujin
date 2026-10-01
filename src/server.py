from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
  return "<a href='/hi'>Hi</a>"

@app.route('/hi', methods=['GET'])
def hello_world():
  user_name = request.args.get("userName", "unknown")
  return render_template('main.html', user=user_name)
