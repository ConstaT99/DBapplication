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
def editUser(userId: str, password: int, nickname: str, alertLocation: str, phoneNumber: int, email: str):
    #userId = request.args.get('userId')
    #password = request.args.get('password')
    #nickName = request.args.get('nickName')
    #alertLocation = request.args.get('alertLocation')
    #phoneNumber = request.args.get('phoneNumber')
    #email = request.args.get('email')
    pw = user.find({"userId": userId},{"password" : 1,"_id":0 })[0]["password"]
    if pw != password:
        # raise error
         return '''<h1>An error achieve </h1><p>your password is not correct</p >'''
    else:
        output = user.update_one({"userId": userId}, {"$set":{"nickname": nickname, "alertLocation": alertLocation, "phoneNumber": phoneNumber, "email": email}})

    return dumps(output)


if __name__ == "__main__":
  userId = input("userId: ")
  password = input("password: ")
  nickname = input("nickname: ")
  alertLocation = input("alertLocation: ")
  phoneNumber = input("phoneNumber: ")
  email = input("email: ")
  print(editUser(userId, password,nickname, alertLocation, phoneNumber, email))