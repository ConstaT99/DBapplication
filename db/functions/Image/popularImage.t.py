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


@app.route('/api/image/popular/<incidentId>', methods=['GET'])
def popularImage(incidentId):
    limit = int(request.args.get('limit'))
    document = images.find({"incidentId": incidentId}, {"_id": 0, "imageId": "$_id"}).sort(
        "like", pymongo.DESCENDING).limit(limit)
    if document is None:
        return '''Invalid request''', 400
    for i in document:
        print(i)
    return flask.jsonify(list(document))

app.run()