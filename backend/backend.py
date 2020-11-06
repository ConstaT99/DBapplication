import flask
from flask import request, jsonify, redirect, json
from pymongo import MongoClient
import numpy as np
import datetime
from bson.json_util import dumps
import pymysql.cursors
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]
# userDocument = {
#   "userId":  "404" ,
#   "password": "12345",
#   "nickName": "small4",
#   "alertLocation": "SF",
#   "phoneNumber": 12345678,
#   "email" : "411411@gmail.com"
# }


client = MongoClient('localhost', 27017)
db = client.projectnull  # create test collection
user = db.user
messages = db.messages

# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='teamnull',
#                              db='db',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)
#
#
# cursor = connection.cursor()

#
# @app.route('/', methods=['GET'])
# def home():
#     return '''<h1>Distant Reading Archive</h1>
# <p>A prototype API for distant reading of science fiction novels.</p>'''
#
#
# # A route to return all of the available entries in our catalog.
# @app.route('/api/people/mongodb', methods=['GET'])
# def api_mongodb():
#     return dumps(db.people.find_one())


# @app.route('/api/people/mysql', methods=['GET'])
# def api_mysql():
#     sql = "SELECT * FROM people WHERE name=%s"
#     # use request.args.get to fetch get params
#     # e.g. GET /api/people/mysql?name=root
#     cursor.execute(sql, request.args.get('name'))
#     return jsonify(cursor.fetchall())

@app.route('/api/user/login', methods=['GET'])
def login():
    userId = request.args.get('userId')
    password = request.args.get('password')
    doc = user.find_one({"userId": userId})
    if doc is None or doc["password"] != password:
        # raise error
        return '''Invalid request''', 400

    response = flask.jsonify(user.find_one({"userId": userId}, {
        "userId": 1, "nickName": 1, "alertLocation": 1, "phoneNumber": 1, "email": 1, "_id": 0}))
    return response

@app.route('/api/people/mongodb/create', methods=['GET'])
def createUser():
    userId = request.args.get('userId')
    password = request.args.get('password')
    nickName = request.args.get('nickName')
    alertLocation = request.args.get('alertLocation')
    phoneNumber = request.args.get('phoneNumber')
    email = request.args.get('email')
    exist_check = user.find({"userId":userId},{"_id":0}).count()

    if exist_check >=1:
        return dumps(print("Account already exsits")),400
    else:
        userDocument = {
          "userId":userId,
          "password":password,
          "nickName":nickName,
          "alertLocation": alertLocation,
          "phoneNumber": phoneNumber,
          "email" : email
        }
        user.insert_one(userDocument)
        print("Field value is not present")
        return dumps(user.find({"userId":userId},{"password":0}))
        # return redirect('http://localhost:3000')


@app.route('/api/location/messages', methods=['GET'])
def postComment():
    # userId = request.args.get('userId')
    # nickName = request.args.get('nickName')
    # alertLocation = request.args.get('alertLocation')
    location = request.args.get('location')
    # phoneNumber = request.args.get('phoneNumber')
    # email = request.args.get('email')
    message = request.args.get('messages')

    messagesDocument = {
      # "userId":userId,
      # "nickName":nickName,
      # "alertLocation": alertLocation,
      "location": location,
      # "phoneNumber": alertLocation,
      # "email" : email,
      "messages" : message
    }
    messages.insert_one(messagesDocument)

    print("Input comment")
    return dumps(messages.find({"location":location}))
    # return dumps(messages.find({"userId":userId}))
        # return redirect('http://localhost:3000'




app.run()
