#!/Users/theDoctor/opt/anaconda3/envs/ PythonData

from flask import Flask, render_template, redirect


app = Flask(__name__)

@app.route("/")
def index():
	print("hello")
	return render_template("index.html")