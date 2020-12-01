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

# cursor.execute("CREATE DATABASE projectnull")
cursor.execute('''CREATE TABLE calFire
        (incidentName varchar(255),
        incidentIsFinal varchar(255),
        incidentDateLastUpdate varchar(255),
        incidentDateCreated varchar(255),
        incidentCounty varchar(255),
        incidentLocation varchar(255),
        incidentAcresBurned varchar(255),
        incidentContainment varchar(255),
        incidentLongitude varchar(255),
        incidentLatitude varchar(255),
        incidentType varchar(255),
        incidentId varchar(255),
        incidentUrl varchar(255),
        incidentDateExtinguished varchar(255),
        incidentDateonlyExtinguished varchar(255),
        incidentDateonlyCreated varchar(255),
        isActive varchar(255),
        calfireIncident varchar(255),
        notificationDesired varchar(255),
        primary key(incidentId))
                ''')
