import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.lwtest
collection = db.test1
res = collection.find()
for i in res:
    print(i)
