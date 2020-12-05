import sys
sys.path.append('../')
import dbConnect
client = dbConnect.mongoConnect()
test = client.test
people = test.people
print(people.find_one())