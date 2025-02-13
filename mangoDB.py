import pymongo
import logging

# #url = 172.24.6.84
# url="172.24.6.190"
# #url=https://mccd-infrascalingqaes.matildacloud.com/
# #url = mongo
# username = "admin"
# password = "Matilda7#"
# #port = 27017
# port = 30020
# database ="Assessment"
# #sample_uri = mongodb+srv://<USERNAME>:<PASSWORD>@cluster-test.fndbj.mongodb.net/UserData?retryWrites=true&w=majority
# # uri =
# url_flag = True

myclient = pymongo.MongoClient("mongodb://admin:Matilda7%23@mccd-infradev.matildacloud.com:30020/")

mydb  = myclient["matildacost"]
collection = mydb["mcost_oci"]

result = collection.find({"tfService":"VCN"})

for i in result:
    print(f"{i["serviceIdentifier"]}: {(i["name"])}")
    print(i.keys())
    
    