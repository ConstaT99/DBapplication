import flask
from flask import request, jsonify
from pymongo import MongoClient
import numpy as np
import datetime
from bson.json_util import dumps
import pymysql.cursors
from flask import request
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

client = MongoClient("localhost", 27017)
db = client.projectnull
user = db.user
calFire = db.calFire
messages = db.messages
images = db.images

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='teamnull',
                             db='projectnull',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/user', methods=['POST'])
def createUser():
    userId = request.args.get('userId')
    password = request.args.get('password')
    nickName = request.args.get('nickName')
    physicalLocation = request.args.get('physicalLocation')
    alertLocation = ''
    phoneNumber = request.args.get('phoneNumber')
    email = request.args.get('email')
    doc = user.find_one({"userId": userId}, {"_id": 0})

    if doc is not None:
        # raise error
        return '''Invalid request''', 400

    userDocument = {
        "userId": userId,
        "password": password,
        "nickName": nickName,
        "physicalLocation": physicalLocation,
        "alertLocation": alertLocation,
        "phoneNumber": phoneNumber,
        "email": email
    }

    user.insert_one(userDocument)

    return flask.jsonify('Success')


@app.route('/api/user/login', methods=['GET'])
def login():
    userId = request.args.get('userId')
    password = request.args.get('password')
    doc = user.find_one({"userId": userId})
    if doc is None or doc["password"] != password:
        # raise error
        return '''Invalid request''', 400

    return flask.jsonify('Success')


@app.route('/api/user', methods=['GET'])
def readUser():
    userId = request.args.get('userId')
    password = request.args.get('password')
    doc = user.find_one({"userId": userId})
    print(doc)
    if doc is None or doc["password"] != password:
        # raise error
        return '''Invalid request''', 400

    document = user.find_one({"userId": userId}, {"_id": 0})
    document["alertLocation"] = ",".join(document["alertLocation"])
    return flask.jsonify(document)


@app.route('/api/user', methods=['PUT'])
def editUser():
    userId = request.args.get('userId')
    password = request.args.get('password')
    nickName = request.args.get('nickName')
    physicalLocation = request.args.get('physicalLocation')
    alertLocation = request.args.get('alertLocation').split(',')
    phoneNumber = request.args.get('phoneNumber')
    email = request.args.get('email')
    doc = user.find_one({"userId": userId})
    if doc is None or doc["password"] != password:
        # raise error
        return '''Invalid request''', 400

    user.update_one({"userId": userId}, {"$set": {
        "nickName": nickName, "physicalLocation": physicalLocation, "alertLocation": alertLocation, "phoneNumber": phoneNumber, "email": email}})

    document = user.find_one({"userId": userId}, {"_id": 0})
    document["alertLocation"] = ",".join(document["alertLocation"])
    return flask.jsonify(document)


@app.route('/api/user', methods=['DELETE'])
def deleteUser():
    userId = request.args.get('userId')
    password = request.args.get('password')
    doc = user.find_one({"userId": userId})
    if doc is None or doc["password"] != password:
        # raise error
        return '''Invalid request''', 400

    user.delete_one({"userId": userId})
    return flask.jsonify('Success')


# @app.route('/api/location/messages', methods=['POST'])
# def postComment():
#     userId = "binyaoj222"
#     location = request.args.get('location')
#     message = request.args.get('message')

#     messagesDocument = {
#         "userId": userId,
#         "location": location,
#         "message": message
#     }
#     messages.insert_one(messagesDocument)
#     return flask.jsonify('Success')


# @app.route('/api/location/messages', methods=['GET'])
# def getComment():
#     userId = request.args.get('userId')
#     location = request.args.get('location')

#     if location is None:
#         comments = messages.find(
#             {"userId": userId}, {"_id": 0})
#     else:
#         comments = messages.find(
#             {"location": location}, {"_id": 0})

#     return flask.jsonify(list(comments))


@app.route('/api/location', methods=['GET'])
def getHistData():
    startDate = request.args.get("startDate")
    endDate = request.args.get("endDate")
    events = calFire.find({"incident_dateonly_created": {"$gt": startDate, "$lt": endDate}}, {"_id": 0})
    return flask.jsonify(list(events))


@ app.route('/api/userInFire', methods=['GET'])
def userInFire():
    # startDate = "20200806"  # request.args.get("startDate")
    # endDate = "20201106"  # request.args.get("endDate")
    topDocs = list(calFire.aggregate([
        {"$match": {"incident_is_final": "False"}},
        {"$group": {
            "_id": "$incident_county",
            "numFires": {"$sum": 1},
        }}
    ]))
    topCounties = list(map(lambda document: document["_id"], topDocs))
    print(topCounties)
    return flask.jsonify(list(user.find({"physicalLocation": {"$in": topCounties}}, {"_id": 0})))


@ app.route('/api/userInAlert', methods=['GET'])
def userInAlert():
    topDocs = list(calFire.aggregate([
        {"$match": {"incident_is_final": "False"}},
        {"$group": {
            "_id": "$incident_county",
            "numFires": {"$sum": 1},
        }}
    ]))
    topCounties = list(map(lambda document: document["_id"], topDocs))
    print(topCounties)
    return flask.jsonify(list(user.find({"alertLocation": {"$in": topCounties}}, {"_id": 0})))


@ app.route('/api/location/messages', methods=['POST'])
def createMessages():
    # cursor.execute("CREATE TABLE messages (messageId VARCHAR(255) primary key NOT NULL AUTO_INCREMENT,userId VARCHAR(255), content VARCHAR(255), location VARCHAR(255))")
    sql = "INSERT INTO messages (userId, content, location) VALUES (%s, %s, %s)"
    userId = request.args.get('userId')
    content = request.args.get('content')
    location = request.args.get('location')
    val = (userId, content, location)
    cursor.execute(sql, val)
    connection.commit()
    cursor.execute("select * from messages")
    return jsonify(cursor.fetchall())


# sample link localhost:5000/api/message/mysql/read?messageId=14
# ocalhost:5000/api/message/mysql/read?location=Sierra
@ app.route('/api/location/messages', methods=['GET'])
def readMessage():
    location = request.args.get('location')
    userId = request.args.get('userId')
    if location == None:
        sql = "select * FROM messages where userId = %s "
        val = userId
    elif userId == None:
        sql = "select * FROM messages where location = %s "
        val = location
    else:
        return '''<h1>An error achieve </h1><p>404</p >''', 404
    cursor.execute(sql, val)
    # use request.args.get to fetch get params
    # e.g. GET /api/people/mysql?name=root
    return jsonify(cursor.fetchall())


# sample link http://localhost:5000/api/message/mysql/update?messageId=15&content=UpdatedHelloWorld
# http://localhost:5000/api/message/mysql/update?messageId=14
@ app.route('/api/location/messages', methods=['PUT'])
def updateMessage():
    sql = "UPDATE messages SET content = %s WHERE messageId = %s"
    messageId = request.args.get('messageId')
    content = request.args.get('content')
    if len(content) == 0:
        sql = "DELETE FROM messages where messageId = %s "
        val = request.args.get('messageId')
        cursor.execute(sql, val)
        connection.commit()
        cursor.execute("select * from messages")
        return jsonify(cursor.fetchall())
    val = (content, messageId)
    cursor.execute(sql, val)
    connection.commit()
    cursor.execute(
        ("select * from messages where messageId = %s"), (messageId))
    connection.commit()
    return jsonify(cursor.fetchall())


@ app.route('/api/people/mysql', methods=['GET'])
def api_mysql():
    sql = "SELECT * FROM people WHERE name=%s"
    # use request.args.get to fetch get params
    # e.g. GET /api/people/mysql?name=root
    cursor.execute(sql, request.args.get('name'))
    return jsonify(cursor.fetchall())

@app.route('/api/image', methods=['POST'])
def createImage():
    target = os.path.join(APP_ROOT, 'images/')  # folder path
    if not os.path.isdir(target):
        os.mkdir(target)     # create folder if not exits
    userId = request.form['userId']
    incidentId = request.form['incidentId']

    image = request.files.getlist("fireImage")[0]
    imageDocument = {
        "userId": userId,
        "incidentId": incidentId
    }
    insertedId = str(images.insert_one(imageDocument).inserted_id)
    filename = insertedId + ".jpg"
    destination = "/".join([target, filename])
    image.save(destination)
    return flask.jsonify(insertedId)


@app.route('/api/image/<imageId>', methods=['GET'])
def readImage(imageId):
    print(images.find_one())
    doc = images.find_one({"_id": ObjectId(imageId)})
    if doc is None:
        # raise error
        return '''Invalid request''', 400
    return send_from_directory('./images/', imageId + ".jpg")

# @app.route('/api/image/<imageId>', methods=['DELETE'])
# def deleteImage():
#     doc = images.find_one({"_id": ObjectId(imageId)})
#     if doc is None:
#         # raise error
#         return '''Invalid request''', 400
#     document = images.delete_one({"imageId": imageId})
#     return flask.jsonify(document)

@app.route('/api/image/<imageId>/like/<userId>', methods=['PUT'])
def likeImage():
    doc = images.find_one({"_id": ObjectId(imageId)})
    # doc = images.find_one({"imageId": imageId})
    if doc is None:
        # raise error
        return '''Invalid request''', 400
    image.update_one({"imageId": imageId}, {"$inc": {
        "like": 1}})
    document = images.find_one({"_id": ObjectId(imageId)})
    return flask.jsonify(document)

@app.route('/api/image/popular/<incidentId>', methods=['GET'])
def popularImage(incidentId):
    limit = int(request.args.get('limit'))
    documents = images.find({"incidentId": incidentId}, {"_id": 0, "imageId": "$_id", "incidentId": 1, "userId": 1, "comments": 1, "like": 1}).sort(
        "like", pymongo.DESCENDING).limit(limit)

    if documents is None:
        return '''Invalid request''', 400
    result = list(documents)
    for document in result:
        document["imageId"] = str(document["imageId"].binary.hex())
    return flask.jsonify(result)



# @app.route('/js/<path:path>')
# def send_js(path):
#     return send_from_directory('js', path)

app.run()
