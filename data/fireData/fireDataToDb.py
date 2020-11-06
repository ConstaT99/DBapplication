import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
fireData = open('data.csv', 'r')
reader = csv.DictReader(fireData)

client = MongoClient("localhost",27017)
db = client.projectnull
user = db.calFire

db.calFire.drop()

header= list(pd.read_csv('data.csv').columns)[1:]

# print(header)
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.calFire.insert_one(row)