#!/usr/bin/env python3
from pymongo import MongoClient
import numpy as np
import dns
import datetime

client = MongoClient('localhost', 27017)
db = client.test # create test collection
people = db.people

# create person document
personDocument = {
  "name": { "first": "Alan", "last": "Turing" },
  "birth": datetime.datetime(1912, 6, 23),
  "death": datetime.datetime(1954, 6, 7),
  "contribs": [ "Turing machine", "Turing test", "Turingery" ],
  "views": 1250000
}

# insert the document
personID = people.insert_one(personDocument).inserted_id
if (personID != None):
  print("inserted sucess")