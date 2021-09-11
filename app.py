#!/usr/bin/env python3

from flask import Flask, render_template, redirect
from static.database import DataBase as DB


app = Flask(__name__)

@app.route("/")
def index():
	print("hello")
	return render_template("index.html")


@app.route("/wordcloud")
def wordCloud():
	db = DB()
	(_,pwords, _, nwords) = db.getWordList()
	return render_template("wordcloud.html",pwords, nwords)


@app.route("/pie")
def pieGraph():
	db = DB()
	(p,n) = db.getPieDatq()
	return render_template("wordcloud.html",p, n)