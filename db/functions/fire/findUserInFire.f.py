import flask
from flask import request, jsonify
from pymongo import MongoClient
import numpy as np
import datetime
from bson.json_util import dumps
import pymongo
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


client = MongoClient("localhost",27017)
db = client.projectnull
fire = db.calFire
user = db.user

@app.route('/api/user/fire', methods=['GET'])
def userInFire():
    #userId = request.args.get("userId")
    alertLocation = request.args.get("alertLocation")
    # county = fire.find({"incident_county": alertLocation},{"_id": 0 })
    # response = flask.jsonify(county)

    a = fire.aggregate([
        {$unwind: "$incident_county"},
        {$group:{
            _id:"$incident_county",
            numFires: { $sum: 1 },
         },
        },
        {$match: {numFires: {$gt: 3}}}
        ])
    counties = new Array()
    while (a.hasNext()){
        tmp = aid.push(a.next()._id)
        }
    response = flask.jsonify(list(user.find({alertLocation: {$in: tmp}}, {userId:1, _id:0})))

    return response

app.run()
