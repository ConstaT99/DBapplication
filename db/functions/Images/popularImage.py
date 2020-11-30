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


def create_connection():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='teamnull',
                           db='projectnull',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

@app.route('/api/image/popular/<incidentId>', methods=['GET'])
def popularImage(incidentId):
    limit = int(request.args.get('limit'))
    documents = images.find({"incidentId": incidentId}, {"_id": 0, "imageId": "$_id", "incidentId": 1, "userId": 1, "comments": 1, "like": 1}).sort(
        "like", pymongo.DESCENDING).limit(limit)

    if documents is None:
        return '''Invalid request''', 400
    result = list(documents)
    for document in result:
        document["imageId"] = str(document["imageId"].binary.hex())

    return flask.jsonify(result)
