from app import *
from flask import render_template, request, redirect, url_for, json
import vk_plus
import mail_plus
from configurate_message import configurate_message
import settings


@app.route("/", methods=["GET", "POST"])
def main():
	return render_template("index.html")


@app.route("/form", methods=["GET", "POST"])
def form():
	client_name = request.form["client_name"]
	phone_number = request.form["phone_number"]
	email = request.form["email"]

	model = request.form["model"]
	memory_size = request.form["memory_size"]
	color = request.form["color"]
	state = request.form["state"]
	tags = request.form["tags"]
	other_information = request.form["other_information"]

	message = configurate_message(
								client_name,
								phone_number,
								email,
								model,
								memory_size,
								color,
								state,
								tags,
								other_information
							)

	mail_plus.send_email(settings.to_mail, settings.from_mail, settings.from_mail_password, message)
	vk_plus.send_message(settings.token, settings.to_user_id)
	return "1"







		

