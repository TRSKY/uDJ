import json
import os
import re
from flask import Flask, render_template, request, redirect, url_for, abort, Response
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
db = client.test

@app.route("/test/insertdb/user", methods=['POST'])
def insertTest():
	print 'we get here'
	key1 = "username"
	key2 = "device_ID"
	user = request.form['user']
	#user should have the correct schema {"username":"jdoe13", "device_ID": "xxxxx"}
	user = json.loads(user)
	if len(user.keys()) != 2:
		return json.dumps("error")
	if key1 in user.keys() and key2 in user.keys():
		if re.match("^[a-zA-Z0-9_]+$", user[key1]) != None and re.match("^[a-zA-Z0-9_]+$",user[key2]) != None:
			result = db.users.insert_one(user)
			print result.inserted_id
			print type(result.inserted_id)
			return json.dumps(str(result.inserted_id))
	return "error"

@app.route("/test", methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
	#logs in existing usr, makes new user if the request is valid and the usr cannot be found
	return render_template('login.html')

@app.route("/<user_id>", methods=['GET'])
def user_page(user_id):
	#we need a usr db
	#get usr meta from usr db
	#return user meta as json
	return ''

@app.route("/event", methods=['GET', 'POST'])
def new_event(event_id):
	#create new event 
	#return the new event id
	return ''

@app.route('/events/<query>', methods=["GET, POST"])
def search_events(query):
	#return events matched to query
	return ''

@app.route("/event/<event_id>", methods=['GET', 'PUT'])
def event(event_id):
	#add songs to queue
	return ''

@app.route("/admin/event/<event_id>", methods=['GET', 'PUT'])
def admin(event_id):
	#check if the request is actually from the admin
	#admin power behavior
	return ''

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True) # local running on port 5000
    #app.run(host='0.0.0.0', port=8080, debug=False)
