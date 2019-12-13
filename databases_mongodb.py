## DATABASES - MONGODB
"""
Python needs a MongoDB driver(Pymongo) to access the MongoDB database.
install Pymongo using python -m pip install PyMongo
import it to start using....

"""
import pymongo
#connect
conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn.learntrail
collection = db.notes
datadict = {'title':'Getting started', 'content':'mongodb'}
inserted = collection.insert_one(datadict)
print(inserted.inserted_id)
# INSERTING MULTIPLE DOCUMENTS/ROWS
collection2 = db.learners
learner_dict = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
insert = collection2.insert_many(learner_dict)
# print(insert.inserted_ids)

# SELECTING FROM DB
# 1 find_one()
"""
To select data from a collection in MongoDB, we can use the find_one() method.
The find_one() method returns the first occurrence in the selection """
one = collection2.find_one()
# print(one)

# 2 find()
""" select s all documents """
resp = collection2.find()

for res in resp:
    pass
    # print(res)

# Return Only Some Fields
""" 
use find({}, {options}) to get specific fields 
option:0 = means do not fetch it, 1 to fetch instead
the following will exclude id and return the rest.
"""
response = collection2.find({}, {'_id':0, 'name':1, 'address':1})
for  resp in response:
    pass
    # print(resp)
"""
One will get error if you specify a 1 and a 0 in the same object e.g.
========= find({},{ "name": 1, "address": 0 })

You HOWEVER not get error if one of the fields is the _id field
"""
# Filter the Result
""" 
to filter results pass a query object in find() as parameter 1.
example FIND WHERE NAME= BEN, RETURN ALL BUT _id
"""
filtered = collection2.find({'name': 'Ben'}, {'_id':0})
for f in filtered:
    pass
    # print(f)

# Advanced queries
"""
To make advanced queries you can use modifiers as values in the query object.
E.g. to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), 
use the greater than modifier: {"$gt": "S"}: as follows 
===== find({ "address": { "$gt": "S" } })
"""
#Python MongoDB Sort
"""
Use the sort() method to sort the result in ascending or descending order.
The sort() takes 2 params:-  "fieldname" and "direction"(ascending is the default direction).

example
"""
asorted = collection2.find().sort('name') # OR sort("name", 1) === ascending by name
dsorted = collection2.find().sort('name', -1) # === discending by name

#DELETING BY QUERY OBJECT
delete_one = collection2.delete_one({'name':'Ben'}) # delete where name = ben, delete just one entry

# Delete Many Documents
"""
To delete more than one document, use the delete_many() method.
The first parameter of the delete_many() method is a query object defining which documents to delete.
"""
delete_many = collection2.delete_many({'name':'Ben'}) # delete all where name = ben
deleted_count = delete_many.deleted_count

"""
use delete_many({}) to delete everything in a collection
use collection.drop() to delete collection
"""
# Python MongoDB Update 1
"""
You can update a record, or document as it is called in MongoDB, by using the update_one() method.
1. 1st parameter is a query object defining which document to update 
2. 2nd parameter is a query object defining the new values
NOTE -+-+ if there is more than 1 occurence, the first one gets updated.

Example....
"""
updated = collection2.update_one({'name':'Susan'},{'$set':{'name':'Alita'}}) # update 1
updated = collection2.update_many({'name':'Susan'},{'$set':{'name':'Alita'}}) # update many
res = updated.raw_result
print(res)
print('Query found ' + str(res['n']) + ' and updated ' + str(res['nModified']) + ' entries')
for x in collection2.find().limit(1):
    pass
    print(x)

## Python MongoDB Limit - using limit()
found = collection2.find().limit(1)
for f in found :
    print(f)

## Python MongoDB Distinct - using distinct()
uniques = collection2.find().limit(5).distinct('name')
for unique in uniques :
    print(unique)










