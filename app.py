"""

	main.py


	This script will use the Twilio API to send + receive texts

	Tutorials: 
		https://medium.com/hackernoon/using-twilio-to-send-sms-texts-via-python-flask-and-ngrok-9874b54a0d3

"""


# twilio, flask backend
import os
from dotenv import load_dotenv
import twilio
from twilio.rest import Client
import random
from flask import Flask, request, redirect, render_template, request
from twilio.twiml.messaging_response import MessagingResponse
from flask_sqlalchemy import SQLAlchemy
import sys
import argparse

# set testing = True, as default
testing = True

# load environment, get credentials
load_dotenv(".env")
account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]

# log into account
client = Client(account_sid, auth_token)

# get phone numbers
from_number="+12392417096"
#to_number="+12393003122"
to_number=""

# create our app
app = Flask(__name__)

# get/send messages
"""
@app.route("/sms", methods=["GET", "POST"])
def sms():

	# get their text
	message_body = request.form["Body"].upper() # change to uppercase

	# initialize response text
	resp_text = ""

	# if their message said "DINER", send message confirming subscription, add to SQL database
	if "DINER" in message_body:
		resp_text = r"Thank you for following us here at Thee City's Diner! Be on the lookout for new deals every week, and we look forward to seeing you soon!"

	else:
		resp_text = r"Welcome to Thee City's Diner! Please text 'DINER' to be the first to receive exclusive offers, such as 10% off any entree. Sign up today!"

	# send text back
	resp = MessagingResponse()
	resp.message(resp_text)
	return str(resp)
"""

# for debugging purposes
@app.route("/")
def main():

	return "This is the main page of the Twilio app!"

@app.route("/sms", methods = ["GET", "POST"])
def sms():
	"""
		Respond to incoming messages with our own message
	"""

	# initialize response
	resp = MessagingResponse()

	# add a message
	resp.message("Thank you for your response! We are confirming your message.")

	return str(resp)

"""
# add website to send number (make generic, for now, to take any page name)
@app.route("/<string:page_name>")
def render_static(page_name):

	return render_template(f"{page_name}.html")
"""

@app.route("/send_text")
def send_text():
	"""
		Gets inputs from webpage to send text, then sends texts
	"""
	if request.method=="POST":
		# get the phone number
		phone_number = request.form.get("phone_number")
		# get message
		message = request.form.get("message")
		return f"You're sending the following messaging to {phone_number}: {message}"
	return render_template("send_text.html")


if __name__ == "__main__":

	"""
	# parse args
	parser = argparse.ArgumentParser()
	parser.add_argument("--testing", default=True, type=bool, choices=[True, False], help="Boolean flag for testing purposes") # add argument

	args = parser.parse_args() # get args

	# get testing argument
	if args.testing:
		testing=True
	else:
		testing=False

	# input phone number:
	to_number = input("Please add someone's phone number for this service: (in the form of +12345678910) ")


	# send initial messages
	init_message = r"Thank you for subscribing to Thee City's Diner! Treat yourself to a 10% discount next time you come see us! Come along with your family and spend tonight with us here at Thee City's Diner!"

	# create initial message
	client.messages.create(to=to_number, from_=from_number, body=init_message)

	"""

	# run app
	app.run(debug=True)







