import flask
from flask import request, jsonify
from pymongo import MongoClient
import numpy as np
import datetime
from bson.json_util import dumps
import pymongo
from flask import request

client = MongoClient('localhost', 27017)
db = client.projectnull  # create test collection
user = db.user

countyName = ["Alameda County","Alpine County","Amador County","Butte County","Calaveras County",
"Colusa County","Contra Costa County","Del Norte County","El Dorado County","Fresno County","Glenn County",
"Humboldt County","Imperial County","Inyo County","Kern County","Kings County","Lake County","Lassen County",
"Los Angeles County","Madera County","Marin County","Mariposa County","Mendocino County","Merced County","Modoc County",
"Mono County","Monterey County","Napa County","Nevada County","Orange County","Placer County","Plumas County","Riverside County",
"Sacramento County","San Benito County","San Bernardino County","San Diego County","San Francisco County","San Joaquin County,"
"San Luis Obispo County","San Mateo County","Santa Barbara County","Santa Clara County","Santa Cruz County","Shasta County",
"Sierra County","Siskiyou County","Solano County","Sonoma County","Stanislaus County,Sutter County","Tehama County","Trinity County",
"Tulare County","Tuolumne County","Ventura County","Yolo County","Yuba County"]

# create user document
for x in range(5):
    a = uuid.uuid4().hex[:8]
    b = uuid.uuid4().hex[:4]
    c = uuid.uuid4().hex[:8]
    random_index = randrange(len(countyName))
    item = countyName[random_index]
    d = item
    random_index_2 = randrange(len(countyName))
    item_2 = countyName[random_index_2]
    e = item_2
    f = random(10)
    g = uuid.uuid4().hex[:10]

    userDocument = {
            "userId": a,
            "password": b,
            "nickName": c,
            "physicalLocation": d,
            "alertLocation": e,
            "phoneNumber": f,
            "email": g
        }
    user.insert_one(userDocument)


# insert the document
