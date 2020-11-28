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



@app.route('/api/image/<imageId>/like/<userId>', methods=['PUT'])
def likeImage(imageId, userId):
    doc = images.find_one({"_id": ObjectId(imageId)})
    if doc is None:
        # raise error
        return '''Invalid request''', 400

    # userId is the id of user who click the like button
    result = user.find_one(
        {"$and": [{"userId": userId}, {"likes": {"$elemMatch": {"$eq": imageId}}}]})

    if result is None:
        images.update_one({"_id": ObjectId(imageId)}, {"$inc": {
            "like": 1}})
        user.update_one({"userId": userId}, {"$push": {
            "likes": imageId}})
    else:
        images.update_one({"_id": ObjectId(imageId)}, {"$inc": {
            "like": -1}})
        user.update_one({"userId": userId}, {"$pull": {
            "likes": imageId}})
    return flask.jsonify(images.find_one({"_id": ObjectId(imageId)}, {"_id": 0}))
