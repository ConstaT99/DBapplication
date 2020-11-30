import flask
from flask import request, jsonify
import numpy as np
import datetime
from bson.json_util import dumps
import pymysql.cursors
from flask import request
import pymongo
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

client = pymongo.MongoClient("localhost", 27017)
db = client.projectnull
images = db.images

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Teamnull',
                             db='projectnull',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

user = db.user

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@ app.route('/api/comment', methods=['POST'])
def createComment():
    sql = "INSERT INTO comments (userId, content, imageId) VALUES (%s, %s, %s)"
    userId = request.form.get('userId')
    imageId = request.form.get('imageId')
    content = request.form.get('content')
    val = (userId, content, imageId)
    cursor.execute(sql, val)
    connection.commit()

    doc = user.find_one({"userId": userId})
    if doc is None:
        # raise error
        return '''Invalid request''', 400

    comments = doc["comments"]
    comments.append(cursor.lastrowid)
    user.update_one({"userId": userId}, {"$set": {
        "comments": comments}})

    doc2 = images.find_one({"imageId": imageId})
    if doc2 is None:
        return '''Ivalid request ''', 400
    comments2 = doc['comments']
    comments2.append(cursor.lastrowid)
    images.update_one({"imageId": imageId}, {"$set": {
        "comments": comments2}})

    return flask.jsonify('Success')