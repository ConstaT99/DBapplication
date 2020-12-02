import flask
from flask import request, jsonify
import pymongo
from flask import request
from flask_cors import CORS
from flask.helpers import send_from_directory
from bson.objectid import ObjectId
import sendEmail
import dbConnect
import os


app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

client = dbConnect.mongoConnect()

db = client.projectnull
user = db.user
images = db.images

# def create_connection():
#     return pymysql.connect(host='localhost',
#                            user='root',
#                            password='teamnull',
#                            db='projectnull',
#                            charset='utf8mb4',
#                            cursorclass=pymysql.cursors.DictCursor)


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Success!</h1>'''


@app.route('/api/user', methods=['POST'])
def createUser():
    userId = request.form.get('userId')
    password = request.form.get('password')
    nickName = request.form.get('nickName')
    physicalLocation = request.form.get('physicalLocation')
    phoneNumber = request.form.get('phoneNumber')
    email = request.form.get('email')
    likes = []
    uploads = []
    comments = []
    doc = user.find_one({"userId": userId}, {"_id": 0})

    if doc is not None:
        # raise error
        return '''Invalid request''', 400

    userDocument = {
        "userId": userId,
        "password": password,
        "nickName": nickName,
        "physicalLocation": physicalLocation,
        "phoneNumber": phoneNumber,
        "email": email,
        "likes": likes,
        "uploads": uploads,
        "comments": comments
    }

    user.insert_one(userDocument)

    return flask.jsonify('Success')


@app.route('/api/user/login', methods=['POST'])
def login():
    userId = request.form.get('userId')
    password = request.form.get('password')
    doc = user.find_one({"userId": userId})
    if doc is None or doc["password"] != password:
        # raise error
        return '''Invalid request''', 400

    return flask.jsonify('Success')


@app.route('/api/user/<userId>', methods=['GET'])
def readUser(userId):
    doc = user.find_one({"userId": userId})
    if doc is None:
        # raise error
        return '''Invalid request''', 400

    document = user.find_one({"userId": userId}, {"_id": 0})
    return flask.jsonify(document)


@app.route('/api/user/<userId>', methods=['PUT'])
def editUser(userId):
    password = request.form.get('password')
    nickName = request.form.get('nickName')
    physicalLocation = request.form.get('physicalLocation')
    phoneNumber = request.form.get('phoneNumber')
    email = request.form.get('email')
    doc = user.find_one({"userId": userId})
    if doc is None or doc["password"] != password:
        # raise error
        return '''Invalid request''', 400

    user.update_one({"userId": userId}, {"$set": {
        "nickName": nickName, "physicalLocation": physicalLocation, "phoneNumber": phoneNumber, "email": email}})

    document = user.find_one({"userId": userId}, {"_id": 0})
    return flask.jsonify(document)


@app.route('/api/user/<userId>', methods=['DELETE'])
def deleteUser(userId):
    doc = user.find_one({"userId": userId})
    if doc is None:
        # raise error
        return '''Invalid request''', 400

    user.delete_one({"userId": userId})
    return flask.jsonify('Success')


@app.route('/api/location', methods=['GET'])
def getHistData():
    connection = dbConnect.mysqlConnect()
    cursor = connection.cursor()
    startDate = request.args.get("startDate")
    endDate = request.args.get("endDate")
    sql = "select * from calFire where incidentDateonlyCreated > %s and incidentDateonlyCreated < %s "
    val = (startDate, endDate)
    cursor.execute(sql, val)
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(cursor.fetchall())


@ app.route('/api/admin/userInFire/<userId>', methods=['GET'])
def userInFire(userId):
    doc = user.find_one({"userId": userId})
    if doc is None or doc["admin"] is None:
        # raise error
        return '''Invalid request''', 400

    connection = dbConnect.mysqlConnect()
    cursor = connection.cursor()
    sql = "select incidentCounty from calFire where incidentIsFinal = 0 "
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()

    fireCounties = set()
    document = list(cursor.fetchall())
    for line in document:
        for county in line['incidentCounty'].split(", "):
            fireCounties.add(county)

    return flask.jsonify(list(user.find({"physicalLocation": {"$in": list(fireCounties)}}, {"_id": 0})))


@ app.route('/api/admin/popularIncidents/<userId>', methods=['GET'])
def popularIncidents(userId):
    doc = user.find_one({"userId": userId})
    if doc is None or doc["admin"] is None:
        # raise error
        return '''Invalid request''', 400

    connection = dbConnect.mysqlConnect()
    cursor = connection.cursor()
    sql = "select calFire.incidentName, count(*) as count from calFire join comments on calFire.incidentId = comments.incidentId group by calFire.incidentId order by count(*) desc limit 10"
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()

    document = list(cursor.fetchall())
    return flask.jsonify(document)


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
        "incidentId": incidentId,
        "comments": [],
        "like": 0
    }
    insertedId = str(images.insert_one(imageDocument).inserted_id)
    filename = insertedId + ".jpg"
    destination = "/".join([target, filename])
    image.save(destination)
    user.update_one({"userId": userId}, {"$push": {
        "uploads": insertedId}})
    return flask.jsonify(insertedId)


@app.route('/api/image/<imageId>', methods=['GET'])
def readImage(imageId):
    doc = images.find_one({"_id": ObjectId(imageId)})
    if doc is None:
        # raise error
        return '''Invalid request''', 400
    return send_from_directory('./images/', imageId + ".jpg")


@app.route('/api/image/popular/<incidentId>', methods=['GET'])
def popularImage(incidentId):
    limit = int(request.args.get('limit'))
    documents = images.find({"incidentId": incidentId}, {"_id": 1, "imageId": 1, "incidentId": 1, "userId": 1, "comments": 1, "like": 1}).sort(
        "like", pymongo.DESCENDING).limit(limit)

    if documents is None:
        return '''Invalid request''', 400
    result = list(documents)
    for document in result:
        document["imageId"] = str(document["_id"].binary.hex())
        del document["_id"]
    return flask.jsonify(result)


@ app.route('/api/comment', methods=['POST'])
def createComment():
    connection = dbConnect.mysqlConnect()
    cursor = connection.cursor()
    sql = "INSERT INTO comments (userId, content, imageId, incidentId) VALUES (%s, %s, %s, %s)"
    userId = request.form.get('userId')
    imageId = request.form.get('imageId')
    content = request.form.get('content')
    doc = user.find_one({"userId": userId})
    if doc is None:
        connection.close()
        return '''Invalid request''', 400
    doc2 = images.find_one({"_id": ObjectId(imageId)})
    incidentId = doc2["incidentId"]
    val = (userId, content, imageId, incidentId)
    if doc2 is None:
        connection.close()
        return '''Invalid request ''', 400

    cursor.execute(sql, val)
    commentId = cursor.lastrowid
    user.update_one({"userId": userId}, {"$push": {
        "comments": commentId}})

    images.update_one({"_id": ObjectId(imageId)}, {"$push": {
        "comments": commentId}})
    # send Email
    targetuser = doc2["userId"]  # get post userid
    doc3 = user.find_one({"userId": targetuser})
    if doc3 is None:
        connection.close()
        return '''Invalid request''', 400
    targetemail = doc3['email']
    connection.commit()
    cursor.close()
    connection.close()
    sendEmail.sendEmail(targetemail, content, imageId)
    return flask.jsonify('Success')


# sample link localhost:5000/api/message/mysql/read?messageId=14
# ocalhost:5000/api/message/mysql/read?location=Sierra
@ app.route('/api/comment/<commentId>', methods=['GET'])
def readComment(commentId):
    connection = dbConnect.mysqlConnect()
    cursor = connection.cursor()
    sql = "SELECT * FROM comments where commentId = %s "
    val = commentId
    cursor.execute(sql, val)
    connection.commit()
    cursor.close()
    connection.close()
    result = cursor.fetchone()
    print(result)
    return jsonify(result)


# sample link http://localhost:5000/api/message/mysql/update?messageId=15&content=UpdatedHelloWorld
# http://localhost:5000/api/message/mysql/update?messageId=14
@ app.route('/api/comment/<commentId>', methods=['PUT'])
def updateComment(commentId):
    connection = dbConnect.mysqlConnect()
    cursor = connection.cursor()
    sql = "UPDATE comments SET content = %s WHERE commentId = %s AND userId = %s"
    userId = request.form.get('userId')
    content = request.form.get('content')
    val = (content, commentId, userId)
    cursor.execute(sql, val)
    cursor.execute(
        ("SELECT * from comments where commentId = %s"), (commentId))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(cursor.fetchone())


@app.route('/api/image/<imageId>/like/<userId>', methods=['PUT'])
def likeImage(imageId, userId):
    doc = images.find_one({"_id": ObjectId(imageId)})
    if doc is None:
        # raise error
        return '''Invalid request''', 400

    # userId is the id of user who click the like button
    result = user.find_one(
        {"$and": [{"userId": userId}, {"likes": {"$elemMatch": {"$eq": imageId}}}]})

    if result is None:
        images.update_one({"_id": ObjectId(imageId)}, {"$inc": {
            "like": 1}})
        user.update_one({"userId": userId}, {"$push": {
            "likes": imageId}})
    else:
        images.update_one({"_id": ObjectId(imageId)}, {"$inc": {
            "like": -1}})
        user.update_one({"userId": userId}, {"$pull": {
            "likes": imageId}})
    return flask.jsonify(images.find_one({"_id": ObjectId(imageId)}, {"_id": 0}))


if __name__ == '__main__':
    app.run()
