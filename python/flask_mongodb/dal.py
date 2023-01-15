from pymongo import MongoClient
#from models import SavingAccount,CheckingAccount

class dao:
    client=MongoClient('mongodb://localhost:27017')
    def __init__(self,db,collection) -> None:
        self.db=dao.client[db]
        self.collection=self.db[collection]
    def list(self):
        objects=[]
        for object in self.collection.find():
            objects.append(object)
        return objects
    def add(self,object):
        if self.exist(object)==None:
            self.collection.insert_one(object)
        else:
            raise Exception(str(object['_id'])+' already exist')
    def delete(self,id):
        self.collection.delete_one({"_id":id})
    def update(self,object):
        self.collection.update_one({'_id':object['_id']},{'$set':object})
    def exist(self,object):
        results=self.collection.find_one({'_id':object['_id']})
        return results

'''
import json
client=MongoClient('mongodb://localhost:27017')
print(client.list_database_names())
#get database reference
db=client['banking']
#get Collection
accountsCol=db['Accounts']
accountsCol.insert_many([
    {'_id':1,'balance':10000,'type':'S'},
    {'_id':2,'balance':9000,'type':'S'},
    {'_id':3,'balance':0,'type':'C'},
    {'_id':4,'balance':7000,'type':'C'}

])


d=json.loads('{"interestRate":0.01,"account":4,"balance":7000}')
print(SavingAccount(**d))
p=vars(SavingAccount(0.05,1,1200))

print(p)
#accountsCol.insert_one(p)
#listAccounts=accountsCol.find().sort([('type',1),('balance',-1)])
accountsCol.update_many({'balance':0},{'$set':{'balance':100}})
listAccounts=accountsCol.find()
accountsCol.delete_many({'balance':{"$lt":0}})
for account in listAccounts:
    print(account)

'''
