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
# messages(userId, content)

# sample link localhost:5000/api/message/mysql/create?userId=1a231414&content=Hello_World&location=Sierra
@app.route('/api/message/mysql/create', methods=['GET'])
def createMessages():
    # cursor.execute("CREATE TABLE messages (messageId VARCHAR(255) primary key NOT NULL AUTO_INCREMENT,userId VARCHAR(255), content VARCHAR(255), location VARCHAR(255))")
    sql = "INSERT INTO messages (userId, content, location) VALUES (%s, %s, %s)"
    userId = request.args.get('userId')
    content =request.args.get('content')
    location = request.args.get('location')
    val = (userId,content,location)
    cursor.execute(sql, val)
    connection.commit()
    cursor.execute("select * from messages")
    return jsonify(cursor.fetchall())


# sample link localhost:5000/api/message/mysql/read?messageId=14
# ocalhost:5000/api/message/mysql/read?location=Sierra
@app.route('/api/message/mysql/read', methods=['GET'])
def readMessage():
    location = request.args.get('location')
    messageId = request.args.get('messageId')
    if location == None:
        sql = "select messages.content FROM messages where messageId = %s "
        val = messageId
    elif messageId == None:
        sql = "select messages.content FROM messages where location = %s "
        val = location
    else:
        return '''<h1>An error achieve </h1><p>404</p >''',404
    cursor.execute(sql, val)
    # use request.args.get to fetch get params
    # e.g. GET /api/people/mysql?name=root
    return jsonify(cursor.fetchall())


# sample link http://localhost:5000/api/message/mysql/update?messageId=15&content=UpdatedHelloWorld
# http://localhost:5000/api/message/mysql/update?messageId=14
@app.route('/api/message/mysql/update', methods=['GET'])
def updateMessage():
    sql = "UPDATE messages SET content = %s WHERE messageId = %s"
    messageId = request.args.get('messageId')
    content = request.args.get('content')
    if (content == None):
        sql = "DELETE FROM messages where messageId = %s "
        val = request.args.get('messageId')
        cursor.execute(sql, val)
        connection.commit()
        cursor.execute("select * from messages")
        return jsonify(cursor.fetchall())
    val =  (content,messageId)
    cursor.execute(sql, val)
    connection.commit()
    cursor.execute(("select * from messages where messageId = %s"),(messageId))
    connection.commit()
    return jsonify(cursor.fetchall())

app.run()


