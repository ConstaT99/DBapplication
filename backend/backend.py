import flask
from flask import request, jsonify, redirect
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

fireDocument = {
  "userId": { "404DontTrustTears" },
  "password": {"areukiddingme"},
  "nickName": {"small4"},
  "alertLocation": {"SF"},
  "phoneNumber": {1234567},
  "email" : {"411411@gmail.com"}
}

client = MongoClient('localhost', 27017)
db = client.projectnull  # create test collection
user = db.user

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

print("wwwwwww")

@app.route('/api/people/mongodb', methods=['GET'])
def createUser():
    print("aaa")
    userId = request.args.get('userId')
    password = request.args.get('password')
    nickName = request.args.get('nickName')
    alertLocation = request.args.get('alertLocation')
    phoneNumber = request.args.get('phoneNumber')
    email = request.args.get('email')
    exist_check = user.find({"userId":userId},{"_id":0}).count()

    if exist_check >=1:
        print("ttttttttttttttt")
        return dumps(print("Account already exsits")),400
    else:
        userDocument = {
          "userId":userId,
          "password":password,
          "nickName":nickName,
          "alertLocation": alertLocation,
          "phoneNumber": alertLocation,
          "email" : email
        }
        user.insert_one(userDocument)
        print("Field value is not present")
        return dumps(user.find({"userId":userId},{"password":0}))
        # return redirect('http://localhost:3000')



app.run()
