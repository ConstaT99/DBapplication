import flask
from flask import request, jsonify
import pymongo
from pymongo import MongoClient
import numpy as np
import datetime
from bson.json_util import dumps
import pymysql.cursors
from flask import request
from flask_cors import CORS
import os
from flask.helpers import send_from_directory
from bson.objectid import ObjectId

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

client = MongoClient("localhost", 27017)
db = client.projectnull
user = db.user
calFire = db.calFire
images = db.images
@app.route('/api/user', methods=['POST'])
def createUser():
    userId = request.form.get('userId')
    password = request.form.get('password')
    nickName = request.form.get('nickName')
    physicalLocation = request.form.get('physicalLocation')
    phoneNumber = request.form.get('phoneNumber')
    email = request.form.get('email')
    likes = []
    uploads = []
    comments = []
    doc = user.find_one({"userId": userId}, {"_id": 0})

    if doc is not None:
        # raise error
        return '''Invalid request''', 400

    userDocument = {
        "userId": userId,
        "password": password,
        "nickName": nickName,
        "physicalLocation": physicalLocation,
        "phoneNumber": phoneNumber,
        "email": email,
        "likes": likes,
        "uploads": uploads,
        "comments": comments
    }

    user.insert_one(userDocument)

    return flask.jsonify('Success')
