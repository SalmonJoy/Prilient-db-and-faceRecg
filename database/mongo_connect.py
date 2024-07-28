import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["mywebsite"]
mycol = mydb["users"]

new_entry = {"name":"Vaishnavi Pillai","email":"vaishnavi@gmail.com"}

obj = mycol.insert_one(new_entry)
print("New entry id is", obj.inserted_id)

for result in mycol.find():
    print(result)