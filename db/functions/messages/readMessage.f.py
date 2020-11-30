import flask
from flask import request, jsonify
import numpy as np
import datetime
from bson.json_util import dumps
import pymysql.cursors
from flask import request

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Teamnull',
                             db='projectnull',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/message/mysql/read', methods=['GET'])
def readMessage():
    location = request.args.get('location')
    messageId = request.args.get('messageId')
    if location == None:
        sql = "select messages.content FROM messages where messageId = %s "
        val = messageId
    else if messageId == None:
        sql = "select messages.content FROM messages where location = %s "
        val = location
    cursor.execute(sql, val)
    # use request.args.get to fetch get params
    # e.g. GET /api/people/mysql?name=root
    return jsonify(cursor.fetchall())

# messagesDelete(1)
app.run()