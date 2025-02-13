import pymongo

myclient = pymongo.MongoClient("mongodb://admin:Matilda7%23@172.24.6.190:30020")
mydatabase = myclient["matildacost"]
mycol = mydatabase.mcost_gcp_raw

print(mydatabase.list_collection_names())
print(mycol.find_one({"skuId": "1AD1-5B57-590A"}))