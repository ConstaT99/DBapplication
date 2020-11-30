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

incidentId = "adasqewqeqasfasfsd"
imageurl = "localhost"
comment = [1,2,3,4,5,6,7,8]

for i in range(10):
    Image1 = {
            "userId": i,
            "incidentId": incidentId,
            "imageurl": imageurl,
            "comment" : [1,2,3,4,5,6,7,8],
            "like" : 1000 - i* 100
        }

    images.insert_one(Image1)

