import flask
from flask import request, jsonify
import pymongo
import numpy as np
import datetime
from bson.json_util import dumps
from flask import request
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

client = pymongo.MongoClient("localhost", 27017)
db = client.projectnull
images = db.images

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
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
        "incidentId": incidentId
    }
    insertedId = str(images.insert_one(imageDocument).inserted_id)
    filename = insertedId + ".jpg"
    destination = "/".join([target, filename])
    image.save(destination)
    return flask.jsonify(insertedId)

