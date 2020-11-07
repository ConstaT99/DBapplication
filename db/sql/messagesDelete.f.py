import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Teamnull',
                             db='projectnull',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



cursor = connection.cursor()


cursor.execute("CREATE TABLE messages IF NOT EXISTS (messageId INT ,userId VARCHAR(255), content VARCHAR(255),location VARCHAR(255))")

@app.route('/api/people/mysql', methods=['GET'])
def messagesDelete():
    sql = "DELETE FROM messages where messageId=%i "
    # use request.args.get to fetch get params
    # e.g. GET /api/people/mysql?name=root
    cursor.execute(sql, request.args.get('messageId'))
    return jsonify(cursor.fetchall())
