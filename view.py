from app import *
from flask import render_template, request, redirect, url_for, json


@app.route("/main", methods=["GET", "POST"])
def main():
	return render_template("main.html")


@app.route("/form", methods=["GET", "POST"])
def form():
	