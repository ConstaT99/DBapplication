import flask
from flask import request, jsonify
from pymongo import MongoClient
import numpy as np
import datetime
from bson.json_util import dumps
import pymongo
from flask import request

client = MongoClient("localhost",27017)
db = client.projectnull
user = db.user

userDocument = {
  "userId": { "404DontTrustTears" },
  "password": {"areukiddingme"},
  "nickName": {"small4"},
  "alertLocation": {"SF"},
  "phoneNumber": {1234567},
  "email" : {"411411@gmail.com"}
}

# @app.route('/api/people/mongodb', methods=['GET'])
def deleteUser(userID: str, password: int):
    userId = request.args.get('userId')
    password = request.args.get('password')
    pw = user.find({userID: "userID"},{password:1})
    if pw != password:
        # raise error
         return '''<h1>An error achieve </h1><p>your password is not correct</p >'''
    else:
        user.remove({userID: "userID"})

    return 0