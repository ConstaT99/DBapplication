import flask
from flask import request, jsonify
from pymongo import MongoClient
import numpy as np
import datetime
from bson.json_util import dumps
import pymysql.cursors
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

client = MongoClient('localhost', 27017)
db = client.projectnull # create test collection
user = db.user

userDocument = {
  "userId": { "404DontTrustTears" },
  "password": {"areukiddingme"},
  "nickName": {"small4"},
  "alertLocation": {"SF"},
  "phoneNumber": {1234567},
  "email" : {"411411@gmail.com"}
}


@app.route('/api/people/mongodb', methods=['GET'])
def createUser(userId: str, password: str, nickName: str, alertLocation: str,
phoneNumber: int, email: str):
    userId = request.args.get('userId')
    password = request.args.get('password')
    nickName = request.args.get('nickName')
    alertLocation = request.args.get('alertLocation')
    phoneNumber = request.args.get('phoneNumber')
    email = request.args.get('email')
    exist_check = user.find({"$or": [{"email": email}, {"pnumber": phoneNumber}]},{'_id':0}).count()
    if exist_check >=1:
        return dumps(print("Account already exsits")),400
    else:
        obj_id = user.insert_one(userDocument).insert_id
        print("Field value is not present")
        return redirect('http://localhost:3000')

#
userDocument = {
  "userId": { "%s" },
  "password": {"%s"},
  "nickName": {"%s"},
  "alertLocation": {"%s"},
  "phoneNumber": {%},
  "email" : {"%s"}
} % (userId,password,nickName,alertLocation,phoneNumber,email)
