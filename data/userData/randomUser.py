import flask
from flask import request, jsonify
from pymongo import MongoClient
import numpy as np
import datetime
from bson.json_util import dumps
import pymongo
from flask import request
import uuid
from random import randrange, random, randint

client = MongoClient('localhost', 27017)
db = client.projectnull  # create test collection
user = db.user

countyName = ["Alameda","Alpine","Amador","Butte","Calaveras",
"Colusa","Contra_Costa","Del_Norte","El_Dorado ","Fresno","Glenn",
"Humboldt","Imperial","Inyo","Kern","Kings","Lake","Lassen",
"Los_Angeles ","Madera","Marin","Mariposa","Mendocino","Merced","Modoc",
"Mono","Monterey","Napa","Nevada","Orange","Placer","Plumas","Riverside",
"Sacramento","San_Benito","San_Bernardino","San_Diego","San_Francisco","San_Joaquin",
"San_Luis_Obispo","San_Mateo","Santa_Barbara","Santa_Clara","Santa_Cruz","Shasta",
"Sierra","Siskiyou","Solano","Sonoma","Stanislaus","Sutter","Tehama","Trinity",
"Tulare","Tuolumne","Ventura","Yolo","Yuba"]


def random_with_n_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

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
    f = random_with_n_digits(10)
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
