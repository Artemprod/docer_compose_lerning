from pymongo import MongoClient
from pprint import pprint
mongo_url = "mongodb://mongo:27017"
client = MongoClient(mongo_url)

# Use the client to list databases
dbs_list = client.list_databases()
pprint(list(dbs_list))