from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['patient']
db_collection=db['signup']
patient_1={
    "name":"Hansi",
    "age":"20",
    "email":"Hansi@gmail.com",
    "ph":"8899007766"
}
db_collection.insert_one(patient_1)




