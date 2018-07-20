#！usr/bin/env python

__author__ = 'Camille'

import pymongo
from bson.objectid import ObjectId

conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn.testdb2
# newcol = db['newcol']
# db.newcol.insert({"name":'yanying','province':'江苏','age':25})
# db.col.insert([
#     {"name":'yanying','province':'江苏','age':25},
#     {"name":'张三','province':'浙江','age':24},
#     {"name":'张三1','province':'浙江1','age':25},
#     {"name":'张三2','province':'浙江2','age':26},
#     {"name":'张三3','province':'浙江3','age':28},
# ])
# print(db.col.find_one())

# for item in db.col.find():
#     print(item)

# for item in db.col.find({'name':'yanying'}):
#     print(item)
db.col.update({'_id':ObjectId('5b514f64374c323268821120')},{'$set':{'name':'王二麻33333'}})