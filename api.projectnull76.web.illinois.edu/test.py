import dbConnect
import pymongo
from bson.objectid import ObjectId

client = dbConnect.mongoConnect()
db = client.projectnull
images = db.images
user = db.user
imageId = "5fc682437810c1c9f988a0e1"
doc = images.find_one({"_id": ObjectId(imageId)})
doc2 = user.find_one({"userId": doc["userId"]})


print(doc2["email"])