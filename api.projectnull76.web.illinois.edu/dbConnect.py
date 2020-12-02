import pymongo
import pymysql
import pymysql.cursors


def mongoConnect():
    client = pymongo.MongoClient(
        "mongodb+srv://76rtao6:rtao676411@cluster0.8st24.gcp.mongodb.net/76rtao6?retryWrites=true&w=majority", 27017)
    return client


def mysqlConnect():
    connection = pymysql.connect(host='localhost',
                                 user='projectnull76_root',
                                 password='Teamnull1234',
                                 db='projectnull76_mysql',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
