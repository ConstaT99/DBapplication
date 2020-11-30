import flask
from flask import request, jsonify
from pymongo import MongoClient
import numpy as np
import datetime
from bson.json_util import dumps
import pymongo
from flask import request

client = MongoClient("localhost",27017)
db = client.projectnull
location = db.location


def funcname(parameter_list):
    """
    docstring
    """
    pass
