import pymongo


client = pymongo.MongoClient(host="mongodb+srv://developer:{password}@cluster0.juo1t.mongodb.net/NLP?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE".format(password="devo1234"), connect=False)

print(list(client['NLP']['TERMS'].find({})))

