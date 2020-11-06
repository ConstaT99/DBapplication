#!/usr/bin/env python3
from pymongo import MongoClient
import numpy as np
import datetime

client = MongoClient("localhost",27017)
db = client.projectnull
user = db.user

# create person document
userDocument = {
  "userId": "404DontTrustTears",
  "password": "areukiddingme",
  "nickName": "small4",
  "alertLocation": "SF",
  "phoneNumber": 1234567,
  "email" : "411411@gmail.com"
}
userID = user.insert_one(userDocument).inserted_id