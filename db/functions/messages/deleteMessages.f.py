import flask
from flask import request, jsonify
import numpy as np
import datetime
from bson.json_util import dumps
import pymysql.cursors
from flask import request

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Teamnull',
                             db='projectnull',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


cursor = connection.cursor()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# cursor.execute("CREATE TABLE messages IF NOT EXISTS (messageId INT ,userId VARCHAR(255), content VARCHAR(255),location VARCHAR(255))")
# localhost:5000/api/message/mysql/delete?messageId=1
@app.route('/api/message/mysql/delete', methods=['GET'])
def deleteMessage():
    sql = "DELETE FROM messages where messageId = %s "
    # use request.args.get to fetch get params
    # e.g. GET /api/people/mysql?name=root
    val = request.args.get('messageId')
    cursor.execute(sql, val)
    connection.commit()
    cursor.execute("select * from messages")
    return jsonify(cursor.fetchall())

# messagesDelete(1)
app.run()
