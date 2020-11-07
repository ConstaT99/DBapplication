import flask
from flask import request, jsonify
import numpy as np
import datetime
from bson.json_util import dumps
import pymysql.cursors
from flask import request

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='teamnull',
                             db='projectnull',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# cursor.execute("CREATE DATABASE projectnull")
cursor.execute("CREATE TABLE messages (messageId int NOT NULL AUTO_INCREMENT,userId VARCHAR(255), content VARCHAR(255), location VARCHAR(255), primary key(messageId))")