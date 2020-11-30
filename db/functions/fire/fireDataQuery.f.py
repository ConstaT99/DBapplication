import flask
from flask import request, jsonify
import numpy as np
import datetime
from bson.json_util import dumps
import pymysql.cursors
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Teamnull',
                             db='projectnull',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()


@app.route('/api/location', methods=['GET'])
def getHistData():
    startDate = request.args.get("startDate")
    endDate = request.args.get("endDate")
    sql = "select * from calFire where incidentDateonlyCreated > %s or incidentDateonlyCreated < %s "
    val = (startDate,endDate)
    cursor.execute(sql, val)
    return jsonify(cursor.fetchall())

app.run()