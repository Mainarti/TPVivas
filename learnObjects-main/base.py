# _*_ coding: utf-8 -*_

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.learnObjects
coll = db.testes

def create_one(input):
    insert = coll.insert_one(input)
    print(insert.inserted_id)

def create_many(input):
    insert = coll.insert_many(input)
    print(insert.inserted_ids)

def read_one():
    read = coll.find_one()
    print(read)

def read_many(filter):
    for read in coll.find(filter):
        print(read)

def read_all():
    for read in coll.find():
        print(read)

def update_one(filter, newValue):
    update = coll.update_one(filter, {"$set":newValue})
    read_all()

def update_many(filter, newValues):
    update = coll.update_many(filter, {"$set": newValues})
    print(update.modified_count, "Documentos alterados")
    read_all()

def delete_one(filter):
    delete = coll.delete_one(filter)

def delete_many(filter):
    delete = coll.delete_many(filter)
    print(delete.deleted_count, "Documentos deletados")

def delete_all():
    delete = coll.delete_many({})
    print(delete.deleted_count, "Documentos deletados")