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


@app.route('/api/image', methods=['POST'])
def createImage():
    target = os.path.join(APP_ROOT, 'images/')  # folder path
    if not os.path.isdir(target):
        os.mkdir(target)     # create folder if not exits
    userId = request.form['userId']
    incidentId = request.form['incidentId']

    image = request.files.getlist("fireImage")[0]
    imageDocument = {
        "userId": userId,
        "incidentId": incidentId,
        "comments": [],
        "like": 0
    }
    insertedId = str(images.insert_one(imageDocument).inserted_id)
    filename = insertedId + ".jpg"
    destination = "/".join([target, filename])
    image.save(destination)
    user.update_one({"userId": userId}, {"$push": {
        "uploads": insertedId}})
    return flask.jsonify(insertedId)
