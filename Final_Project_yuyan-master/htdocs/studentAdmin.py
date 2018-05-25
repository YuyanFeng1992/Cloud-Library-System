
from flask import Flask, render_template, request, Response
from flask import Flask, jsonify, abort, make_response, url_for
from flask.ext.httpauth import HTTPBasicAuth
from collections import OrderedDict
import json
import twitter
import hashlib
from dbfunctions import *
 
app = Flask(__name__, static_url_path = "")

auth = HTTPBasicAuth()
@app.route("/")
@app.route("/studentRecords", methods = ['GET'])
@auth.login_required
def studentRecords():
 
	studentRecs = getEnrollmentRecords()
	

	return render_template('book content.html', records=studentRecs)

@app.route("/index")
@auth.login_required
def index():
	courses = getCourses()		# get the list of courses from db to initialize the raio button list
	return render_template('add.html', courses=courses)

@auth.get_password
def get_password(username):
	dbPwd = getPwd(username)
	return dbPwd

@auth.hash_password
def hash_pw(password):
    pwd = hashlib.sha512(str.encode(password)).hexdigest()
    return pwd

@auth.error_handler
def unauthorized():
	return make_response(jsonify( { 'error': 'Unauthorized access' } ), 401)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog
    
@app.errorhandler(400)
def not_found(error):
	return make_response(jsonify( { 'error': 'Bad request' } ), 400)
 
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route("/bookRecords/api/v1.0/records", methods=['GET'])
def bookRecordsAPI():
	records = getEnrollmentRecords()
	return jsonify({'book record' : records}), 201


@app.route("/processRecord", methods = ['POST'])
@auth.login_required
def processRecord():
# *** A. You are to create the code for the route decorator of "/processRecord" to handle the 
# POST request from the form 
# The view function for this route decorator should:
# 1. store the 5 fields from the form into database using the 
#		db method of createRecord in dbfunctions.
	recorddd = request.form['BookName']
	record = {
		"BookName": request.form['BookName'],
		"Author": request.form['Author'],
		"Publisher": request.form['Publisher'],
		"Pubdate": request.form['Pubdate'],
		"Price": request.form['Price'],
		"Sellingprice": request.form['Sellingprice'],
		"BookCName": request.form['BookCName']
		}
	createRecord(**record)
	api = twitter.Api(consumer_key='6ettX3DHAbMKJKYTn8f2lfN97',consumer_secret='U8MdYGo09zEpyO75Po2z51uhekK3FSxH12frQrND7Km69tqnMl',access_token_key='891462251554770944-URUpURDfqNSq9eFU2p079fqdECrsNPN',access_token_secret='sA5qk6FmVyS8vk1VnfEWKRgfyJ8HGQGVkgYpIFLIvVAeY')
	tweet = "We add a new book : %s"%recorddd
	status = api.PostUpdate(status=tweet)
#	status = api.PostUpdate('There is a new boo')
# 2. on return, render the template of processRecord.html, and pass to the template 
#		the parameters of firstname, lastname, email, and coursenum so that you
#		can use these info to display them on that page
	return render_template('processRecord.html', record=record)
#--------------------------------------------------------
@app.route("/processSuccess", methods = ['POST'])
@auth.login_required
def processSuccess():
	recordd = {"BookId": request.form['BookId']}

	deleted(**recordd)

	return render_template('processSuccess.html', recordd=recordd)


@app.route("/delete")
@auth.login_required
def delete():# get the list of courses from db to initialize the raio button list
	return render_template('delete.html')








#----------------------------------------------------------------
# used for debugging in development only!  NOT for production!!!
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=5000)