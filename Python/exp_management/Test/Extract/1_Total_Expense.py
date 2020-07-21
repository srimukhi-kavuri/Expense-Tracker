#expense by month

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["expense_db"]
mycol = mydb["expense"]

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:
    db = client.expense_db

    agr = [{'$group': {'_id': 1, 'all': {'$sum': '$price'}}}]

    val = list(db.expense.aggregate(agr))

    print('The sum of prices is {}'.format(val[0]['all']))





#     date = ""
#     date=i['date']
#     split_date = date.split('/')
#     print(split_date[1])
#     if split_date[1]==
#
# print(date,type(date))

#date="02/02/2020"





